# Test Results — Warm Runtime Pool / Custom Sandbox Image

**PR:** [#609 — Custom images in the warm runtime pool](https://github.com/OpenHands/docs/pull/609)  
**Environment:** `replicated-test-03` (GCP us-central1-b, project `app-team-sandbox-012345`)  
**Installer version:** OpenHands Enterprise KOTS chart, sequence 5  
**runtime-api image:** `openhands-runtime-api` (runtime-api chart embedded in openhands chart)  
**Date:** 2026-09-15

---

## Prerequisites

- A running OHE install (k0s embedded cluster, `openhands` namespace)
- `KUBECONFIG=/var/lib/embedded-cluster/k0s/pki/admin.conf`
- `kubectl` at `/var/lib/embedded-cluster/bin/kubectl` (prefix with `sudo -E`)
- Admin password set via KOTS: `kubectl-kots set config openhands -n default admin_password=<password>`  
  → redeploys runtime-api with `ADMIN_PASSWORD` env var via a Kubernetes Secret
- The `default-api-key` Secret in the `openhands` namespace is the runtime-api API key

### Admin auth protocol (for scripts)

The admin endpoints use a PBKDF2 challenge-response. **Important:** this protocol changed
between sessions — read `management_fastapi.py` to confirm before scripting:

```
GET  /api/admin/challenge  →  { challenge, salt, iterations }
client_hash = PBKDF2-HMAC-SHA256(password, (salt+challenge).encode('utf-8'), iterations, dklen=32)
POST /api/admin/login      { challenge, hash: client_hash }  →  { token }
PUT  /api/admin/warm-runtime-configs/{name}  (Bearer {token})
```

> **Note on password:** `KOTS set config` did NOT apply the literal string we passed for
> `admin_password`. The pod's `ADMIN_PASSWORD` env var was a 20-character auto-generated
> value (first 4 chars `Warm`, last 3 `26!`). Verify the actual value before scripting:
>
> ```bash
> kubectl exec -n openhands <runtime-api-pod> -c runtime-api -- python3 -c \
>   "import os; p=os.environ['ADMIN_PASSWORD']; print(len(p), p[:4], p[-3:])"
> ```

---

## Test 1 — Basic warm config lifecycle (DB-backed entry)

### Steps

1. **Baseline list** — confirm only `v1_current` (source=file) is present:
   ```bash
   curl -H "X-API-Key: $API_KEY" https://runtime-api.<domain>/api/warm-runtime-configs
   ```

2. **Save a new config** — `PUT /api/admin/warm-runtime-configs/custom-test` with payload:
   ```json
   {
     "image": "images.r9.all-hands.dev/proxy/openhands/ghcr.io/openhands/agent-server:1.46.0-python",
     "working_dir": "/workspace/project",
     "command": ["/usr/local/bin/openhands-agent-server", "--port", "60000"],
     "environment": { <standard env vars — copy from v1_current response> },
     "count": 1,
     "run_as_user": 10001, "run_as_group": 10001, "fs_group": 10001
   }
   ```

3. **Wait ~1 min** for the reconciler CronJob (`openhands-runtime-api-warm-runtimes`) to run.

4. **Verify warm pod created:**
   ```bash
   kubectl get pods -n openhands | grep "^runtime-"
   # A new runtime-<id> pod appears with AGE < 2m
   ```

5. **Verify from reconciler log:**
   ```
   "Created warm runtime 1/1 for custom-test: <runtime-id>"
   "Warm runtime pool for custom-test is full"
   "warm_runtime_counts": {"v1_current": 3, "custom-test": 1}
   ```

6. **Claim the warm pod** — send `/start` with matching env (no LMNR vars) →
   response is immediate with `status: starting` and the pre-warmed `runtime_id`.

### Results

| Step | Expected | Actual |
|---|---|---|
| Baseline list | `v1_current` source=file, count=null | ✅ Matches |
| Save config | 200, source=db, count=1 | ✅ Matches |
| Reconciler creates pod | Pod Running within ~1 min | ✅ Pod `uyztcfaeefeidjnd`, Running at 48s |
| List shows both configs | v1_current (file) + custom-test (db) | ✅ Both listed |
| Claim warm pod | Immediate response, correct runtime_id | ✅ `uyztcfaeefeidjnd` claimed, session `test-custom-sandbox-001` |
| App restarts | Zero | ✅ openhands pod restarts=0 throughout |

---

## Test 2 — Overlay semantics (DB overrides ConfigMap)

### Steps

1. PUT a DB entry named `v1_current` with `count: 2`.
2. List configs — `v1_current` switches to source=db, count=2.
3. DELETE the DB `v1_current` entry.
4. List again — `v1_current` reverts to source=file, count=null.

### Results

| Step | Expected | Actual |
|---|---|---|
| Save DB v1_current | source=db, count=2 | ✅ |
| Delete DB v1_current | source reverts to file | ✅ Instant revert |

---

## Test 3 — Real image pull (uncached tag)

This test validates that the reconciler correctly pulls an image that is **not** in
the node's containerd cache, rather than just scheduling a pod that happens to find
the image already cached.

### Setup

Confirmed via `k0s ctr images list` that only `agent-server:1.46.0-python` was cached.
Probed `1.45.0-python`, `1.44.0-python`, `1.43.0-python` via a k8s Job with the
`openhands-registry` pull secret — all pulled and completed successfully.
Then removed `1.45.0-python` from containerd before the test:

```bash
sudo /var/lib/embedded-cluster/bin/k0s ctr images remove \
  images.r9.all-hands.dev/proxy/openhands/ghcr.io/openhands/agent-server:1.45.0-python
```

### Steps

Same as Test 1, but the config image is `agent-server:1.45.0-python` (not cached).

### Results

| Step | Expected | Actual |
|---|---|---|
| Save `v1-realimage` config | 200, source=db, count=1 | ✅ T0=14:31:12Z |
| Reconciler detects deficit | `"Missing 1 runtimes for v1-realimage, creating 1..."` | ✅ T=14:32:07Z (+55s) |
| Pod created with correct image | `agent-server:1.45.0-python`, Running | ✅ Pod `zlzsnlpielsqrqea` Running (pull from Replicated proxy) |

**End-to-end pull time: ~60s** (reconciler cycle) + image pull (~90s from cold). Total:
pod reached Running state within ~3 min of the PUT call.

---

## Key Observations

### What works exactly as documented

- `PUT /admin/warm-runtime-configs/{name}` creates or updates a config without restart.
- DB entries appear in `GET /api/warm-runtime-configs` immediately.
- Reconciler (1-min CronJob) detects the deficit and creates the warm pod.
- DB entry with the same name as a ConfigMap entry **overrides** it (source switches to `db`).
- Deleting a DB entry **instantly reverts** to the ConfigMap value.
- Warm pod matching is **env-var exact** — a request with missing env vars does NOT match
  a warm pod that has extra env vars. If `v1_current` (file) has LMNR telemetry vars but
  your DB config doesn't, they will be treated as separate pools.
- Pool replenishment after claim is automatic on the next reconciler cycle.

### Findings worth noting in the PR / docs

1. **Admin password sourcing:** The KOTS `admin_password` config field may produce a
   different value than the literal string passed. Always verify `ADMIN_PASSWORD` inside
   the pod before scripting against the admin API.

2. **Auth protocol:** The challenge-response protocol is:
   ```
   combined_salt = (challenge_response.salt + challenge_response.challenge).encode('utf-8')
   client_hash   = PBKDF2-HMAC-SHA256(admin_password, combined_salt, iterations, dklen=32)
   POST /api/admin/login { "challenge": ..., "hash": client_hash }  →  { "token": ... }
   ```
   The field is `hash` (not `signature`), the login endpoint is `/admin/login` (not
   `/admin/token`), and the PBKDF2 salt is the concatenated string, not fixed `b"openhands"`.

3. **Env-var matching is strict.** The reconciler's `warm_runtime_matches` compares the
   full env dict. If you create a DB config that omits vars present in the file config
   (e.g., LMNR telemetry), the DB config gets its own isolated pool. This is correct
   behavior but may surprise operators who expect a DB entry to inherit the file config's
   env.

4. **Image pull secret is `openhands-registry`.** All warm pods can pull any image
   reachable via the Replicated proxy (`images.r9.all-hands.dev/proxy/openhands/…`)
   — no extra secret configuration needed. The pull secret is automatically applied.

---

## Cleanup

After all tests, the install was restored to baseline:
- All DB-backed warm configs deleted
- Test runtime sessions stopped
- Only `v1_current` (source=file) remains
- 3 v1_current warm pods Running (unchanged from pre-test)
