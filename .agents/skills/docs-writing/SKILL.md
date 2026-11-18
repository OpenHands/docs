---
name: docs-writing
description: >-
  Writing rules for pages on the OpenHands docs site. Use when writing, editing, or reviewing prose
  in .mdx pages.
triggers:
  - /docs-writing
---

# Writing OpenHands Docs

Follow these rules when you write or edit pages on this site. The goal is a page the reader can act
on.

For formatting conventions such as header case, lists, code blocks, and links, follow
`openhands/DOC_STYLE_GUIDE.md`.

## Make the reader the actor

Write task-oriented sentences around what the reader does, not what a tool or product does. Put the
reader's action or goal first, usually as an imperative ("Use X to…", "Give X…", "Run X…"). Don't
make a tool or product the subject and leave the reader out, especially in intros and step
descriptions.

| Avoid | Prefer |
|-------|--------|
| ngrok gives the Docker Compose stack a public HTTPS URL. | Use ngrok to give the Docker Compose stack a public HTTPS URL. |
| The Docker Compose stack runs OpenHands Enterprise on a single machine. | Use Docker Compose to run OpenHands Enterprise on a single machine. |

Describing what a component is, for example on an architecture page, is fine with the component as
the subject. This rule applies when the sentence is about a task the reader performs.
Recommendations such as "We recommend using S3" are fine too.

## Lead with a recommendation

- When there are several ways to do something and one is better, recommend it ("We recommend X").
  Use `<Tabs>` when the reader's setup decides the choice, such as their OS or cloud provider.
- Lead with the recommendation and name the things involved.
  - Avoid: "OpenHands Enterprise runs two very different workloads: the application services and
    the agent sandboxes. To keep them apart, you can use separate node pools."
  - Prefer: "We recommend using two separate node pools: a general pool for the OpenHands
    application services and cluster add-ons, and a Sysbox pool for the agent sandboxes."

## State requirements without justifying them

State the requirement or the setting and stop. Don't add what breaks without it, and don't explain
why the default is wrong. The reader already knows that a pod without enough memory gets OOMKilled.

| Avoid | Prefer |
|-------|--------|
| Provision at least 3 GB of memory for X, or its pods will get OOMKilled. | X requires at least 3 GB of memory. |
| The default storage class (standard-rwo) is GKE-only. Set STORAGE_CLASS or sandboxes won't start. | Set `runtime-api.env.STORAGE_CLASS` to your `gp3` class. |
| The bundled MinIO is ephemeral; for production back it with an S3 bucket: | For production, we recommend using S3: |

Leave out background, rationale, and internal implementation details. Describe what the reader
needs to do.

## Limit caveats and callouts

- State a limitation once, in plain inline text. Don't repeat a caveat across sections or pages.
  For example, don't put a "use Kubernetes for production" reminder in the intro, a callout, and a
  closing "Next steps" section on the same page.
- Use `<Note>`, `<Warning>`, and `<Info>` sparingly. Most information belongs in the body text.
  Reserve callouts for something the reader would otherwise get wrong.

## Keep instructions simple

- Prefer the shortest path that works. For the Docker Compose install, that is
  `git clone https://github.com/OpenHands/enterprise.git`, `cd enterprise`, and
  `docker compose up --wait`. Leave out version lookups, file downloads, extra flags, and
  placeholder variables for values the reader doesn't need to choose, such as `VERSION=<latest>`.
- Point readers at the product's own flows and entry points instead of describing every click or
  linking to internal routes. For example, "Open `http://localhost:9043` and follow the onboarding
  flow to create your first user and configure your LLM provider" beats deep links to sign-up URLs
  or instructions to open Settings.
- Keep prerequisite lists short. Name the tool or credential (Git, Docker and Docker Compose, an LLM
  API key) without explaining it or adding sizing asides.
- Don't narrate what the product does next, such as "After you sign in, OpenHands opens Agent Canvas
  at…". A short check that tells the reader a step worked, such as "You should see the dashboard",
  is fine. Keep progress notes to one line, such as "On the first start, the application pulls
  images, which can take several minutes."

## Treat configurable values as examples

- Values the reader controls aren't fixed facts. Present defaults as examples, advise around the
  reader's chosen settings, and link to the page that documents the setting. For example: "Set
  per-sandbox CPU and memory on the Resource Limits page, then size nodes around the values you
  choose there."
- State the minimum versions OpenHands requires. Don't copy an upstream project's support window,
  because it falls out of date. Say "a currently supported version" and link to the upstream
  project's list instead.

## Leave out

- Don't list everything. Write "the application services" instead of naming every service, and
  give one example instead of a list of examples.
- Don't explain how the underlying platform works, such as Kubernetes, Docker, or containerd. Drop
  asides like "(request = limit, so it's guaranteed)". Our own components that readers may need to
  configure still get named. For example, the Docker Compose docs name Caddy because it serves HTTPS
  and readers customize it.
- In install and configuration guides, state infrastructure requirements in general terms, such as
  node pools, IAM permissions, and Helm values. Don't include Terraform or point at internal source
  code. Cloning a public repository is fine when it's the install method itself.

## Organize pages

- Put guidance that applies to every platform on its own page, so it extends to other platforms
  and distributions. Don't nest general topics, such as installing a container runtime or setting
  up DNS and TLS, under one provider's page.
- Platform-specific pages cover that platform's details and link to the general pages. A
  platform-specific callout inside a general page is fine, such as an "Amazon EKS" note, as long as
  the page itself stays general.
- Link to existing pages instead of repeating their content. This applies within a page too: don't
  add a `<CardGroup>` that repeats links already given in a table or sentence above it.
- Keep configuration reference on its own page. Don't grow a variables table inside an install
  guide.

## Write plain sentences

These are docs. Don't write them like a blog post or a story, and don't try to make sentences punchy
or memorable. Use simple, complete sentences with one idea each: a subject, a verb, and what the
reader needs to know.

- Avoid these patterns:
  - Fragments: "Standard EKS nodes on the Amazon Linux 2023 AMI; on-demand or Spot." Write "Use
    standard EKS nodes on the Amazon Linux 2023 AMI, with on-demand or Spot capacity."
  - Dramatic contrasts and reveals, such as "It's a gateway, not a proxy." or "The result: zero
    downtime."
  - Rhetorical questions, such as "Need more capacity? Add a node pool."
  - Long sentences that chain several clauses together. Split them into shorter sentences.
- Headings, table cells, and list items that name a thing, such as a prerequisites list, can be
  short phrases.
- Don't use em-dashes. Use a comma, period, parentheses, or a colon instead. For bold-lead list
  items, write `**Term**: description`.

## Keep sidebar labels short

Keep sidebar labels short enough to fit on one line. When a page title is long, add a
`sidebarTitle` to the frontmatter rather than shortening the page title. For example, "Running
Docker in the Agent Sandbox" uses `sidebarTitle: "Docker in the Sandbox"`. A label can rely on its
group for context, such as "Sysbox" in Kubernetes or "AWS" in VM Install.

## OpenHands Enterprise positioning

- Recommend Docker Compose for trials and proofs of concept, and Kubernetes (Helm) for production.
- Cover self-hosted options only. Don't offer OpenHands Cloud as a deployment option.
- The VM install is a last resort. Don't suggest or link to it as a deployment path in new content.
  Existing VM install pages stay in the navigation.
