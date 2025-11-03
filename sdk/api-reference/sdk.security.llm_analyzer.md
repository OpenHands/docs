---
title: openhands.sdk.security.llm_analyzer
description: API reference for openhands.sdk.security.llm_analyzer
---

# openhands.sdk.security.llm_analyzer module

<a id="module-openhands.sdk.security.llm_analyzer"></a>

### class openhands.sdk.security.llm_analyzer.LLMSecurityAnalyzer(, kind: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['LLMSecurityAnalyzer'] = 'LLMSecurityAnalyzer')

Bases: [`SecurityAnalyzerBase`](https://github.com/OpenHands/software-agent-sdk/sdk.security.analyzer.md#openhands.sdk.security.analyzer.SecurityAnalyzerBase)

LLM-based security analyzer.

This analyzer respects the security_risk attribute that can be set by the LLM
when generating actions, similar to OpenHands’ LLMRiskAnalyzer.

It provides a lightweight security analysis approach that leverages the LLM’s
understanding of action context and potential risks.

#### security_risk(action: [ActionEvent](https://github.com/OpenHands/software-agent-sdk/sdk.event.llm_convertible.action.md#openhands.sdk.event.llm_convertible.action.ActionEvent)) → [SecurityRisk](https://github.com/OpenHands/software-agent-sdk/sdk.security.risk.md#openhands.sdk.security.risk.SecurityRisk)

Evaluate security risk based on LLM-provided assessment.

This method checks if the action has a security_risk attribute set by the LLM
and returns it. The LLM may not always provide this attribute but it defaults to
UNKNOWN if not explicitly set.

#### model_config  : ClassVar[ConfigDict] = \{\}

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### kind : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['LLMSecurityAnalyzer']
