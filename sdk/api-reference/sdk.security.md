---
title: openhands.sdk.security
description: API reference for openhands.sdk.security
---

# openhands.sdk.security package

<a id="module-openhands.sdk.security"></a>

### *class* openhands.sdk.security.SecurityRisk(\*values)

Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

Security risk levels for actions.

Based on OpenHands security risk levels but adapted for agent-sdk.
Integer values allow for easy comparison and ordering.

#### property description : [str](https://docs.python.org/3/library/stdtypes.html#str)

Get a human-readable description of the risk level.

#### get_color() → [str](https://docs.python.org/3/library/stdtypes.html#str)

Get the color for displaying this risk level in Rich text.

#### property visualize : Text

Return Rich Text representation of this risk level.

#### is_riskier(other: [SecurityRisk](https://github.com/OpenHands/software-agent-sdk/sdk.security.risk.md#openhands.sdk.security.risk.SecurityRisk), reflexive: [bool](https://docs.python.org/3/library/functions.html#bool) = True) → [bool](https://docs.python.org/3/library/functions.html#bool)

Check if this risk level is riskier than another.

Risk levels follow the natural ordering: LOW is less risky than MEDIUM, which is
less risky than HIGH. UNKNOWN is not comparable to any other level.

To make this act like a standard well-ordered domain, we reflexively consider
risk levels to be riskier than themselves. That is:

> for risk_level in list(SecurityRisk):
> : assert risk_level.is_riskier(risk_level)

> # More concretely:
> assert SecurityRisk.HIGH.is_riskier(SecurityRisk.HIGH)
> assert SecurityRisk.MEDIUM.is_riskier(SecurityRisk.MEDIUM)
> assert SecurityRisk.LOW.is_riskier(SecurityRisk.LOW)

This can be disabled by setting the reflexive parameter to False.

