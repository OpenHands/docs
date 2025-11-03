---
title: openhands.sdk.security.analyzer
description: API reference for openhands.sdk.security.analyzer
---

# openhands.sdk.security.analyzer module

<a id="module-openhands.sdk.security.analyzer"></a>

### class openhands.sdk.security.analyzer.SecurityAnalyzerBase(, kind: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['LLMSecurityAnalyzer'] = 'LLMSecurityAnalyzer')

Bases: [`DiscriminatedUnionMixin`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.models.md#openhands.sdk.utils.models.DiscriminatedUnionMixin), [`ABC`](https://docs.python.org/3/library/abc.html#abc.ABC)

Abstract base class for security analyzers.

Security analyzers evaluate the risk of actions before they are executed
and can influence the conversation flow based on security policies.

This is adapted from OpenHands SecurityAnalyzer but designed to work
with the agent-sdk’s conversation-based architecture.

#### abstractmethod security_risk(action: [ActionEvent](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.action.md#openhands.sdk.event.llm_convertible.action.ActionEvent)) → [SecurityRisk](https://github.com/OpenHands/software-agent-sdk/sdk.security.risk.md#openhands.sdk.security.risk.SecurityRisk)

Evaluate the security risk of an ActionEvent.

This is the core method that analyzes an ActionEvent and returns its risk level.
Implementations should examine the action’s content, context, and potential
impact to determine the appropriate risk level.

Parameters:
  action – The ActionEvent to analyze for security risks
Returns:
  ActionSecurityRisk enum indicating the risk level

#### analyze_event(event: [Event](https://github.com/OpenHands/software-agent-sdk/sdk.event.base.md#openhands.sdk.event.base.Event)) → [SecurityRisk](https://github.com/OpenHands/software-agent-sdk/sdk.security.risk.md#openhands.sdk.security.risk.SecurityRisk) | [None](https://docs.python.org/3/library/constants.html#None)

Analyze an event for security risks.

This is a convenience method that checks if the event is an action
and calls security_risk() if it is. Non-action events return None.

Parameters:
  event – The event to analyze
Returns:
  ActionSecurityRisk if event is an action, None otherwise

#### should_require_confirmation(risk: [SecurityRisk](https://github.com/OpenHands/software-agent-sdk/sdk.security.risk.md#openhands.sdk.security.risk.SecurityRisk), confirmation_mode: [bool](https://docs.python.org/3/library/functions.html#bool) = False) → [bool](https://docs.python.org/3/library/functions.html#bool)

Determine if an action should require user confirmation.

This implements the default confirmation logic based on risk level
and confirmation mode settings.

Parameters:
  * risk – The security risk level of the action
  * confirmation_mode – Whether confirmation mode is enabled
Returns:
  True if confirmation is required, False otherwise

#### analyze_pending_actions(pending_actions: [list](https://docs.python.org/3/library/stdtypes.html#list)[[ActionEvent](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.action.md#openhands.sdk.event.llm_convertible.action.ActionEvent)]) → [list](https://docs.python.org/3/library/stdtypes.html#list)[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[ActionEvent](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.action.md#openhands.sdk.event.llm_convertible.action.ActionEvent), [SecurityRisk](https://github.com/OpenHands/software-agent-sdk/sdk.security.risk.md#openhands.sdk.security.risk.SecurityRisk)]]

Analyze all pending actions in a conversation.

This method gets all unmatched actions from the conversation state
and analyzes each one for security risks.

Parameters:
  conversation – The conversation to analyze
Returns:
  List of tuples containing (action, risk_level) for each pending action

#### model_config  : ClassVar[ConfigDict] = \{\}

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].
