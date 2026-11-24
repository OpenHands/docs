/*
 * OpenHands Enterprise architecture diagram. Styles live in /style.css under `.oh-arch`.
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
export const EnterpriseArchitecture = () => {
  const icons = {
    globe: (
      <>
        <circle cx="12" cy="12" r="10" />
        <path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20" />
        <path d="M2 12h20" />
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
    database: (
      <>
        <ellipse cx="12" cy="5" rx="9" ry="3" />
        <path d="M3 5V19A9 3 0 0 0 21 19V5" />
        <path d="M3 12A9 3 0 0 0 21 12" />
      </>
    ),
    layers: (
      <>
        <path d="M12.83 2.18a2 2 0 0 0-1.66 0L2.6 6.08a1 1 0 0 0 0 1.83l8.58 3.91a2 2 0 0 0 1.66 0l8.58-3.9a1 1 0 0 0 0-1.83z" />
        <path d="M2 12a1 1 0 0 0 .58.91l8.6 3.91a2 2 0 0 0 1.65 0l8.58-3.9A1 1 0 0 0 22 12" />
        <path d="M2 17a1 1 0 0 0 .58.91l8.6 3.91a2 2 0 0 0 1.65 0l8.58-3.9A1 1 0 0 0 22 17" />
      </>
    ),
    box: (
      <>
        <path d="M21 8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16Z" />
        <path d="m3.3 7 8.7 5 8.7-5" />
        <path d="M12 22V12" />
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

  const Service = ({ x, y, width = 200, name, detail, icon, href, accent, stacked }) => (
    <a href={href} className="oh-arch-service" aria-label={`${name}: ${detail}. View documentation.`}>
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
    <figure className="not-prose oh-arch" aria-label="OpenHands Enterprise architecture">
      <div className="oh-arch-header">
        <span className="oh-arch-eyebrow">Deployment architecture</span>
      </div>
      <div className="oh-arch-scroll" tabIndex={0} role="region" aria-label="Architecture diagram">
        <svg viewBox="0 0 800 764" className="oh-arch-diagram" role="group">
          <desc>
            Users connect to the OpenHands app. The app connects to PostgreSQL, a Redis cache, and the
            sandbox provider, which starts sandboxes. The worker connects to the same three
            services. Sandboxes connect to your LLM provider and your source control. Everything
            except the LLM provider and source control runs in your infrastructure.
          </desc>

          <rect x="20" y="104" width="760" height="512" rx="12" className="oh-arch-boundary" />
          <Icon name="lock" x={300} y={124} size={14} />
          <text x="322" y="136" className="oh-arch-label">
            YOUR INFRASTRUCTURE
          </text>
          <text x="758" y="136" textAnchor="end" className="oh-arch-detail">
            Cloud / on-premises
          </text>

          <g transform="translate(40 24)">
            <rect width="200" height="54" rx="8" className="oh-arch-card" />
            <Icon name="globe" x={16} y={17} />
            <text x="46" y="33" className="oh-arch-name">
              Users
            </text>
          </g>

          <g className="oh-arch-app-paths">
            <path d="M 140 78 V 268" />
            <path d="m 136 262 4 6 4 -6" />
            <path d="M 240 284 C 270 284 270 204 300 204" />
            <path d="M 240 308 H 300" />
            <path d="M 240 332 C 270 332 270 412 300 412" />
            <path d="m 294 200 6 4 -6 4" />
            <path d="m 294 304 6 4 -6 4" />
            <path d="m 294 408 6 4 -6 4" />
          </g>
          <g className="oh-arch-worker-paths">
            <path d="M 560 284 C 530 284 530 204 500 204" />
            <path d="M 560 308 H 500" />
            <path d="M 560 332 C 530 332 530 412 500 412" />
            <path d="m 506 200 -6 4 6 4" />
            <path d="m 506 304 -6 4 6 4" />
            <path d="m 506 408 -6 4 6 4" />
          </g>
          <g className="oh-arch-app-paths">
            <path d="M 400 452 V 496" />
            <path d="m 396 490 4 6 4 -6" />
          </g>

          <text x="154" y="180" className="oh-arch-detail">
            Requests
          </text>
          <text x="660" y="242" textAnchor="middle" className="oh-arch-label">
            BACKGROUND PROCESSING
          </text>

          <Service
            x={40}
            y={268}
            name="OpenHands App"
            detail="UI & API server"
            icon="server"
            href="/enterprise/architecture"
            accent
          />
          <Service
            x={560}
            y={268}
            name="OpenHands Worker"
            detail="Background jobs"
            icon="blocks"
            href="/enterprise/architecture"
            accent
          />
          <Service
            x={300}
            y={164}
            name="PostgreSQL"
            detail="Application data"
            icon="database"
            href="/enterprise/external-postgres"
          />
          <Service
            x={300}
            y={268}
            name="Redis"
            detail="Cache"
            icon="listOrdered"
            href="/enterprise/architecture"
          />
          <Service
            x={300}
            y={372}
            name="Sandbox provider"
            detail="Starts and stops sandboxes"
            icon="layers"
            href="/enterprise/conversations-and-sandboxes"
          />
          <Service
            x={294}
            y={496}
            name="Sandboxes"
            detail="Where agents run code"
            icon="box"
            href="/enterprise/custom-sandbox-images/index"
            stacked
          />

          <g className="oh-arch-external-paths">
            <path d="M 294 536 H 246 Q 230 536 230 552 V 664" />
            <path d="M 506 536 H 554 Q 570 536 570 552 V 664" />
          </g>
          <g className="oh-arch-arrows">
            <path d="m 226 658 4 6 4 -6" />
            <path d="m 566 658 4 6 4 -6" />
          </g>

          <Service
            x={120}
            y={664}
            width={220}
            name="LLM provider"
            detail="Bring your own"
            icon="sparkles"
            href="/enterprise/integrations/external-llm-gateways"
          />
          <Service
            x={460}
            y={664}
            width={220}
            name="Source control"
            detail="GitHub, GitLab, and more"
            icon="git"
            href="/enterprise/integrations/overview"
          />
        </svg>
      </div>
      <figcaption className="oh-arch-caption">
        <div className="oh-arch-legend">
          <span>
            <i className="oh-arch-key-app" />
            App connections
          </span>
          <span>
            <i className="oh-arch-key-worker" />
            Worker connections
          </span>
          <span>
            <i className="oh-arch-key-external" />
            External services
          </span>
        </div>
        <p>Select a component to read its documentation.</p>
      </figcaption>
    </figure>
  );
};
