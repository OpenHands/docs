// Push copy-button clicks into the dataLayer for Google Tag Manager.
//
// Mintlify's GTM integration (integrations.gtm in docs.json) initializes the
// dataLayer and loads the container on every page. This script guarantees the
// dataLayer array exists even if the container hasn't loaded yet, and pushes a
// `copy_click` event on every copy-button click so the GTM container can track
// installation-command copies without extra DOM-scraping triggers.

(function () {
  function dataLayer() {
    window.dataLayer = window.dataLayer || [];
    return window.dataLayer;
  }

  function isCopyButton(target) {
    if (!(target instanceof Element)) return false;
    return Boolean(
      target.closest(
        'button[data-testid="copy-code-button"], button[aria-label^="Copy"], button[title="Copy"]',
      ),
    );
  }

  document.addEventListener('click', function (event) {
    if (!isCopyButton(event.target)) return;
    dataLayer().push({
      event: 'copy_click',
      page_path: window.location.pathname,
      page_title: document.title,
    });
  });
})();