Parameters:
  * other ([*SecurityRisk*](#openhands.sdk.security.SecurityRisk)) – The other risk level to compare against.
  * reflexive ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – Whether the relationship is reflexive.
Raises:
  [ValueError](https://docs.python.org/3/library/exceptions.html#ValueError) – If either risk level is UNKNOWN.

#### UNKNOWN *= 'UNKNOWN'*

#### LOW *= 'LOW'*

#### MEDIUM *= 'MEDIUM'*

#### HIGH *= 'HIGH'*

## Submodules

* [openhands.sdk.security.analyzer module](https://github.com/OpenHands/software-agent-sdk/sdk.security.analyzer.md)
  * [`SecurityAnalyzerBase`](https://github.com/OpenHands/software-agent-sdk/sdk.security.analyzer.md#openhands.sdk.security.analyzer.SecurityAnalyzerBase)
    * [`SecurityAnalyzerBase.security_risk()`](https://github.com/OpenHands/software-agent-sdk/sdk.security.analyzer.md#openhands.sdk.security.analyzer.SecurityAnalyzerBase.security_risk)
    * [`SecurityAnalyzerBase.analyze_event()`](https://github.com/OpenHands/software-agent-sdk/sdk.security.analyzer.md#openhands.sdk.security.analyzer.SecurityAnalyzerBase.analyze_event)
    * [`SecurityAnalyzerBase.should_require_confirmation()`](https://github.com/OpenHands/software-agent-sdk/sdk.security.analyzer.md#openhands.sdk.security.analyzer.SecurityAnalyzerBase.should_require_confirmation)
    * [`SecurityAnalyzerBase.analyze_pending_actions()`](https://github.com/OpenHands/software-agent-sdk/sdk.security.analyzer.md#openhands.sdk.security.analyzer.SecurityAnalyzerBase.analyze_pending_actions)
    * [`SecurityAnalyzerBase.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.security.analyzer.md#openhands.sdk.security.analyzer.SecurityAnalyzerBase.model_config)
* [openhands.sdk.security.confirmation_policy module](https://github.com/OpenHands/software-agent-sdk/sdk.security.confirmation_policy.md)
  * [`ConfirmationPolicyBase`](https://github.com/OpenHands/software-agent-sdk/sdk.security.confirmation_policy.md#openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase)
    * [`ConfirmationPolicyBase.should_confirm()`](https://github.com/OpenHands/software-agent-sdk/sdk.security.confirmation_policy.md#openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase.should_confirm)
    * [`ConfirmationPolicyBase.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.security.confirmation_policy.md#openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase.model_config)
  * [`AlwaysConfirm`](https://github.com/OpenHands/software-agent-sdk/sdk.security.confirmation_policy.md#openhands.sdk.security.confirmation_policy.AlwaysConfirm)
    * [`AlwaysConfirm.should_confirm()`](https://github.com/OpenHands/software-agent-sdk/sdk.security.confirmation_policy.md#openhands.sdk.security.confirmation_policy.AlwaysConfirm.should_confirm)
    * [`AlwaysConfirm.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.security.confirmation_policy.md#openhands.sdk.security.confirmation_policy.AlwaysConfirm.model_config)
    * [`AlwaysConfirm.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.security.confirmation_policy.md#openhands.sdk.security.confirmation_policy.AlwaysConfirm.kind)
  * [`NeverConfirm`](https://github.com/OpenHands/software-agent-sdk/sdk.security.confirmation_policy.md#openhands.sdk.security.confirmation_policy.NeverConfirm)
    * [`NeverConfirm.should_confirm()`](https://github.com/OpenHands/software-agent-sdk/sdk.security.confirmation_policy.md#openhands.sdk.security.confirmation_policy.NeverConfirm.should_confirm)
    * [`NeverConfirm.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.security.confirmation_policy.md#openhands.sdk.security.confirmation_policy.NeverConfirm.model_config)
    * [`NeverConfirm.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.security.confirmation_policy.md#openhands.sdk.security.confirmation_policy.NeverConfirm.kind)
  * [`ConfirmRisky`](https://github.com/OpenHands/software-agent-sdk/sdk.security.confirmation_policy.md#openhands.sdk.security.confirmation_policy.ConfirmRisky)
    * [`ConfirmRisky.threshold`](https://github.com/OpenHands/software-agent-sdk/sdk.security.confirmation_policy.md#openhands.sdk.security.confirmation_policy.ConfirmRisky.threshold)
    * [`ConfirmRisky.confirm_unknown`](https://github.com/OpenHands/software-agent-sdk/sdk.security.confirmation_policy.md#openhands.sdk.security.confirmation_policy.ConfirmRisky.confirm_unknown)
    * [`ConfirmRisky.validate_threshold()`](https://github.com/OpenHands/software-agent-sdk/sdk.security.confirmation_policy.md#openhands.sdk.security.confirmation_policy.ConfirmRisky.validate_threshold)
    * [`ConfirmRisky.should_confirm()`](https://github.com/OpenHands/software-agent-sdk/sdk.security.confirmation_policy.md#openhands.sdk.security.confirmation_policy.ConfirmRisky.should_confirm)
    * [`ConfirmRisky.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.security.confirmation_policy.md#openhands.sdk.security.confirmation_policy.ConfirmRisky.model_config)
    * [`ConfirmRisky.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.security.confirmation_policy.md#openhands.sdk.security.confirmation_policy.ConfirmRisky.kind)
* [openhands.sdk.security.llm_analyzer module](https://github.com/OpenHands/software-agent-sdk/sdk.security.llm_analyzer.md)
  * [`LLMSecurityAnalyzer`](https://github.com/OpenHands/software-agent-sdk/sdk.security.llm_analyzer.md#openhands.sdk.security.llm_analyzer.LLMSecurityAnalyzer)
    * [`LLMSecurityAnalyzer.security_risk()`](https://github.com/OpenHands/software-agent-sdk/sdk.security.llm_analyzer.md#openhands.sdk.security.llm_analyzer.LLMSecurityAnalyzer.security_risk)
    * [`LLMSecurityAnalyzer.model_config`](https://github.com/OpenHands/software-agent-sdk/sdk.security.llm_analyzer.md#openhands.sdk.security.llm_analyzer.LLMSecurityAnalyzer.model_config)
    * [`LLMSecurityAnalyzer.kind`](https://github.com/OpenHands/software-agent-sdk/sdk.security.llm_analyzer.md#openhands.sdk.security.llm_analyzer.LLMSecurityAnalyzer.kind)
* [openhands.sdk.security.risk module](https://github.com/OpenHands/software-agent-sdk/sdk.security.risk.md)
  * [`SecurityRisk`](https://github.com/OpenHands/software-agent-sdk/sdk.security.risk.md#openhands.sdk.security.risk.SecurityRisk)
    * [`SecurityRisk.UNKNOWN`](https://github.com/OpenHands/software-agent-sdk/sdk.security.risk.md#openhands.sdk.security.risk.SecurityRisk.UNKNOWN)
    * [`SecurityRisk.LOW`](https://github.com/OpenHands/software-agent-sdk/sdk.security.risk.md#openhands.sdk.security.risk.SecurityRisk.LOW)
    * [`SecurityRisk.MEDIUM`](https://github.com/OpenHands/software-agent-sdk/sdk.security.risk.md#openhands.sdk.security.risk.SecurityRisk.MEDIUM)
    * [`SecurityRisk.HIGH`](https://github.com/OpenHands/software-agent-sdk/sdk.security.risk.md#openhands.sdk.security.risk.SecurityRisk.HIGH)
    * [`SecurityRisk.description`](https://github.com/OpenHands/software-agent-sdk/sdk.security.risk.md#openhands.sdk.security.risk.SecurityRisk.description)
    * [`SecurityRisk.get_color()`](https://github.com/OpenHands/software-agent-sdk/sdk.security.risk.md#openhands.sdk.security.risk.SecurityRisk.get_color)
    * [`SecurityRisk.visualize`](https://github.com/OpenHands/software-agent-sdk/sdk.security.risk.md#openhands.sdk.security.risk.SecurityRisk.visualize)
    * [`SecurityRisk.is_riskier()`](https://github.com/OpenHands/software-agent-sdk/sdk.security.risk.md#openhands.sdk.security.risk.SecurityRisk.is_riskier)
