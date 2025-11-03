---
title: openhands.sdk.security.risk
description: API reference for openhands.sdk.security.risk
---

# openhands.sdk.security.risk module

<a id="module-openhands.sdk.security.risk"></a>

### *class* openhands.sdk.security.risk.SecurityRisk(\*values)

Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

Security risk levels for actions.

Based on OpenHands security risk levels but adapted for agent-sdk.
Integer values allow for easy comparison and ordering.

#### UNKNOWN *= 'UNKNOWN'*

#### LOW *= 'LOW'*

#### MEDIUM *= 'MEDIUM'*

#### HIGH *= 'HIGH'*

#### *property* description *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

Get a human-readable description of the risk level.

#### get_color() → [str](https://docs.python.org/3/library/stdtypes.html#str)

Get the color for displaying this risk level in Rich text.

#### *property* visualize *: Text*

Return Rich Text representation of this risk level.

#### is_riskier

**Parameters:**

- `other: [SecurityRisk](#openhands.sdk.security.risk.SecurityRisk)`
- `reflexive: [bool](https://docs.python.org/3/library/functions.html#bool) = True) → [bool](https://docs.python.org/3/library/functions.html#bool`


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

* **Parameters:**
  * **other** ([*SecurityRisk*](#openhands.sdk.security.risk.SecurityRisk)) – The other risk level to compare against.
  * **reflexive** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – Whether the relationship is reflexive.
* **Raises:**
  [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError) – If either risk level is UNKNOWN.
