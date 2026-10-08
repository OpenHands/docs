(function () {
  var PRODUCTION_HOST = 'docs.openhands.dev';
  var SETUP_PATH = '/openhands/usage/agent-canvas/setup';
  var LINKEDIN_PARTNER_ID = '10045108';
  var LINKEDIN_CONVERSION_ID = 29318740;
  var initialized = false;

  function isSetupPage() {
    return (
      window.location.hostname === PRODUCTION_HOST &&
      window.location.pathname.replace(/\/+$/, '') === SETUP_PATH
    );
  }

  function initializeLinkedIn() {
    if (initialized) return;
    initialized = true;

    window._linkedin_data_partner_ids = window._linkedin_data_partner_ids || [];
    if (window._linkedin_data_partner_ids.indexOf(LINKEDIN_PARTNER_ID) === -1) {
      window._linkedin_data_partner_ids.push(LINKEDIN_PARTNER_ID);
    }

    if (!window.lintrk) {
      window.lintrk = function (action, payload) {
        window.lintrk.q.push([action, payload]);
      };
      window.lintrk.q = [];
    }

    if (!document.querySelector('script[src="https://snap.licdn.com/li.lms-analytics/insight.min.js"]')) {
      var script = document.createElement('script');
      script.async = true;
      script.src = 'https://snap.licdn.com/li.lms-analytics/insight.min.js';
      document.head.appendChild(script);
    }
  }

  document.addEventListener('click', function (event) {
    if (!isSetupPage() || !(event.target instanceof Element)) return;

    var copyButton = event.target.closest(
      'button[data-testid="copy-code-button"], button[aria-label^="Copy"]',
    );
    if (!copyButton) return;

    initializeLinkedIn();
    window.lintrk('track', { conversion_id: LINKEDIN_CONVERSION_ID });
  });

  if (isSetupPage()) initializeLinkedIn();
})();
