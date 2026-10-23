const assert = require('node:assert/strict');
const { readFileSync } = require('node:fs');
const { test } = require('node:test');
const vm = require('node:vm');

const script = readFileSync(require.resolve('../openhands/canvas-handoff.js'), 'utf8');

function handoff(initialUrl, targetUrl, analyticsEnabled = true) {
  let onClick;
  const storage = new Map();
  const posthog = {
    get_distinct_id: () => 'anon-123',
    get_session_id: () => 'session-456',
    has_opted_out_capturing: () => false,
  };
  const location = new URL(initialUrl);
  const context = {
    URL,
    URLSearchParams,
    Uint8Array,
    btoa,
    Date,
    navigator: { doNotTrack: '0' },
    window: { location, posthog: analyticsEnabled ? posthog : undefined, crypto: globalThis.crypto },
    document: {
      referrer: '',
      addEventListener: (_name, listener) => { onClick = listener; },
    },
    sessionStorage: {
      getItem: (key) => storage.get(key) ?? null,
      setItem: (key, value) => storage.set(key, value),
      removeItem: (key) => storage.delete(key),
    },
  };
  class Anchor {
    constructor(href) { this.href = href; }
    closest() { return this; }
  }
  context.Element = Anchor;
  vm.runInNewContext(script, context);
  location.href = 'https://docs.openhands.dev/sdk';
  const anchor = new Anchor(targetUrl);
  onClick({ target: anchor });
  if (!analyticsEnabled) return anchor.href;
  const encoded = new URLSearchParams(new URL(anchor.href).hash.slice(1)).get('oh_ph_handoff');
  assert.equal(new URL(anchor.href).searchParams.get('signup_entry_source'), 'docs');
  assert.ok(encoded);
  return JSON.parse(Buffer.from(encoded, 'base64url').toString());
}

test('docs entry survives site navigation and includes its campaign', () => {
  const payload = handoff(
    'https://docs.openhands.dev/overview?utm_source=newsletter&utm_campaign=fall',
    'https://app.all-hands.dev/',
  );
  assert.equal(payload.signup_entry_source, 'docs');
  assert.equal(payload.attribution.utm_source, 'newsletter');
  assert.equal(payload.attribution.utm_campaign, 'fall');
  assert.equal(payload.attribution.landing_page_category, 'docs_sdk');
});

test('docs origin survives without collecting analytics identifiers', () => {
  const url = handoff(
    'https://docs.openhands.dev/sdk',
    'https://app.all-hands.dev/',
    false,
  );
  assert.equal(new URL(url).searchParams.get('signup_entry_source'), 'docs');
  assert.equal(new URL(url).searchParams.has('oh_ph_handoff'), false);
});
