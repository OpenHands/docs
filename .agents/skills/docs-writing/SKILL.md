---
name: docs-writing
description: >-
  Writing rules for pages on the OpenHands docs site. Use when writing, editing, or reviewing
  prose in .mdx pages: make the reader the actor, state limitations once, use few callouts, keep
  instructions and prerequisites short, keep sidebar labels to one line, and position OpenHands
  Enterprise deployment options correctly.
triggers:
  - /docs-writing
---

# Writing OpenHands Docs

Follow these rules when you write or edit pages on this site. For formatting conventions such as
header case, lists, code blocks, and links, follow `openhands/DOC_STYLE_GUIDE.md`.

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

## Inspire confidence

- State a limitation once, in plain inline text. Don't repeat a caveat across sections or pages.
  For example, don't put a "use Kubernetes for production" reminder in the intro, a callout, and a
  closing "Next steps" section on the same page.
- Use `<Note>`, `<Warning>`, and `<Info>` sparingly. Most information belongs in the body text.
  Reserve callouts for something the reader would otherwise get wrong.

## Keep instructions simple

- Prefer the shortest path that works. For the Docker Compose install, that is
  `git clone https://github.com/OpenHands/enterprise.git`, `cd enterprise`, and
  `docker compose up --wait`. Leave out version lookups, file downloads, and extra flags that add
  steps without adding value.
- Point readers at the product's own flows instead of describing every click. For example, "Open
  `http://localhost:9043` and follow the onboarding flow to create your first user and configure
  your LLM provider" beats deep links to sign-up URLs or instructions to open Settings.
- Keep prerequisite lists short. Name the tool or credential (Git, Docker and Docker Compose, an LLM
  API key) without explaining it.

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
