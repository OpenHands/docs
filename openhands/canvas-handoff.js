(function () {
  const APP_HOST = "app.all-hands.dev";
  const APP_PREVIEW_HOST = "pr-1175.staging.all-hands.dev";
  const HANDOFF_PARAM = "oh_ph_handoff";
  const HANDOFF_TTL_MS = 5 * 60 * 1000;
  const ATTRIBUTION_KEYS = [
    "utm_source",
    "utm_medium",
    "utm_campaign",
    "landing_page_category",
    "cta_id",
    "cta_surface",
    "referring_domain_category",
  ];

  function cleanValue(value) {
    if (typeof value !== "string") return undefined;
    const trimmed = value.trim().toLowerCase().replace(/[^a-z0-9_:-]+/g, "_");
    return trimmed ? trimmed.slice(0, 80) : undefined;
  }

  function isDoNotTrackEnabled() {
    return navigator.doNotTrack === "1" || window.doNotTrack === "1";
  }

  function isProductionDocsHost(hostname) {
    const normalized = hostname.toLowerCase().replace(/^www\./, "");
    return normalized === "docs.openhands.dev";
  }

  function getAppTargetOrigin() {
    if (isProductionDocsHost(window.location.hostname)) return `https://${APP_HOST}`;
    return `https://${APP_PREVIEW_HOST}`;
  }

  function getPostHog() {
    const posthog = window.posthog;
    if (!posthog || isDoNotTrackEnabled()) return undefined;

    try {
      if (posthog.has_opted_out_capturing?.() === true) return undefined;
    } catch {
      return undefined;
    }

    return posthog;
  }

  function getSessionId(posthog) {
    try {
      return posthog.get_session_id?.() || posthog.get_property?.("$session_id");
    } catch {
      return undefined;
    }
  }

  function randomNonce() {
    const bytes = new Uint8Array(16);
    if (window.crypto?.getRandomValues) {
      window.crypto.getRandomValues(bytes);
    } else {
      for (let i = 0; i < bytes.length; i += 1) {
        bytes[i] = Math.floor(Math.random() * 256);
      }
    }
    return Array.from(bytes, (byte) => byte.toString(16).padStart(2, "0")).join("");
  }

  function base64UrlEncode(value) {
    const encoded = btoa(
      encodeURIComponent(value).replace(/%([0-9A-F]{2})/g, (_, hex) =>
        String.fromCharCode(Number.parseInt(hex, 16)),
      ),
    );
    return encoded.replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/g, "");
  }

  function landingPageCategory() {
    const path = window.location.pathname;
    if (path === "/" || path.startsWith("/overview")) return "docs_overview";
    if (path.startsWith("/sdk")) return "docs_sdk";
    if (path.startsWith("/openhands/usage/cloud")) return "docs_cloud";
    if (path.startsWith("/openhands/usage/agent-canvas")) return "docs_agent_canvas";
    if (path.startsWith("/openhands/usage/cli")) return "docs_cli";
    if (path.startsWith("/enterprise")) return "docs_enterprise";
    return "docs_other";
  }

  function targetCategory(url) {
    if (url.pathname === "/canvas" || url.pathname.startsWith("/canvas/")) return "canvas";
    if (url.pathname === "/" || url.pathname === "") return "cloud_home";
    if (url.pathname.startsWith("/settings/api-keys")) return "settings_api_keys";
    if (url.pathname.startsWith("/settings/billing")) return "settings_billing";
    if (url.pathname.startsWith("/settings/integrations")) return "settings_integrations";
    if (url.pathname.startsWith("/launch")) return "plugin_launch";
    return "cloud_app";
  }

  function referringDomainCategory() {
    if (!document.referrer) return "direct";
    try {
      const host = new URL(document.referrer).hostname.replace(/^www\./, "");
      if (host === window.location.hostname.replace(/^www\./, "")) return "internal";
      if (host.endsWith("google.com") || host.endsWith("bing.com") || host.endsWith("duckduckgo.com")) return "search";
      if (host.endsWith("github.com")) return "developer_community";
      if (host.endsWith("linkedin.com") || host.endsWith("x.com") || host.endsWith("twitter.com")) return "social";
      return "external";
    } catch {
      return "unknown";
    }
  }

  function buildAttribution(url) {
    const params = new URLSearchParams(window.location.search);
    const attribution = {
      landing_page_category: landingPageCategory(),
      cta_id: targetCategory(url),
      cta_surface: "docs_link",
      referring_domain_category: referringDomainCategory(),
    };

    for (const key of ["utm_source", "utm_medium", "utm_campaign"]) {
      const value = cleanValue(params.get(key));
      if (value) attribution[key] = value;
    }

    return attribution;
  }

  function buildHandoffUrl(href) {
    const url = new URL(href, window.location.href);
    if (url.hostname !== APP_HOST && url.hostname !== APP_PREVIEW_HOST) return href;

    const targetOrigin = new URL(getAppTargetOrigin());
    url.protocol = targetOrigin.protocol;
    url.host = targetOrigin.host;

    const posthog = getPostHog();
    if (!posthog) return url.toString();

    const distinctId = posthog.get_distinct_id?.();
    const sessionId = getSessionId(posthog);
    if (!distinctId || !sessionId) return url.toString();

    const payload = {
      v: 1,
      exp: Date.now() + HANDOFF_TTL_MS,
      nonce: randomNonce(),
      distinct_id: String(distinctId).slice(0, 256),
      session_id: String(sessionId).slice(0, 256),
      attribution: buildAttribution(url),
    };

    const sanitizedAttribution = {};
    for (const key of ATTRIBUTION_KEYS) {
      if (payload.attribution[key]) sanitizedAttribution[key] = payload.attribution[key];
    }
    payload.attribution = sanitizedAttribution;

    const hash = new URLSearchParams(url.hash.slice(1));
    hash.set(HANDOFF_PARAM, base64UrlEncode(JSON.stringify(payload)));
    url.hash = hash.toString();
    return url.toString();
  }

  document.addEventListener(
    "click",
    (event) => {
      const anchor = event.target instanceof Element ? event.target.closest("a[href]") : null;
      if (!anchor) return;

      try {
        anchor.href = buildHandoffUrl(anchor.href);
      } catch {
        // Attribution must never interfere with navigation.
      }
    },
    { capture: true },
  );
})();
