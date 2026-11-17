/*
 * OpenHands Enterprise Docker Compose architecture diagram. Styles live in /style.css under `.oh-arch`.
 *
 * Adapted from the Langfuse self-hosting architecture diagram
 * (https://github.com/langfuse/langfuse-docs, components/SelfHostingArchitecture.tsx and
 * components/SelfHostingArchitecture.module.css), used under the MIT License:
 *
 *   MIT License
 *
 *   Copyright (c) 2022-2025 Langfuse GmbH
 *
 *   Permission is hereby granted, free of charge, to any person obtaining a copy
 *   of this software and associated documentation files (the "Software"), to deal
 *   in the Software without restriction, including without limitation the rights
 *   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 *   copies of the Software, and to permit persons to whom the Software is
 *   furnished to do so, subject to the following conditions:
 *
 *   The above copyright notice and this permission notice shall be included in all
 *   copies or substantial portions of the Software.
 *
 *   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 *   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 *   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 *   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 *   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 *   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 *   SOFTWARE.
 *
 * Icon paths are from Lucide (https://github.com/lucide-icons/lucide), used under the
 * ISC License:
 *
 *   ISC License
 *
 *   Copyright (c) 2026 Lucide Icons and Contributors
 *
 *   Permission to use, copy, modify, and/or distribute this software for any
 *   purpose with or without fee is hereby granted, provided that the above
 *   copyright notice and this permission notice appear in all copies.
 *
 *   THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
 *   WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
 *   MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
 *   ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
 *   WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
 *   ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
 *   OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
 *
 * The `database` and `server` icons are derived from Feather
 * (https://github.com/feathericons/feather), used under the MIT License:
 *
 *   The MIT License (MIT)
 *
 *   Copyright (c) 2013-present Cole Bemis
 *
 *   Permission is hereby granted, free of charge, to any person obtaining a copy
 *   of this software and associated documentation files (the "Software"), to deal
 *   in the Software without restriction, including without limitation the rights
 *   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 *   copies of the Software, and to permit persons to whom the Software is
 *   furnished to do so, subject to the following conditions:
 *
 *   The above copyright notice and this permission notice shall be included in all
 *   copies or substantial portions of the Software.
 *
 *   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 *   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 *   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 *   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 *   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 *   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 *   SOFTWARE.
 */
