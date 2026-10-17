# Implementation-ready specification template

## Selected requirement

Requirement ID: R-4. Waitlist sees only ready equipment.
Evidence trace: E-5 (INT-01:P09, INT-01:P13, INT-01:P21), E-2 (INT-01:P06, INT-01:P21), E-3 (INT-01:P17, INT-01:P21), E-4 (INT-01:P06, INT-01:P17, INT-01:P19, INT-01:P21); open items Q-2, Q-3, Q-1, A-1.

## Behavior and scope

Given a reservation's current disposition and whether the technicians have recorded the kit's preparation as complete, decide whether the kit may be offered to the waitlist. The answer is true only for a reservation that is "releasable" and whose kit is recorded as prepared. A release decision on its own is never enough. This specification covers only that decision. Computing the disposition (R-1 to R-3) and recording preparation are inputs, not part of this behavior.

## Typed interface or function signature

```python
from typing import Literal

Disposition = Literal["active", "held", "releasable"]

def can_offer_to_waitlist(
    *,
    disposition: Disposition,
    preparation_complete: bool,
) -> bool: ...
```

## Preconditions

1. `disposition` is exactly one of "active", "held", or "releasable".
2. `disposition` is the reservation's current disposition, computed under the lab's configured grace period and any recorded staff hold (R-1 to R-3). The caller must not pass a disposition computed from a hard-coded grace value.
3. `preparation_complete` is a `bool`, never `None`. The caller passes `True` only when the technicians have recorded that this kit is ready for the next checkout. When no preparation record exists, the caller passes `False`.
4. Both arguments are passed by name.

## Postconditions

1. Returns `True` if and only if `disposition == "releasable"` and `preparation_complete is True`.
2. Returns `False` when `disposition` is "active" or "held", whatever the value of `preparation_complete`.
3. Returns `False` when `disposition` is "releasable" and `preparation_complete` is `False`.
4. Raises `ValueError` and returns nothing when `disposition` is not one of the three allowed values.
5. Has no side effects: it does not change the reservation, the preparation record, or the waitlist, and sends no message.

## Invariant

Across every repeated check on the same reservation, a kit is never offered to the waitlist while its reservation is "active" or "held", or while its preparation is not recorded as complete.

## Edge cases

1. The reservation is "releasable" but the technicians are still checking the kit (INT-01:P13, a light stand being checked while a waitlisted student waited). The function returns `False`.
2. The reservation is "held" and the kit is already packed on the pickup shelf (INT-01:P04). The function returns `False`; being prepared does not override a hold or the grace period.
3. The reservation is "active" because the student checked in, and preparation is complete. The function returns `False`.
4. The caller passes the desk's paper-slip word "released" (INT-01:P09) or any other value outside the `Disposition` type. The function raises `ValueError` and does not map it to "releasable".
5. No preparation record exists yet because the technicians' signal is undefined (Q-2). The caller passes `False`, and the function returns `False`.

## Non-goal

This specification does not notify or contact anyone: it sends no message to the late student, the waitlisted student, or staff (Q-3).

## Settled decisions

1. The waitlist may only see equipment that is actually ready to hand out; a release decision alone is not enough (E-5: INT-01:P09, INT-01:P13, INT-01:P21).
2. A checked-in reservation stays "active", so its kit is never offered to the waitlist (E-3).
3. A reservation still within the configured grace period, or under a recorded staff hold, is "held", so its kit is not offered (E-2, E-4).
4. The grace period is a configured value supplied upstream; this function neither takes nor chooses it (E-2).

## Open questions the implementation agent may not answer

Do not guess any of these. Stop, leave the behavior out, and ask the named owner.

1. Q-2 (equipment technicians): How do technicians record that a kit is prepared, who may set or clear that record, and on what screen or workflow? Do not invent a preparation workflow or a default of `True`.
2. Q-3 (Jordan Lee): Who is told before a kit goes to the waitlist, when, and through which channel? Do not add any notification.
3. Q-1 (Media Lab manager): What is the current grace value? Do not hard-code 15, 20, or any other number upstream of this function.
4. A-1 (Jordan Lee): If a staff hold ends before the grace period, does the reservation stay "held" until the grace period ends, and is it still held at exactly the hold's end minute? Do not settle this in the disposition passed to this function.
5. (Jordan Lee) Can a hold be added, or the original student reinstated, after a reservation has become "releasable" or after the kit has been offered to the waitlist? Do not add reversal or cancellation behavior.
6. (Jordan Lee) When several students are on the waitlist, which of them is offered the kit first? Do not choose an ordering.
