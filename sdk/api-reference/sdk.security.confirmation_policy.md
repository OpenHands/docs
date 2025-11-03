---
title: openhands.sdk.security.confirmation_policy
description: API reference for openhands.sdk.security.confirmation_policy
---

# openhands.sdk.security.confirmation_policy module

<a id="module-openhands.sdk.security.confirmation_policy"></a>

### *class* openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase(, kind: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['AlwaysConfirm', 'ConfirmRisky', 'NeverConfirm'] = 'AlwaysConfirm')

Bases: [`DiscriminatedUnionMixin`](https://github.com/OpenHands/software-agent-sdk/sdk.utils.models.md#openhands.sdk.utils.models.DiscriminatedUnionMixin), [`ABC`](https://docs.python.org/3/library/abc.html#abc.ABC)

#### abstractmethod should_confirm(risk: [SecurityRisk](https://github.com/OpenHands/software-agent-sdk/sdk.security.risk.md#openhands.sdk.security.risk.SecurityRisk) = SecurityRisk.UNKNOWN) → [bool](https://docs.python.org/3/library/functions.html#bool)

Determine if an action with the given risk level requires confirmation.

This method defines the core logic for determining whether user confirmation
is required before executing an action based on its security risk level.

Parameters:
  risk – The security risk level of the action to be evaluated.
  Defaults to SecurityRisk.UNKNOWN if not specified.
Returns:
  True if the action requires user confirmation before execution,
  False if the action can proceed without confirmation.

#### model_config  : ClassVar[ConfigDict] = \{\}

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

### *class* openhands.sdk.security.confirmation_policy.AlwaysConfirm(, kind: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['AlwaysConfirm'] = 'AlwaysConfirm')

Bases: [`ConfirmationPolicyBase`](#openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase)

#### should_confirm(risk: [SecurityRisk](https://github.com/OpenHands/software-agent-sdk/sdk.security.risk.md#openhands.sdk.security.risk.SecurityRisk) = SecurityRisk.UNKNOWN) → [bool](https://docs.python.org/3/library/functions.html#bool)

Determine if an action with the given risk level requires confirmation.

This method defines the core logic for determining whether user confirmation
is required before executing an action based on its security risk level.

Parameters:
  risk – The security risk level of the action to be evaluated.
  Defaults to SecurityRisk.UNKNOWN if not specified.
Returns:
  True if the action requires user confirmation before execution,
  False if the action can proceed without confirmation.

#### model_config  : ClassVar[ConfigDict] = \{\}

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### kind : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['AlwaysConfirm']

### *class* openhands.sdk.security.confirmation_policy.NeverConfirm(, kind: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['NeverConfirm'] = 'NeverConfirm')

Bases: [`ConfirmationPolicyBase`](#openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase)

#### should_confirm(risk: [SecurityRisk](https://github.com/OpenHands/software-agent-sdk/sdk.security.risk.md#openhands.sdk.security.risk.SecurityRisk) = SecurityRisk.UNKNOWN) → [bool](https://docs.python.org/3/library/functions.html#bool)

Determine if an action with the given risk level requires confirmation.

This method defines the core logic for determining whether user confirmation
is required before executing an action based on its security risk level.

Parameters:
  risk – The security risk level of the action to be evaluated.
  Defaults to SecurityRisk.UNKNOWN if not specified.
Returns:
  True if the action requires user confirmation before execution,
  False if the action can proceed without confirmation.

#### model_config  : ClassVar[ConfigDict] = \{\}

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### kind : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['NeverConfirm']

### *class* openhands.sdk.security.confirmation_policy.ConfirmRisky(, kind: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['ConfirmRisky'] = 'ConfirmRisky', threshold: [SecurityRisk](https://github.com/OpenHands/software-agent-sdk/sdk.security.risk.md#openhands.sdk.security.risk.SecurityRisk) = SecurityRisk.HIGH, confirm_unknown: [bool](https://docs.python.org/3/library/functions.html#bool) = True)

Bases: [`ConfirmationPolicyBase`](#openhands.sdk.security.confirmation_policy.ConfirmationPolicyBase)

#### threshold : [SecurityRisk](https://github.com/OpenHands/software-agent-sdk/sdk.security.risk.md#openhands.sdk.security.risk.SecurityRisk)

#### confirm_unknown : [bool](https://docs.python.org/3/library/functions.html#bool)

#### classmethod validate_threshold(v: [SecurityRisk](https://github.com/OpenHands/software-agent-sdk/sdk.security.risk.md#openhands.sdk.security.risk.SecurityRisk)) → [SecurityRisk](https://github.com/OpenHands/software-agent-sdk/sdk.security.risk.md#openhands.sdk.security.risk.SecurityRisk)

#### should_confirm(risk: [SecurityRisk](https://github.com/OpenHands/software-agent-sdk/sdk.security.risk.md#openhands.sdk.security.risk.SecurityRisk) = SecurityRisk.UNKNOWN) → [bool](https://docs.python.org/3/library/functions.html#bool)

Determine if an action with the given risk level requires confirmation.

This method defines the core logic for determining whether user confirmation
is required before executing an action based on its security risk level.

Parameters:
  risk – The security risk level of the action to be evaluated.
  Defaults to SecurityRisk.UNKNOWN if not specified.
Returns:
  True if the action requires user confirmation before execution,
  False if the action can proceed without confirmation.

#### model_config  : ClassVar[ConfigDict] = \{\}

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].

#### kind : [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['ConfirmRisky']
