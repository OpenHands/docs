## `openhands.sdk.security`

**Modules:**

- [**analyzer**](#openhands.sdk.security.analyzer) –
- [**confirmation_policy**](#openhands.sdk.security.confirmation_policy) –
- [**llm_analyzer**](#openhands.sdk.security.llm_analyzer) –
- [**risk**](#openhands.sdk.security.risk) –

**Classes:**

- [**SecurityRisk**](#openhands.sdk.security.SecurityRisk) – Security risk levels for actions.

### `openhands.sdk.security.SecurityRisk`

Bases: <code>[str](#str)</code>, <code>[Enum](#enum.Enum)</code>

Security risk levels for actions.

Based on OpenHands security risk levels but adapted for agent-sdk.
Integer values allow for easy comparison and ordering.

**Functions:**

- [**get_color**](#openhands.sdk.security.SecurityRisk.get_color) – Get the color for displaying this risk level in Rich text.
- [**is_riskier**](#openhands.sdk.security.SecurityRisk.is_riskier) – Check if this risk level is riskier than another.

**Attributes:**

- [**HIGH**](#openhands.sdk.security.SecurityRisk.HIGH) –
- [**LOW**](#openhands.sdk.security.SecurityRisk.LOW) –
- [**MEDIUM**](#openhands.sdk.security.SecurityRisk.MEDIUM) –
- [**UNKNOWN**](#openhands.sdk.security.SecurityRisk.UNKNOWN) –
- [**description**](#openhands.sdk.security.SecurityRisk.description) (<code>[str](#str)</code>) – Get a human-readable description of the risk level.
- [**visualize**](#openhands.sdk.security.SecurityRisk.visualize) (<code>[Text](#rich.text.Text)</code>) – Return Rich Text representation of this risk level.

#### `openhands.sdk.security.SecurityRisk.HIGH`

```python
HIGH = 'HIGH'
```

#### `openhands.sdk.security.SecurityRisk.LOW`

```python
LOW = 'LOW'
```

#### `openhands.sdk.security.SecurityRisk.MEDIUM`

```python
MEDIUM = 'MEDIUM'
```

#### `openhands.sdk.security.SecurityRisk.UNKNOWN`

```python
UNKNOWN = 'UNKNOWN'
```

#### `openhands.sdk.security.SecurityRisk.description`

```python
description: str
```

Get a human-readable description of the risk level.

#### `openhands.sdk.security.SecurityRisk.get_color`

```python
get_color()
```

Get the color for displaying this risk level in Rich text.

#### `openhands.sdk.security.SecurityRisk.is_riskier`

```python
is_riskier(other, reflexive=True)
```

Check if this risk level is riskier than another.

Risk levels follow the natural ordering: LOW is less risky than MEDIUM, which is
less risky than HIGH. UNKNOWN is not comparable to any other level.

To make this act like a standard well-ordered domain, we reflexively consider
risk levels to be riskier than themselves. That is:

```
for risk_level in list(SecurityRisk):
    assert risk_level.is_riskier(risk_level)

# More concretely:
assert SecurityRisk.HIGH.is_riskier(SecurityRisk.HIGH)
assert SecurityRisk.MEDIUM.is_riskier(SecurityRisk.MEDIUM)
assert SecurityRisk.LOW.is_riskier(SecurityRisk.LOW)
```

This can be disabled by setting the `reflexive` parameter to False.

**Parameters:**

- **other** (<code>[SecurityRisk](#openhands.sdk.security.risk.SecurityRisk)</code>) – The other risk level to compare against.
- **reflexive** (<code>[bool](#bool)</code>) – Whether the relationship is reflexive.

**Raises:**

- <code>[ValueError](#ValueError)</code> – If either risk level is UNKNOWN.

#### `openhands.sdk.security.SecurityRisk.visualize`

```python
visualize: Text
```

Return Rich Text representation of this risk level.

### `openhands.sdk.security.analyzer`

**Classes:**

- [**SecurityAnalyzerBase**](#openhands.sdk.security.analyzer.SecurityAnalyzerBase) – Abstract base class for security analyzers.

**Attributes:**

- [**logger**](#openhands.sdk.security.analyzer.logger) –

#### `openhands.sdk.security.analyzer.SecurityAnalyzerBase`

Bases: <code>[DiscriminatedUnionMixin](#openhands.sdk.utils.models.DiscriminatedUnionMixin)</code>, <code>[ABC](#abc.ABC)</code>

Abstract base class for security analyzers.

Security analyzers evaluate the risk of actions before they are executed
and can influence the conversation flow based on security policies.

This is adapted from OpenHands SecurityAnalyzer but designed to work
with the agent-sdk's conversation-based architecture.

**Functions:**

- [**analyze_event**](#openhands.sdk.security.analyzer.SecurityAnalyzerBase.analyze_event) – Analyze an event for security risks.
- [**analyze_pending_actions**](#openhands.sdk.security.analyzer.SecurityAnalyzerBase.analyze_pending_actions) – Analyze all pending actions in a conversation.
- [**get_serializable_type**](#openhands.sdk.security.analyzer.SecurityAnalyzerBase.get_serializable_type) – Custom method to get the union of all currently loaded
- [**model_dump_json**](#openhands.sdk.security.analyzer.SecurityAnalyzerBase.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.security.analyzer.SecurityAnalyzerBase.model_json_schema) –
- [**model_post_init**](#openhands.sdk.security.analyzer.SecurityAnalyzerBase.model_post_init) –
- [**model_rebuild**](#openhands.sdk.security.analyzer.SecurityAnalyzerBase.model_rebuild) –
- [**model_validate**](#openhands.sdk.security.analyzer.SecurityAnalyzerBase.model_validate) –
- [**model_validate_json**](#openhands.sdk.security.analyzer.SecurityAnalyzerBase.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.security.analyzer.SecurityAnalyzerBase.resolve_kind) –
- [**security_risk**](#openhands.sdk.security.analyzer.SecurityAnalyzerBase.security_risk) – Evaluate the security risk of an ActionEvent.
- [**should_require_confirmation**](#openhands.sdk.security.analyzer.SecurityAnalyzerBase.should_require_confirmation) – Determine if an action should require user confirmation.

**Attributes:**

- [**kind**](#openhands.sdk.security.analyzer.SecurityAnalyzerBase.kind) (<code>[str](#str)</code>) –

##### `openhands.sdk.security.analyzer.SecurityAnalyzerBase.analyze_event`

```python
analyze_event(event)
```

Analyze an event for security risks.

This is a convenience method that checks if the event is an action
and calls security_risk() if it is. Non-action events return None.

**Parameters:**

- **event** (<code>[Event](#openhands.sdk.event.base.Event)</code>) – The event to analyze

**Returns:**

- <code>[SecurityRisk](#openhands.sdk.security.risk.SecurityRisk) | None</code> – ActionSecurityRisk if event is an action, None otherwise

##### `openhands.sdk.security.analyzer.SecurityAnalyzerBase.analyze_pending_actions`

```python
analyze_pending_actions(pending_actions)
```

Analyze all pending actions in a conversation.

This method gets all unmatched actions from the conversation state
and analyzes each one for security risks.

**Parameters:**

- **conversation** – The conversation to analyze

**Returns:**

- <code>[list](#list)\[[tuple](#tuple)\[[ActionEvent](#openhands.sdk.event.llm_convertible.ActionEvent), [SecurityRisk](#openhands.sdk.security.risk.SecurityRisk)\]\]</code> – List of tuples containing (action, risk_level) for each pending action

##### `openhands.sdk.security.analyzer.SecurityAnalyzerBase.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

##### `openhands.sdk.security.analyzer.SecurityAnalyzerBase.kind`

```python
kind: str = Field(default='')
```

##### `openhands.sdk.security.analyzer.SecurityAnalyzerBase.model_dump_json`

```python
model_dump_json(**kwargs)
```

##### `openhands.sdk.security.analyzer.SecurityAnalyzerBase.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

##### `openhands.sdk.security.analyzer.SecurityAnalyzerBase.model_post_init`

```python
model_post_init(_context)
```

##### `openhands.sdk.security.analyzer.SecurityAnalyzerBase.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

##### `openhands.sdk.security.analyzer.SecurityAnalyzerBase.model_validate`

```python
model_validate(obj, **kwargs)
```

##### `openhands.sdk.security.analyzer.SecurityAnalyzerBase.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

##### `openhands.sdk.security.analyzer.SecurityAnalyzerBase.resolve_kind`

```python
resolve_kind(kind)
```

##### `openhands.sdk.security.analyzer.SecurityAnalyzerBase.security_risk`

```python
security_risk(action)
```

Evaluate the security risk of an ActionEvent.

This is the core method that analyzes an ActionEvent and returns its risk level.
Implementations should examine the action's content, context, and potential
impact to determine the appropriate risk level.

**Parameters:**

- **action** (<code>[ActionEvent](#openhands.sdk.event.llm_convertible.ActionEvent)</code>) – The ActionEvent to analyze for security risks

**Returns:**

- <code>[SecurityRisk](#openhands.sdk.security.risk.SecurityRisk)</code> – ActionSecurityRisk enum indicating the risk level

##### `openhands.sdk.security.analyzer.SecurityAnalyzerBase.should_require_confirmation`

```python
should_require_confirmation(risk, confirmation_mode=False)
```

Determine if an action should require user confirmation.

This implements the default confirmation logic based on risk level
and confirmation mode settings.

**Parameters:**

- **risk** (<code>[SecurityRisk](#openhands.sdk.security.risk.SecurityRisk)</code>) – The security risk level of the action
- **confirmation_mode** (<code>[bool](#bool)</code>) – Whether confirmation mode is enabled

**Returns:**

- <code>[bool](#bool)</code> – True if confirmation is required, False otherwise

#### `openhands.sdk.security.analyzer.logger`

```python
logger = get_logger(__name__)
```

### `openhands.sdk.security.confirmation_policy`

**Classes:**

- [**AlwaysConfirm**](#openhands.sdk.security.confirmation_policy.AlwaysConfirm) –
- [**ConfirmRisky**](#openhands.sdk.security.confirmation_policy.ConfirmRisky) –
- [**ConfirmationPolicyBase**](#openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase) –
- [**NeverConfirm**](#openhands.sdk.security.confirmation_policy.NeverConfirm) –

#### `openhands.sdk.security.confirmation_policy.AlwaysConfirm`

Bases: <code>[ConfirmationPolicyBase](#openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase)</code>

**Functions:**

- [**get_serializable_type**](#openhands.sdk.security.confirmation_policy.AlwaysConfirm.get_serializable_type) – Custom method to get the union of all currently loaded
- [**model_dump_json**](#openhands.sdk.security.confirmation_policy.AlwaysConfirm.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.security.confirmation_policy.AlwaysConfirm.model_json_schema) –
- [**model_post_init**](#openhands.sdk.security.confirmation_policy.AlwaysConfirm.model_post_init) –
- [**model_rebuild**](#openhands.sdk.security.confirmation_policy.AlwaysConfirm.model_rebuild) –
- [**model_validate**](#openhands.sdk.security.confirmation_policy.AlwaysConfirm.model_validate) –
- [**model_validate_json**](#openhands.sdk.security.confirmation_policy.AlwaysConfirm.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.security.confirmation_policy.AlwaysConfirm.resolve_kind) –
- [**should_confirm**](#openhands.sdk.security.confirmation_policy.AlwaysConfirm.should_confirm) –

**Attributes:**

- [**kind**](#openhands.sdk.security.confirmation_policy.AlwaysConfirm.kind) (<code>[str](#str)</code>) –

##### `openhands.sdk.security.confirmation_policy.AlwaysConfirm.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

##### `openhands.sdk.security.confirmation_policy.AlwaysConfirm.kind`

```python
kind: str = Field(default='')
```

##### `openhands.sdk.security.confirmation_policy.AlwaysConfirm.model_dump_json`

```python
model_dump_json(**kwargs)
```

##### `openhands.sdk.security.confirmation_policy.AlwaysConfirm.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

##### `openhands.sdk.security.confirmation_policy.AlwaysConfirm.model_post_init`

```python
model_post_init(_context)
```

##### `openhands.sdk.security.confirmation_policy.AlwaysConfirm.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

##### `openhands.sdk.security.confirmation_policy.AlwaysConfirm.model_validate`

```python
model_validate(obj, **kwargs)
```

##### `openhands.sdk.security.confirmation_policy.AlwaysConfirm.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

##### `openhands.sdk.security.confirmation_policy.AlwaysConfirm.resolve_kind`

```python
resolve_kind(kind)
```

##### `openhands.sdk.security.confirmation_policy.AlwaysConfirm.should_confirm`

```python
should_confirm(risk=SecurityRisk.UNKNOWN)
```

#### `openhands.sdk.security.confirmation_policy.ConfirmRisky`

Bases: <code>[ConfirmationPolicyBase](#openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase)</code>

**Functions:**

- [**get_serializable_type**](#openhands.sdk.security.confirmation_policy.ConfirmRisky.get_serializable_type) – Custom method to get the union of all currently loaded
- [**model_dump_json**](#openhands.sdk.security.confirmation_policy.ConfirmRisky.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.security.confirmation_policy.ConfirmRisky.model_json_schema) –
- [**model_post_init**](#openhands.sdk.security.confirmation_policy.ConfirmRisky.model_post_init) –
- [**model_rebuild**](#openhands.sdk.security.confirmation_policy.ConfirmRisky.model_rebuild) –
- [**model_validate**](#openhands.sdk.security.confirmation_policy.ConfirmRisky.model_validate) –
- [**model_validate_json**](#openhands.sdk.security.confirmation_policy.ConfirmRisky.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.security.confirmation_policy.ConfirmRisky.resolve_kind) –
- [**should_confirm**](#openhands.sdk.security.confirmation_policy.ConfirmRisky.should_confirm) –
- [**validate_threshold**](#openhands.sdk.security.confirmation_policy.ConfirmRisky.validate_threshold) –

**Attributes:**

- [**confirm_unknown**](#openhands.sdk.security.confirmation_policy.ConfirmRisky.confirm_unknown) (<code>[bool](#bool)</code>) –
- [**kind**](#openhands.sdk.security.confirmation_policy.ConfirmRisky.kind) (<code>[str](#str)</code>) –
- [**threshold**](#openhands.sdk.security.confirmation_policy.ConfirmRisky.threshold) (<code>[SecurityRisk](#openhands.sdk.security.risk.SecurityRisk)</code>) –

##### `openhands.sdk.security.confirmation_policy.ConfirmRisky.confirm_unknown`

```python
confirm_unknown: bool = True
```

##### `openhands.sdk.security.confirmation_policy.ConfirmRisky.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

##### `openhands.sdk.security.confirmation_policy.ConfirmRisky.kind`

```python
kind: str = Field(default='')
```

##### `openhands.sdk.security.confirmation_policy.ConfirmRisky.model_dump_json`

```python
model_dump_json(**kwargs)
```

##### `openhands.sdk.security.confirmation_policy.ConfirmRisky.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

##### `openhands.sdk.security.confirmation_policy.ConfirmRisky.model_post_init`

```python
model_post_init(_context)
```

##### `openhands.sdk.security.confirmation_policy.ConfirmRisky.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

##### `openhands.sdk.security.confirmation_policy.ConfirmRisky.model_validate`

```python
model_validate(obj, **kwargs)
```

##### `openhands.sdk.security.confirmation_policy.ConfirmRisky.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

##### `openhands.sdk.security.confirmation_policy.ConfirmRisky.resolve_kind`

```python
resolve_kind(kind)
```

##### `openhands.sdk.security.confirmation_policy.ConfirmRisky.should_confirm`

```python
should_confirm(risk=SecurityRisk.UNKNOWN)
```

##### `openhands.sdk.security.confirmation_policy.ConfirmRisky.threshold`

```python
threshold: SecurityRisk = SecurityRisk.HIGH
```

##### `openhands.sdk.security.confirmation_policy.ConfirmRisky.validate_threshold`

```python
validate_threshold(v)
```

#### `openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase`

Bases: <code>[DiscriminatedUnionMixin](#openhands.sdk.utils.models.DiscriminatedUnionMixin)</code>, <code>[ABC](#abc.ABC)</code>

**Functions:**

- [**get_serializable_type**](#openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase.get_serializable_type) – Custom method to get the union of all currently loaded
- [**model_dump_json**](#openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase.model_json_schema) –
- [**model_post_init**](#openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase.model_post_init) –
- [**model_rebuild**](#openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase.model_rebuild) –
- [**model_validate**](#openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase.model_validate) –
- [**model_validate_json**](#openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase.resolve_kind) –
- [**should_confirm**](#openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase.should_confirm) – Determine if an action with the given risk level requires confirmation.

**Attributes:**

- [**kind**](#openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase.kind) (<code>[str](#str)</code>) –

##### `openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

##### `openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase.kind`

```python
kind: str = Field(default='')
```

##### `openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase.model_dump_json`

```python
model_dump_json(**kwargs)
```

##### `openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

##### `openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase.model_post_init`

```python
model_post_init(_context)
```

##### `openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

##### `openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase.model_validate`

```python
model_validate(obj, **kwargs)
```

##### `openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

##### `openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase.resolve_kind`

```python
resolve_kind(kind)
```

##### `openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase.should_confirm`

```python
should_confirm(risk=SecurityRisk.UNKNOWN)
```

Determine if an action with the given risk level requires confirmation.

This method defines the core logic for determining whether user confirmation
is required before executing an action based on its security risk level.

**Parameters:**

- **risk** (<code>[SecurityRisk](#openhands.sdk.security.risk.SecurityRisk)</code>) – The security risk level of the action to be evaluated.
  Defaults to SecurityRisk.UNKNOWN if not specified.

**Returns:**

- <code>[bool](#bool)</code> – True if the action requires user confirmation before execution,
- <code>[bool](#bool)</code> – False if the action can proceed without confirmation.

#### `openhands.sdk.security.confirmation_policy.NeverConfirm`

Bases: <code>[ConfirmationPolicyBase](#openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase)</code>

**Functions:**

- [**get_serializable_type**](#openhands.sdk.security.confirmation_policy.NeverConfirm.get_serializable_type) – Custom method to get the union of all currently loaded
- [**model_dump_json**](#openhands.sdk.security.confirmation_policy.NeverConfirm.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.security.confirmation_policy.NeverConfirm.model_json_schema) –
- [**model_post_init**](#openhands.sdk.security.confirmation_policy.NeverConfirm.model_post_init) –
- [**model_rebuild**](#openhands.sdk.security.confirmation_policy.NeverConfirm.model_rebuild) –
- [**model_validate**](#openhands.sdk.security.confirmation_policy.NeverConfirm.model_validate) –
- [**model_validate_json**](#openhands.sdk.security.confirmation_policy.NeverConfirm.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.security.confirmation_policy.NeverConfirm.resolve_kind) –
- [**should_confirm**](#openhands.sdk.security.confirmation_policy.NeverConfirm.should_confirm) –

**Attributes:**

- [**kind**](#openhands.sdk.security.confirmation_policy.NeverConfirm.kind) (<code>[str](#str)</code>) –

##### `openhands.sdk.security.confirmation_policy.NeverConfirm.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

##### `openhands.sdk.security.confirmation_policy.NeverConfirm.kind`

```python
kind: str = Field(default='')
```

##### `openhands.sdk.security.confirmation_policy.NeverConfirm.model_dump_json`

```python
model_dump_json(**kwargs)
```

##### `openhands.sdk.security.confirmation_policy.NeverConfirm.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

##### `openhands.sdk.security.confirmation_policy.NeverConfirm.model_post_init`

```python
model_post_init(_context)
```

##### `openhands.sdk.security.confirmation_policy.NeverConfirm.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

##### `openhands.sdk.security.confirmation_policy.NeverConfirm.model_validate`

```python
model_validate(obj, **kwargs)
```

##### `openhands.sdk.security.confirmation_policy.NeverConfirm.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

##### `openhands.sdk.security.confirmation_policy.NeverConfirm.resolve_kind`

```python
resolve_kind(kind)
```

##### `openhands.sdk.security.confirmation_policy.NeverConfirm.should_confirm`

```python
should_confirm(risk=SecurityRisk.UNKNOWN)
```

### `openhands.sdk.security.llm_analyzer`

**Classes:**

- [**LLMSecurityAnalyzer**](#openhands.sdk.security.llm_analyzer.LLMSecurityAnalyzer) – LLM-based security analyzer.

**Attributes:**

- [**logger**](#openhands.sdk.security.llm_analyzer.logger) –

#### `openhands.sdk.security.llm_analyzer.LLMSecurityAnalyzer`

Bases: <code>[SecurityAnalyzerBase](#openhands.sdk.security.analyzer.SecurityAnalyzerBase)</code>

LLM-based security analyzer.

This analyzer respects the security_risk attribute that can be set by the LLM
when generating actions, similar to OpenHands' LLMRiskAnalyzer.

It provides a lightweight security analysis approach that leverages the LLM's
understanding of action context and potential risks.

**Functions:**

- [**analyze_event**](#openhands.sdk.security.llm_analyzer.LLMSecurityAnalyzer.analyze_event) – Analyze an event for security risks.
- [**analyze_pending_actions**](#openhands.sdk.security.llm_analyzer.LLMSecurityAnalyzer.analyze_pending_actions) – Analyze all pending actions in a conversation.
- [**get_serializable_type**](#openhands.sdk.security.llm_analyzer.LLMSecurityAnalyzer.get_serializable_type) – Custom method to get the union of all currently loaded
- [**model_dump_json**](#openhands.sdk.security.llm_analyzer.LLMSecurityAnalyzer.model_dump_json) –
- [**model_json_schema**](#openhands.sdk.security.llm_analyzer.LLMSecurityAnalyzer.model_json_schema) –
- [**model_post_init**](#openhands.sdk.security.llm_analyzer.LLMSecurityAnalyzer.model_post_init) –
- [**model_rebuild**](#openhands.sdk.security.llm_analyzer.LLMSecurityAnalyzer.model_rebuild) –
- [**model_validate**](#openhands.sdk.security.llm_analyzer.LLMSecurityAnalyzer.model_validate) –
- [**model_validate_json**](#openhands.sdk.security.llm_analyzer.LLMSecurityAnalyzer.model_validate_json) –
- [**resolve_kind**](#openhands.sdk.security.llm_analyzer.LLMSecurityAnalyzer.resolve_kind) –
- [**security_risk**](#openhands.sdk.security.llm_analyzer.LLMSecurityAnalyzer.security_risk) – Evaluate security risk based on LLM-provided assessment.
- [**should_require_confirmation**](#openhands.sdk.security.llm_analyzer.LLMSecurityAnalyzer.should_require_confirmation) – Determine if an action should require user confirmation.

**Attributes:**

- [**kind**](#openhands.sdk.security.llm_analyzer.LLMSecurityAnalyzer.kind) (<code>[str](#str)</code>) –

##### `openhands.sdk.security.llm_analyzer.LLMSecurityAnalyzer.analyze_event`

```python
analyze_event(event)
```

Analyze an event for security risks.

This is a convenience method that checks if the event is an action
and calls security_risk() if it is. Non-action events return None.

**Parameters:**

- **event** (<code>[Event](#openhands.sdk.event.base.Event)</code>) – The event to analyze

**Returns:**

- <code>[SecurityRisk](#openhands.sdk.security.risk.SecurityRisk) | None</code> – ActionSecurityRisk if event is an action, None otherwise

##### `openhands.sdk.security.llm_analyzer.LLMSecurityAnalyzer.analyze_pending_actions`

```python
analyze_pending_actions(pending_actions)
```

Analyze all pending actions in a conversation.

This method gets all unmatched actions from the conversation state
and analyzes each one for security risks.

**Parameters:**

- **conversation** – The conversation to analyze

**Returns:**

- <code>[list](#list)\[[tuple](#tuple)\[[ActionEvent](#openhands.sdk.event.llm_convertible.ActionEvent), [SecurityRisk](#openhands.sdk.security.risk.SecurityRisk)\]\]</code> – List of tuples containing (action, risk_level) for each pending action

##### `openhands.sdk.security.llm_analyzer.LLMSecurityAnalyzer.get_serializable_type`

```python
get_serializable_type()
```

Custom method to get the union of all currently loaded
non absract subclasses

##### `openhands.sdk.security.llm_analyzer.LLMSecurityAnalyzer.kind`

```python
kind: str = Field(default='')
```

##### `openhands.sdk.security.llm_analyzer.LLMSecurityAnalyzer.model_dump_json`

```python
model_dump_json(**kwargs)
```

##### `openhands.sdk.security.llm_analyzer.LLMSecurityAnalyzer.model_json_schema`

```python
model_json_schema(*args, **kwargs)
```

##### `openhands.sdk.security.llm_analyzer.LLMSecurityAnalyzer.model_post_init`

```python
model_post_init(_context)
```

##### `openhands.sdk.security.llm_analyzer.LLMSecurityAnalyzer.model_rebuild`

```python
model_rebuild(*, force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace=None)
```

##### `openhands.sdk.security.llm_analyzer.LLMSecurityAnalyzer.model_validate`

```python
model_validate(obj, **kwargs)
```

##### `openhands.sdk.security.llm_analyzer.LLMSecurityAnalyzer.model_validate_json`

```python
model_validate_json(json_data, **kwargs)
```

##### `openhands.sdk.security.llm_analyzer.LLMSecurityAnalyzer.resolve_kind`

```python
resolve_kind(kind)
```

##### `openhands.sdk.security.llm_analyzer.LLMSecurityAnalyzer.security_risk`

```python
security_risk(action)
```

Evaluate security risk based on LLM-provided assessment.

This method checks if the action has a security_risk attribute set by the LLM
and returns it. The LLM may not always provide this attribute but it defaults to
UNKNOWN if not explicitly set.

##### `openhands.sdk.security.llm_analyzer.LLMSecurityAnalyzer.should_require_confirmation`

```python
should_require_confirmation(risk, confirmation_mode=False)
```

Determine if an action should require user confirmation.

This implements the default confirmation logic based on risk level
and confirmation mode settings.

**Parameters:**

- **risk** (<code>[SecurityRisk](#openhands.sdk.security.risk.SecurityRisk)</code>) – The security risk level of the action
- **confirmation_mode** (<code>[bool](#bool)</code>) – Whether confirmation mode is enabled

**Returns:**

- <code>[bool](#bool)</code> – True if confirmation is required, False otherwise

#### `openhands.sdk.security.llm_analyzer.logger`

```python
logger = get_logger(__name__)
```

### `openhands.sdk.security.risk`

**Classes:**

- [**SecurityRisk**](#openhands.sdk.security.risk.SecurityRisk) – Security risk levels for actions.

#### `openhands.sdk.security.risk.SecurityRisk`

Bases: <code>[str](#str)</code>, <code>[Enum](#enum.Enum)</code>

Security risk levels for actions.

Based on OpenHands security risk levels but adapted for agent-sdk.
Integer values allow for easy comparison and ordering.

**Functions:**

- [**get_color**](#openhands.sdk.security.risk.SecurityRisk.get_color) – Get the color for displaying this risk level in Rich text.
- [**is_riskier**](#openhands.sdk.security.risk.SecurityRisk.is_riskier) – Check if this risk level is riskier than another.

**Attributes:**

- [**HIGH**](#openhands.sdk.security.risk.SecurityRisk.HIGH) –
- [**LOW**](#openhands.sdk.security.risk.SecurityRisk.LOW) –
- [**MEDIUM**](#openhands.sdk.security.risk.SecurityRisk.MEDIUM) –
- [**UNKNOWN**](#openhands.sdk.security.risk.SecurityRisk.UNKNOWN) –
- [**description**](#openhands.sdk.security.risk.SecurityRisk.description) (<code>[str](#str)</code>) – Get a human-readable description of the risk level.
- [**visualize**](#openhands.sdk.security.risk.SecurityRisk.visualize) (<code>[Text](#rich.text.Text)</code>) – Return Rich Text representation of this risk level.

##### `openhands.sdk.security.risk.SecurityRisk.HIGH`

```python
HIGH = 'HIGH'
```

##### `openhands.sdk.security.risk.SecurityRisk.LOW`

```python
LOW = 'LOW'
```

##### `openhands.sdk.security.risk.SecurityRisk.MEDIUM`

```python
MEDIUM = 'MEDIUM'
```

##### `openhands.sdk.security.risk.SecurityRisk.UNKNOWN`

```python
UNKNOWN = 'UNKNOWN'
```

##### `openhands.sdk.security.risk.SecurityRisk.description`

```python
description: str
```

Get a human-readable description of the risk level.

##### `openhands.sdk.security.risk.SecurityRisk.get_color`

```python
get_color()
```

Get the color for displaying this risk level in Rich text.

##### `openhands.sdk.security.risk.SecurityRisk.is_riskier`

```python
is_riskier(other, reflexive=True)
```

Check if this risk level is riskier than another.

Risk levels follow the natural ordering: LOW is less risky than MEDIUM, which is
less risky than HIGH. UNKNOWN is not comparable to any other level.

To make this act like a standard well-ordered domain, we reflexively consider
risk levels to be riskier than themselves. That is:

```
for risk_level in list(SecurityRisk):
    assert risk_level.is_riskier(risk_level)

# More concretely:
assert SecurityRisk.HIGH.is_riskier(SecurityRisk.HIGH)
assert SecurityRisk.MEDIUM.is_riskier(SecurityRisk.MEDIUM)
assert SecurityRisk.LOW.is_riskier(SecurityRisk.LOW)
```

This can be disabled by setting the `reflexive` parameter to False.

**Parameters:**

- **other** (<code>[SecurityRisk](#openhands.sdk.security.risk.SecurityRisk)</code>) – The other risk level to compare against.
- **reflexive** (<code>[bool](#bool)</code>) – Whether the relationship is reflexive.

**Raises:**

- <code>[ValueError](#ValueError)</code> – If either risk level is UNKNOWN.

##### `openhands.sdk.security.risk.SecurityRisk.visualize`

```python
visualize: Text
```

Return Rich Text representation of this risk level.
