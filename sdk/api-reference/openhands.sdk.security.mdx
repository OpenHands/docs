---
title: openhands.sdk.security
description: API reference for openhands.sdk.security
---

# openhands.sdk.security module

### SecurityRisk

Bases: `str`, `Enum`

Security risk levels for actions.

Based on OpenHands security risk levels but adapted for agent-sdk.
Integer values allow for easy comparison and ordering.

#### HIGH = 'HIGH'

#### LOW = 'LOW'

#### MEDIUM = 'MEDIUM'

#### UNKNOWN = 'UNKNOWN'

#### property description : str

Get a human-readable description of the risk level.

#### get_color

Get the color for displaying this risk level in Rich text.

#### is_riskier

Check if this risk level is riskier than another.

Risk levels follow the natural ordering: LOW is less risky than MEDIUM, which is
less risky than HIGH. UNKNOWN is not comparable to any other level.

To make this act like a standard well-ordered domain, we reflexively consider
risk levels to be riskier than themselves. That is:

>` for risk_level in list(SecurityRisk):
>` : assert risk_level.is_riskier(risk_level)

>` # More concretely:
>` assert SecurityRisk.HIGH.is_riskier(SecurityRisk.HIGH)
>` assert SecurityRisk.MEDIUM.is_riskier(SecurityRisk.MEDIUM)
>` assert SecurityRisk.LOW.is_riskier(SecurityRisk.LOW)

This can be disabled by setting the reflexive parameter to False.

* Parameters:
   other ([SecurityRisk*](#openhands.sdk.security.SecurityRisk)) – The other risk level to compare against.
   reflexive (bool*) – Whether the relationship is reflexive.
* Raises:
  ValueError – If either risk level is UNKNOWN.

#### property visualize : Text

Return Rich Text representation of this risk level.
