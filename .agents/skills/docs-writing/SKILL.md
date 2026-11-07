---
name: docs-writing
description: >-
  Writing rules for pages on the OpenHands docs site. Use when writing, editing, or reviewing
  prose in .mdx pages: make the reader the actor, lead with a clear recommendation, stay
  matter-of-fact, state limitations once, keep instructions short, treat configurable values as
  examples, link instead of duplicating, write plain complete sentences without em-dashes, keep
  sidebar labels to one line, and position OpenHands Enterprise deployment options correctly.
triggers:
  - /docs-writing
---

# Writing OpenHands Docs

Follow these rules when you write or edit pages on this site. The goal is a page the reader can act
on, with clear recommendations and no internal notes, background, or tour of how the technology
works. Keep pages as terse and plain as these rules are.

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

## Lead with a recommendation

- When there are several ways to do something, recommend one ("We recommend X"). Don't present a
  list of every possibility and leave the reader to choose.
- Lead with the recommendation and name the things involved.
  - Avoid: "OpenHands Enterprise runs two very different workloads, so…"
  - Prefer: "We recommend using two separate node pools: a general pool for the OpenHands
    application services and cluster add-ons, and a Sysbox pool for the agent sandboxes."
- Tell the reader what to set. Don't justify it by explaining why the default is wrong.
  - Avoid: "The default storage class (standard-rwo) is GKE-only. Set STORAGE_CLASS or sandboxes
    won't start."
  - Prefer: "Set `runtime-api.env.STORAGE_CLASS` to your `gp3` class."
- Give a recommendation rather than an explanation of the default.
  - Avoid: "The bundled MinIO is ephemeral; for production back it with an S3 bucket:"
  - Prefer: "For production, we recommend using S3:"

## Stay matter-of-fact

- State what to do and stop. Don't over-explain.
- Don't explain how the underlying platform works, such as Kubernetes, Docker, or containerd. Drop
  asides like "(request = limit, so it's guaranteed)".
- Do name our own components that readers may need to configure. For example, the Docker Compose
  docs name Caddy because it serves HTTPS and readers customize it.
- If something is required, state the requirement. Leave out warnings about what breaks otherwise,
  such as "or it will never start".

## Inspire confidence

- State a limitation once, in plain inline text. Don't repeat a caveat across sections or pages.
  For example, don't put a "use Kubernetes for production" reminder in the intro, a callout, and a
  closing "Next steps" section on the same page.
- Use `<Note>`, `<Warning>`, and `<Info>` sparingly. Most information belongs in the body text.
  Reserve callouts for something the reader would otherwise get wrong.

## Keep instructions simple

- Prefer the shortest path that works. For the Docker Compose install, that is
  `git clone https://github.com/OpenHands/enterprise.git`, `cd enterprise`, and
  `docker compose up --wait`. Leave out version lookups, placeholder variables, file downloads, and
  extra flags that add steps without adding value.
- Point readers at the product's own flows instead of describing every click. For example, "Open
  `http://localhost:9043` and follow the onboarding flow to create your first user and configure
  your LLM provider" beats deep links to sign-up URLs or instructions to open Settings.
- Link to the entry point. When the app redirects to the right place, give the base URL instead of
  an internal route.
- Keep prerequisite lists short. Name the tool or credential (Git, Docker and Docker Compose, an LLM
  API key) without explaining it or adding sizing asides.
- Don't narrate what happens next. Cut sentences like "After you sign in, OpenHands opens Agent
  Canvas at…". Keep progress notes to one line, such as "On the first start, the application pulls
  images, which can take several minutes."

## Treat configurable values as examples

- Values the reader controls aren't fixed facts. Present defaults as examples, advise around the
  reader's chosen settings, and link to the page that documents the setting. For example: "Set
  per-sandbox CPU and memory on the Resource Limits page, then size nodes around the values you
  choose there."
- Don't hardcode version ranges that will fall out of support. Say "a currently supported version"
  and link to the upstream project's supported-version list. Never recommend an unsupported
  version.

## Leave out

- Don't list everything. Write "the application services" instead of naming every service, and
  keep at most one example where a list of examples would do.
- Cut extended background, rationale, and internal implementation details.
- In install and configuration guides, state infrastructure requirements in general terms, such as
  node pools, IAM permissions, Helm values, and `kubectl` or `helm` commands. Don't include
  Terraform or point at internal source code. Cloning a public repository is fine when it's the
  install method itself.

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

- Write complete sentences. Avoid fragments and clever structure.
  - Avoid: "Standard EKS nodes on the Amazon Linux 2023 AMI; on-demand or Spot."
  - Prefer: "Use standard EKS nodes on the Amazon Linux 2023 AMI, with on-demand or Spot capacity."
- Don't use em-dashes. Use a comma, period, parentheses, or a colon instead. For bold-lead list
  items, write `**Term**: description`.
- When you model a page on another project's docs, borrow the structure and use our own words. A
  table column copied verbatim, such as "Responsibility", reads as copied when "Runs on" says the
  same thing.

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