export const ComposeArchitecture = () => {
  const icons = {
    globe: (
      <>
        <circle cx="12" cy="12" r="10" />
        <path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20" />
        <path d="M2 12h20" />
      </>
    ),
    route: (
      <>
        <circle cx="6" cy="19" r="3" />
        <path d="M9 19h8.5a3.5 3.5 0 0 0 0-7h-11a3.5 3.5 0 0 1 0-7H15" />
        <circle cx="18" cy="5" r="3" />
      </>
    ),
    server: (
      <>
        <rect width="20" height="8" x="2" y="2" rx="2" ry="2" />
        <rect width="20" height="8" x="2" y="14" rx="2" ry="2" />
        <path d="M6 6h.01" />
        <path d="M6 18h.01" />
      </>
    ),
    blocks: (
      <>
        <rect width="7" height="7" x="14" y="3" rx="1" />
        <path d="M10 21V8a1 1 0 0 0-1-1H4a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-5a1 1 0 0 0-1-1H3" />
      </>
    ),
    clock: (
      <>
        <circle cx="12" cy="12" r="10" />
        <path d="M12 6v6l4 2" />
      </>
    ),
    panels: (
      <>
        <rect width="18" height="18" x="3" y="3" rx="2" />
        <path d="M3 9h18" />
        <path d="M9 21V9" />
      </>
    ),
    database: (
      <>
        <ellipse cx="12" cy="5" rx="9" ry="3" />
        <path d="M3 5V19A9 3 0 0 0 21 19V5" />
        <path d="M3 12A9 3 0 0 0 21 12" />
      </>
    ),
    listOrdered: (
      <>
        <path d="M10 12h11" />
        <path d="M10 18h11" />
        <path d="M10 6h11" />
        <path d="M4 10h2" />
        <path d="M4 6h1v4" />
        <path d="M6 18H4c0-1 2-2 2-3s-1-1.5-2-1" />
      </>
    ),
    box: (
      <>
        <path d="M21 8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16Z" />
        <path d="m3.3 7 8.7 5 8.7-5" />
        <path d="M12 22V12" />
      </>
    ),
    lock: (
      <>
        <circle cx="12" cy="16" r="1" />
        <rect x="3" y="10" width="18" height="12" rx="2" />
        <path d="M7 10V7a5 5 0 0 1 10 0v3" />
      </>
    ),
    sparkles: (
      <>
        <path d="M9.937 15.5A2 2 0 0 0 8.5 14.063l-6.135-1.582a.5.5 0 0 1 0-.962L8.5 9.936A2 2 0 0 0 9.937 8.5l1.582-6.135a.5.5 0 0 1 .963 0L14.063 8.5A2 2 0 0 0 15.5 9.937l6.135 1.581a.5.5 0 0 1 0 .964L15.5 14.063a2 2 0 0 0-1.437 1.437l-1.582 6.135a.5.5 0 0 1-.963 0z" />
        <path d="M20 3v4" />
        <path d="M22 5h-4" />
      </>
    ),
    git: (
      <>
        <path d="M6 3v12" />
        <circle cx="18" cy="6" r="3" />
        <circle cx="6" cy="18" r="3" />
        <path d="M18 9a9 9 0 0 1-9 9" />
      </>
    ),
  };

  const Icon = ({ name, x, y, size = 20 }) => (
    <svg
      x={x}
      y={y}
      width={size}
      height={size}
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="1.5"
      strokeLinecap="round"
      strokeLinejoin="round"
      className="oh-arch-icon"
      aria-hidden="true"
    >
      {icons[name]}
    </svg>
  );

  const Service = ({ x, y, width = 160, name, detail, icon, href, accent, stacked }) => (
    <a href={href} className="oh-arch-service" aria-label={`${name}: ${detail}. View details.`}>
      <g transform={`translate(${x} ${y})`}>
        {stacked && <rect x="12" y="12" width={width} height="80" rx="8" className="oh-arch-card" />}
        {stacked && <rect x="6" y="6" width={width} height="80" rx="8" className="oh-arch-card" />}
        <rect width={width} height="80" rx="8" className="oh-arch-card" />
        {accent && (
          // A 4px band along the top edge, trimmed by the card's 8px corner radius.
          <path
            d={`M 1.07 4 A 8 8 0 0 1 8 0 H ${width - 8} A 8 8 0 0 1 ${width - 1.07} 4 Z`}
            className="oh-arch-accent"
          />
        )}
        <Icon name={icon} x={16} y={18} />
        <text x="46" y="33" className="oh-arch-name">
          {name}
        </text>
        <text x="16" y="59" className="oh-arch-detail">
          {detail}
        </text>
      </g>
    </a>
  );

  return (
    <figure className="not-prose oh-arch" aria-label="OpenHands Enterprise Docker Compose architecture">
      <div className="oh-arch-header">
        <span className="oh-arch-eyebrow">Docker Compose architecture</span>
      </div>
      <div className="oh-arch-scroll" tabIndex={0} role="region" aria-label="Architecture diagram">
        <svg viewBox="0 0 800 744" className="oh-arch-diagram" role="group">
          <desc>
            Users connect to the proxy, which routes requests to the sandboxes, the OpenHands app,
            the automation service, and Agent Canvas. The app starts sandboxes and connects to Redis
            and PostgreSQL. The automation service calls the app and connects to PostgreSQL. The
            worker connects to PostgreSQL and Redis. Sandboxes connect to your LLM provider and your
            source control. Everything except the LLM provider and source control runs on one Docker
            host.
          </desc>

          <rect x="20" y="104" width="760" height="488" rx="12" className="oh-arch-boundary" />
          <Icon name="lock" x={40} y={124} size={14} />
          <text x="62" y="136" className="oh-arch-label">
            DOCKER HOST
          </text>
          <text x="758" y="136" textAnchor="end" className="oh-arch-detail">
            One Compose network
          </text>

          <g transform="translate(300 24)">
            <rect width="200" height="54" rx="8" className="oh-arch-card" />
            <Icon name="globe" x={16} y={17} />
            <text x="46" y="33" className="oh-arch-name">
              Users
            </text>
          </g>

          <g className="oh-arch-app-paths">
            <path d="M 400 78 V 164" />
            <path d="m 396 158 4 6 4 -6" />
            <path d="M 400 244 V 272" />
            <path d="M 114 300 V 284 Q 114 272 126 272 H 666 Q 678 272 678 284 V 300" />
            <path d="M 306 272 V 300" />
            <path d="M 492 272 V 300" />
            <path d="m 110 294 4 6 4 -6" />
            <path d="m 302 294 4 6 4 -6" />
            <path d="m 488 294 4 6 4 -6" />
            <path d="m 674 294 4 6 4 -6" />
          </g>
          <text x="414" y="126" className="oh-arch-detail">
            HTTP
          </text>

          <g className="oh-arch-worker-paths">
            <path d="M 222 340 H 200" />
            <path d="m 206 336 -6 4 6 4" />
            <path d="M 412 340 H 392" />
            <path d="m 398 336 -6 4 6 4" />
            <path d="M 306 380 V 440" />
            <path d="m 302 434 4 6 4 -6" />
            <path d="M 346 380 C 346 410 452 410 452 440" />
            <path d="m 448 434 4 6 4 -6" />
            <path d="M 492 380 V 440" />
            <path d="m 488 434 4 6 4 -6" />
            <path d="M 598 480 H 572" />
            <path d="m 578 476 -6 4 6 4" />
            <path d="M 678 520 V 548 Q 678 556 670 556 H 314 Q 306 556 306 548 V 520" />
            <path d="m 302 526 4 -6 4 6" />
          </g>

          <Service x={300} y={164} width={200} name="Proxy" detail="Caddy, routes by path" icon="route" href="#proxy" />
          <Service x={40} y={300} width={148} name="Sandboxes" detail="Run the agent" icon="box" href="#sandboxes" stacked />
          <Service x={222} y={300} width={170} name="OpenHands App" detail="UI and API server" icon="server" href="#app" accent />
          <Service x={412} y={300} name="Automation" detail="Scheduled runs" icon="clock" href="#automation-server" accent />
          <Service x={598} y={300} name="Agent Canvas" detail="Static frontend" icon="panels" href="#canvas-server" accent />
          <Service x={226} y={440} name="Redis" detail="Cache" icon="listOrdered" href="#redis" />
          <Service x={412} y={440} name="PostgreSQL" detail="Application data" icon="database" href="#db" />
          <Service x={598} y={440} name="Worker" detail="Background jobs" icon="blocks" href="#worker" accent />

          <g className="oh-arch-external-paths">
            <path d="M 120 392 V 640" />
            <path d="M 120 608 H 388 Q 400 608 400 620 V 640" />
          </g>
          <g className="oh-arch-arrows">
            <path d="m 116 634 4 6 4 -6" />
            <path d="m 396 634 4 6 4 -6" />
          </g>

          <Service x={40} y={640} width={200} name="LLM provider" detail="Bring your own" icon="sparkles" href="#external-connections" />
          <Service x={300} y={640} width={200} name="Source control" detail="GitHub, GitLab, and more" icon="git" href="#external-connections" />
        </svg>
      </div>
      <figcaption className="oh-arch-caption">
        <div className="oh-arch-legend">
          <span>
            <i className="oh-arch-key-app" />
            Inbound requests
          </span>
          <span>
            <i className="oh-arch-key-worker" />
            Internal connections
          </span>
          <span>
            <i className="oh-arch-key-external" />
            External services
          </span>
        </div>
        <p>Each box inside the Docker host is one container. Select a component to read about it.</p>
      </figcaption>
    </figure>
  );
};
