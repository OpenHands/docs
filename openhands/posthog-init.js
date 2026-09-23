!function(t,e){var o,n,p,r;e.__SV||(window.posthog && window.posthog.__loaded)||(window.posthog=e,e._i=[],e.init=function(i,s,a){function g(t,e){var o=e.split(".");2==o.length&&(t=t[o[0]],e=o[1]),t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}(p=t.createElement("script")).type="text/javascript",p.crossOrigin="anonymous",p.async=!0,p.src=s.api_host.replace(".i.posthog.com","-assets.i.posthog.com")+"/static/array.js",(r=t.getElementsByTagName("script")[0]).parentNode.insertBefore(p,r);var u=e;for(void 0!==a?u=e[a]=[]:a="posthog",u.people=u.people||[],u.toString=function(t){var e="posthog";return"posthog"!==a&&(e+="."+a),t||(e+=" (stub)"),e},u.people.toString=function(){return u.toString(1)+".people (stub)"},o="init zr Wr fi Br Gr ci Nr Hr capture Ui calculateEventProperties Kr register register_once register_for_session unregister unregister_for_session Zr getFeatureFlag getFeatureFlagPayload isFeatureEnabled reloadFeatureFlags updateEarlyAccessFeatureEnrollment getEarlyAccessFeatures on onFeatureFlags onSurveysLoaded onSessionId getSurveys getActiveMatchingSurveys renderSurvey displaySurvey cancelPendingSurvey canRenderSurvey canRenderSurveyAsync identify setPersonProperties group resetGroups setPersonPropertiesForFlags resetPersonPropertiesForFlags setGroupPropertiesForFlags resetGroupPropertiesForFlags reset get_distinct_id getGroups get_session_id get_session_replay_url alias set_config startSessionRecording stopSessionRecording sessionRecordingStarted captureException loadToolbar get_property getSessionProperty Xr Jr createPersonProfile Qr jr ts opt_in_capturing opt_out_capturing has_opted_in_capturing has_opted_out_capturing get_explicit_consent_status is_capturing clear_opt_in_out_capturing Vr debug O Yr getPageViewId captureTraceFeedback captureTraceMetric Or".split(" "),n=0;n<o.length;n++)g(u,o[n]);e._i.push([i,s,a])},e.__SV=1)}(document,window.posthog||[]);

// PostHog initialization.
//
// Mintlify auto-includes every .js file in the content directory on every page,
// so this script runs on both the production custom domain and preview
// deployments with no per-environment env-var layer available. To keep preview
// traffic out of the production PostHog project, we select the project key at
// runtime based on the hostname:
//
//   - docs.openhands.dev          -> PROD_KEY (production custom domain)
//   - *.mintlify.site / .app      -> STAGING_KEY (PR preview deployments)
//   - localhost / 127.0.0.1       -> STAGING_KEY (local dev)
//
// The api_host / ui_host / defaults stay the same for both environments.
// Replace STAGING_KEY with the real staging PostHog project key before merging
// (or leave it as the placeholder to keep previews non-tracking until then).

var PROD_KEY = 'phc_BgzfxKdgsYMLFTmJqt424ZoyVHvKFfrwttLimzdYTKFK';
var STAGING_KEY = 'phc_REPLACE_WITH_STAGING_POSTHOG_KEY';

var POSTHOG_CONFIG = {
  api_host: 'https://z.openhands.dev',
  ui_host: 'https://us.posthog.com',
  defaults: '2025-11-30',
  person_profiles: 'always',
};

var PRODUCTION_HOSTNAMES = ['docs.openhands.dev'];

function isStagingHostname(hostname) {
  if (PRODUCTION_HOSTNAMES.indexOf(hostname) !== -1) return false;
  // Mintlify preview deployments are served from *.mintlify.site or *.mintlify.app.
  return (
    /\.mintlify\.site$/.test(hostname) ||
    /\.mintlify\.app$/.test(hostname) ||
    hostname === 'localhost' ||
    hostname === '127.0.0.1' ||
    hostname === '0.0.0.0'
  );
}

(function () {
  var hostname = (window.location && window.location.hostname) || '';
  var apiKey = isStagingHostname(hostname) ? STAGING_KEY : PROD_KEY;

  if (apiKey.indexOf('REPLACE_WITH_STAGING') !== -1 && isStagingHostname(hostname)) {
    if (window.console && console.warn) {
      console.warn('[analytics] Staging PostHog key is still a placeholder; preview analytics disabled until it is set.');
    }
    return;
  }

  posthog.init(apiKey, POSTHOG_CONFIG);
})();
