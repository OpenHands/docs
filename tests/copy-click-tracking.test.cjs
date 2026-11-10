const assert = require('node:assert/strict');
const { readFileSync } = require('node:fs');
const { test } = require('node:test');
const vm = require('node:vm');

const script = readFileSync(
  require.resolve('../openhands/copy-click-tracking.js'),
  'utf8',
);

class Element {}

const COPY_SELECTOR =
  'button[data-testid="copy-code-button"], button[aria-label^="Copy"], button[title="Copy"]';

function copyButton() {
  return class extends Element {
    closest(sel) {
      return sel === COPY_SELECTOR ? this : null;
    }
  };
}

function nonCopyButton() {
  return class extends Element {
    closest() {
      return null;
    }
  };
}

const CopyButton = copyButton();
const NonCopyButton = nonCopyButton();

function setup({ withDataLayer = true } = {}) {
  let listener;
  const dataLayer = withDataLayer ? [] : undefined;
  const context = {
    window: {
      location: { pathname: '/openhands/usage/agent-canvas/setup' },
      document: { title: 'Agent Canvas Setup' },
      dataLayer,
    },
    document: {
      title: 'Agent Canvas Setup',
      addEventListener: (_name, l) => {
        listener = l;
      },
    },
    Element,
  };
  vm.runInNewContext(script, context);
  return {
    listener,
    clicked(target) {
      listener({ target });
      return context.window.dataLayer;
    },
  };
}

test('copy-button click pushes a copy_click event into the dataLayer', () => {
  const { listener, clicked } = setup();
  const dataLayer = clicked(new CopyButton());
  assert.equal(dataLayer.length, 1);
  assert.equal(dataLayer[0].event, 'copy_click');
  assert.equal(dataLayer[0].page_path, '/openhands/usage/agent-canvas/setup');
  assert.equal(dataLayer[0].page_title, 'Agent Canvas Setup');
  assert.ok(listener);
});

test('all copy-button selectors match the same event', () => {
  const { clicked } = setup();
  for (const _ of [0, 1, 2]) {
    clicked(new CopyButton());
  }
  const dataLayer = clicked(new CopyButton());
  assert.equal(dataLayer.length, 4);
  assert.ok(dataLayer.every((e) => e.event === 'copy_click'));
});

test('non-copy clicks do not touch the dataLayer', () => {
  const { clicked } = setup();
  const dataLayer = clicked(new NonCopyButton());
  assert.equal(dataLayer.length, 0);
});

test('dataLayer is created lazily when missing', () => {
  const { clicked } = setup({ withDataLayer: false });
  const dataLayer = clicked(new CopyButton());
  assert.ok(Array.isArray(dataLayer));
  assert.equal(dataLayer[0].event, 'copy_click');
});