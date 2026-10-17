# CS 690 Assignment 3: Evidence to Executable Specification

Name: Abraham Eapen
Commit SHA: [insert the submitted commit SHA in the PDF]
Repository: https://github.com/AbrahamEapen/CS690_Assignment3

## Part 1. Evidence log

Case: INT-01. Ten entries: six E, one A, three Q. No entry cites SYN-01.

| ID | Source | Claim | Status | Owner |
| --- | --- | --- | --- | --- |
| E-1 | INT-01:P04 | For a 2:00 camera kit, the student called at 2:08 to say a lab was running long; Jordan wrote "hold until 2:25" on the slip, the kit stayed on the pickup shelf, and the student arrived at 2:22 and completed pickup. Without the call it would have been treated as a no-show after the grace period. | Observed | Jordan Lee, checkout coordinator |
| E-2 | INT-01:P06, INT-01:P21 | The grace period is a lab-configured value that the manager has changed before; once it has passed with no check-in and no recorded hold, the desk may release the kit. The system should use whatever value is configured rather than invent one. | Stated | Media Lab manager |
| E-3 | INT-01:P17, INT-01:P21 | A reservation the student has already checked in for should remain active and not disappear when the clock passes the grace window. | Stated | Jordan Lee, checkout coordinator |
| E-4 | INT-01:P06, INT-01:P17, INT-01:P19, INT-01:P21 | Staff sometimes enter a temporary hold with an end time after a student contacts them, and a recorded hold prevents release (the desk releases only when there is no check-in and no recorded hold). Jordan wants the hold's end time and its reason preserved to explain decisions later. | Stated | Jordan Lee, checkout coordinator |
| E-5 | INT-01:P09, INT-01:P13, INT-01:P21 | A reservation can be marked released before the kit is physically ready: technicians may need to reshelve it, replace a battery, or check accessories, and the waitlist should only see equipment that is actually ready to hand out. Last Thursday a released lighting kit was still behind the counter while technicians checked a light stand and a waitlisted student waited at the desk. | Observed | Equipment technicians |
| E-6 | INT-01:P13 | Last Thursday Priya's 3:00 lighting kit was released before she reached the desk at 3:16 (class ran to 3:11; desk line busy at 3:13). She waited until 3:38 for another kit and her interview started about ten minutes late. Email, call history, and the paper list each showed only part of the sequence. | Observed | Priya Shah, student borrower |
| A-1 | INT-01:P04, INT-01:P21 | Assumption: a staff hold can only extend a reservation past the grace period, never shorten it. The only hold described (until 2:25) ended after the grace period; the interview never says what happens when a hold ends earlier, or whether the hold covers its end minute. | Assumption | Jordan Lee, checkout coordinator |
| Q-1 | INT-01:P06, INT-01:P12 | Which grace value is currently configured, and which value are students told? Jordan says the current policy is 15 minutes; Priya says the desk told students 20 minutes, twice, including in March. | Open | Media Lab manager |
| Q-2 | INT-01:P09, INT-01:P17, INT-01:P19, INT-01:P21 | How do equipment technicians record that a released kit is ready for the next checkout, and who sees that signal? Nobody has asked the technicians. | Open | Equipment technicians |
| Q-3 | INT-01:P10 | Who should get a message before a kit goes to the waitlist (the late student, the waitlisted student, or both), when, and through which channel? | Open | Jordan Lee, checkout coordinator |

## Part 2. Evidence audit

Case: INT-01. Evidence IDs refer to `evidence/evidence_log.md`.

| Item | Location | Classification | Why it matters |
| --- | --- | --- | --- |
| 1. Direct factual contradiction | INT-01:P06, INT-01:P12 | Factual contradiction: Jordan says the current grace period is 15 minutes; Priya says the desk told students 20 minutes, twice. | Any requirement or test that uses either number would silently pick a side in a dispute only a stakeholder can settle. It is logged as Q-1, and the requirements use the configured value G instead. |
| 2. Ambiguous statement 1 | INT-01:P07 | Ambiguity, vague amount of time: "If someone is only a little late, we try not to give the kit away." | "A little late" has no number, so it is unclear whether it means within the grace period or a further informal allowance beyond it. An agent could invent a second threshold the lab never set. |
| 3. Ambiguous statement 2 | INT-01:P10 | Ambiguity, unclear who and what: "They should get a message before it goes to the waitlist." | "They" could be the late student, the waitlisted student, or both, and "it" could be the release or the waitlist offer, so the recipient and trigger of the message are undefined. The channel and timing are also unstated (Q-3). |
| 4. Missing stakeholder | INT-01:P02, INT-01:P09, INT-01:P13, INT-01:P17, INT-01:P19, INT-01:P21 | Missing stakeholder: the equipment technicians, who prepare and re-check kits but were never interviewed ("We have not asked them yet," P19). | The waitlist requirement depends on a preparation-complete signal that only the technicians can define (Q-2). Designing their workflow without them would mean inventing it. |
| 5. Compliment | INT-01:P14 | Compliment, not evidence: "a reservation dashboard that fixed all of this would be amazing." | Enthusiasm for an imagined dashboard says nothing about what the user currently does or needs. Treating it as demand could add a dashboard requirement no past event supports. |
| 6. Prediction about future use | INT-01:P15 | Prediction about hypothetical future behavior: "I would probably use it every time I was delayed." | A guess about using a feature that does not exist is not evidence of current behavior. In P13 she actually called the desk, so only calling is observed behavior. |
| 7. Strongest account of a specific past event | INT-01:P13 | Specific past event (Observed): last Thursday's 3:00 lighting kit, released before she arrived at 3:16 while the kit was still being checked. | It gives concrete times, actions, and consequences: the release, the not-yet-ready kit, the waitlisted student at the desk, and an interview that started late. It directly supports E-5 and E-6 and the waitlist-readiness requirement R-4. |

## Part 3. Requirements, INVEST, and acceptance criteria

Evidence IDs refer to `evidence/evidence_log.md`. `G` is the lab's configured grace period in minutes. All times are whole minutes after the reservation start.

### Four requirement slices

#### R-1. Release after the configured grace period

- **User story:** As a checkout desk worker, I want a reservation with no check-in and no recorded hold to become releasable only once the lab's configured grace period has passed, so that I neither give away a kit too early nor hold it indefinitely.
- **Structured requirement:** When a reservation is not checked in and has no active staff hold, the system shall report it as "held" while minutes after start is less than G, and as "releasable" once minutes after start is G or greater. G is read from lab configuration and is not fixed in the software.
- **Trace:** E-2, Q-1. The value of G stays open (Q-1); only the rule that it is configured is settled.

#### R-2. Checked-in reservations stay active

- **User story:** As a student borrower who has checked in at the desk, I want my reservation to stay active after the grace period passes, so that I do not lose equipment I am already picking up.
- **Structured requirement:** When a reservation is checked in, the system shall report it as "active" at any number of minutes after start, including after G has passed.
- **Trace:** E-3.

#### R-3. Staff-recorded temporary hold

- **User story:** As a checkout desk worker, I want to record a temporary hold with an end time and a reason when a late student contacts the desk, so that the kit is not released while they are on the way and we can explain the decision later.
- **Structured requirement:** When staff record a hold ending H minutes after start on a reservation that is not checked in, the system shall report it as "held" while minutes after start is less than H, even if G has passed, and shall store the hold's end time and reason with the reservation.
- **Trace:** E-1, E-4, and `Assumption` (A-1). Read together with R-1, this slice assumes a hold can only extend a reservation: if a hold ends before G, R-1 still keeps the reservation "held" until G. Clarifying questions for Jordan: if a hold ends before G, does the reservation stay held until G? Is the kit still held at exactly minute H?

#### R-4. Waitlist sees only ready equipment

- **User story:** As a waitlisted student, I want to be offered a kit only when its reservation is releasable and the technicians have finished preparing it, so that I am not sent to the desk for equipment that cannot be handed out yet.
- **Structured requirement:** The system shall offer a kit to the waitlist only when its reservation is "releasable" and preparation is recorded as complete. A releasable kit without completed preparation shall not be offered.
- **Trace:** E-5, Q-2. How technicians record preparation stays open (Q-2).

### INVEST check

| Requirement | I | N | V | E | S | T | Named problem for any fail |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R-1 | Pass | Pass | Pass | Pass | Pass | Pass | None |
| R-2 | Pass | Pass | Pass | Pass | Pass | Pass | None |
| R-3 | Pass | Pass | Pass | Pass | Fail | Pass | S: bundles hold-status behavior with storing the hold reason for later audit |
| R-4 | Fail | Pass | Pass | Fail | Pass | Pass | I: depends on a technician preparation-complete signal that does not exist yet (Q-2). E: the technician workflow cannot be sized until the technicians are interviewed |

### Three acceptance criteria

#### AC-1 (R-2)

- **Given** the lab's configured grace period is G minutes, and the student has checked in for the reservation
- **When** the desk checks the reservation status at G + 10 minutes after start
- **Then** the status is "active"

#### AC-2 (R-3)

- **Given** the lab's configured grace period is G minutes, the student has not checked in, and staff have recorded a hold ending at G + 10 minutes after start
- **When** the desk checks the reservation status at G + 5 minutes after start
- **Then** the status is "held"

AC-2 checks a time strictly inside the hold, so it does not settle whether a kit is still held at exactly minute H (A-1).

#### AC-3 (R-4)

- **Given** a reservation whose status is "releasable", and the technicians have not recorded preparation as complete
- **When** the system checks whether the kit may be offered to the waitlist
- **Then** the kit is not offered (the check returns false)

## Part 4. Implementation-ready specification


### Selected requirement

Requirement ID: R-4. Waitlist sees only ready equipment.
Evidence trace: E-5 (INT-01:P09, INT-01:P13, INT-01:P21), E-2 (INT-01:P06, INT-01:P21), E-3 (INT-01:P17, INT-01:P21), E-4 (INT-01:P06, INT-01:P17, INT-01:P19, INT-01:P21); open items Q-2, Q-3, Q-1, A-1.

### Behavior and scope

Given a reservation's current disposition and whether the technicians have recorded the kit's preparation as complete, decide whether the kit may be offered to the waitlist. The answer is true only for a reservation that is "releasable" and whose kit is recorded as prepared. A release decision on its own is never enough. This specification covers only that decision. Computing the disposition (R-1 to R-3) and recording preparation are inputs, not part of this behavior.

### Typed interface or function signature

```python
from typing import Literal

Disposition = Literal["active", "held", "releasable"]

def can_offer_to_waitlist(
    *,
    disposition: Disposition,
    preparation_complete: bool,
) -> bool: ...
```

### Preconditions

1. `disposition` is exactly one of "active", "held", or "releasable".
2. `disposition` is the reservation's current disposition, computed under the lab's configured grace period and any recorded staff hold (R-1 to R-3). The caller must not pass a disposition computed from a hard-coded grace value.
3. `preparation_complete` is a `bool`, never `None`. The caller passes `True` only when the technicians have recorded that this kit is ready for the next checkout. When no preparation record exists, the caller passes `False`.
4. Both arguments are passed by name.

### Postconditions

1. Returns `True` if and only if `disposition == "releasable"` and `preparation_complete is True`.
2. Returns `False` when `disposition` is "active" or "held", whatever the value of `preparation_complete`.
3. Returns `False` when `disposition` is "releasable" and `preparation_complete` is `False`.
4. Raises `ValueError` and returns nothing when `disposition` is not one of the three allowed values.
5. Has no side effects: it does not change the reservation, the preparation record, or the waitlist, and sends no message.

### Invariant

Across every repeated check on the same reservation, a kit is never offered to the waitlist while its reservation is "active" or "held", or while its preparation is not recorded as complete.

### Edge cases

1. The reservation is "releasable" but the technicians are still checking the kit (INT-01:P13, a light stand being checked while a waitlisted student waited). The function returns `False`.
2. The reservation is "held" and the kit is already packed on the pickup shelf (INT-01:P04). The function returns `False`; being prepared does not override a hold or the grace period.
3. The reservation is "active" because the student checked in, and preparation is complete. The function returns `False`.
4. The caller passes the desk's paper-slip word "released" (INT-01:P09) or any other value outside the `Disposition` type. The function raises `ValueError` and does not map it to "releasable".
5. No preparation record exists yet because the technicians' signal is undefined (Q-2). The caller passes `False`, and the function returns `False`.

### Non-goal

This specification does not notify or contact anyone: it sends no message to the late student, the waitlisted student, or staff (Q-3).

### Settled decisions

1. The waitlist may only see equipment that is actually ready to hand out; a release decision alone is not enough (E-5: INT-01:P09, INT-01:P13, INT-01:P21).
2. A checked-in reservation stays "active", so its kit is never offered to the waitlist (E-3).
3. A reservation still within the configured grace period, or under a recorded staff hold, is "held", so its kit is not offered (E-2, E-4).
4. The grace period is a configured value supplied upstream; this function neither takes nor chooses it (E-2).

### Open questions the implementation agent may not answer

Do not guess any of these. Stop, leave the behavior out, and ask the named owner.

1. Q-2 (equipment technicians): How do technicians record that a kit is prepared, who may set or clear that record, and on what screen or workflow? Do not invent a preparation workflow or a default of `True`.
2. Q-3 (Jordan Lee): Who is told before a kit goes to the waitlist, when, and through which channel? Do not add any notification.
3. Q-1 (Media Lab manager): What is the current grace value? Do not hard-code 15, 20, or any other number upstream of this function.
4. A-1 (Jordan Lee): If a staff hold ends before the grace period, does the reservation stay "held" until the grace period ends, and is it still held at exactly the hold's end minute? Do not settle this in the disposition passed to this function.
5. (Jordan Lee) Can a hold be added, or the original student reinstated, after a reservation has become "releasable" or after the kit has been offered to the waitlist? Do not add reversal or cancellation behavior.
6. (Jordan Lee) When several students are on the waitlist, which of them is offered the kit first? Do not choose an ordering.

## Part 5. Tests

Tests are in `tests/test_student_acceptance.py`. `GRACE_MINUTES = 12` is a configured test value, not policy (Q-1).

| Test name | AC ID | Requirement ID | Evidence ID |
| --- | --- | --- | --- |
| `test_ac1_checked_in_stays_active` | AC-1 | R-2 | E-3 |
| `test_ac2_staff_hold_stays_held` | AC-2 | R-3 | E-1;E-4 |
| `test_ac3_unprepared_kit_not_offered` | AC-3 | R-4 | E-5 |

## Part 6. AI audit and synthetic-user critique

### Audit adjudication

Findings refer to `results/ambiguity_audit.md`. Paragraph IDs refer to INT-01.

| Finding | Classification | Paragraphs | Reason |
| --- | --- | --- | --- |
| 1. Grace period value conflict | True positive | INT-01:P06, INT-01:P12 | Jordan states the current policy is 15 minutes and Priya states the desk's rule is 20 minutes, a direct factual contradiction about the same value (Q-1). |
| 2. Release is optional or automatic | True positive | INT-01:P06, INT-01:P09, INT-01:P19 | "We can release" (P06) is a permission, P09 describes staff marking a reservation released, and P19 separately asks when it "became releasable," so the transcript never says whether release is automatic or a staff action. |
| 3. Undefined "a little late" leniency | True positive | INT-01:P07 | "Only a little late" gives no amount and does not say whether it means within the grace period or a further informal allowance. |
| 4. Pre-waitlist message: who, when, how | True positive | INT-01:P10 | "They" and "it" have no clear referent, and P10 names no timing or channel (Q-3). |
| 5. Hold vs. extension: rules and limits | True positive | INT-01:P04, INT-01:P19, INT-01:P21 | The interview uses both "hold" (P04, P19) and "extend a reservation" (P21) without saying whether they are the same, who may create one, or how long it may last. Its P13 citation is weak, since P13 contains no hold. |
| 6. "Check-in" vs. "picked up" | True positive | INT-01:P02, INT-01:P17, INT-01:P21 | P02 describes the desk marking a reservation "picked up," while P17 and P21 use "checked in" as a state that keeps a reservation active, and the transcript never says whether these are the same event. |
| 7. Readiness signal from technicians undefined | True positive | INT-01:P09, INT-01:P17, INT-01:P19, INT-01:P21 | Jordan says the technicians need a way to mark preparation but "We have not asked them yet," and Priya does not know their signal (Q-2). |
| 8. Waitlist priority and substitute kits | True positive | INT-01:P13, INT-01:P21 | P13 shows a paper list and a different kit handed over, but no paragraph defines waitlist order, where a released borrower goes, or whether substitution is policy, so an agent would have to invent all three. |

### Synthetic-user critique

Each claim below is quoted from `synthetic/synthetic_user_output.md` (SYN-01). INT-01 does not establish any of them.

| # | SYN-01 claim | Why INT-01 does not support it |
| --- | --- | --- |
| 1 | "A likely student borrower wants the media lab reservation process to require as little staff contact as possible." | Priya wanted to know her reservation status (P17) and found calling hard when the line was busy (P13, P15), but she never says she wants less staff contact overall. Her own account depends on desk staff. |
| 2 | "Students probably prefer text-message alerts over email" | No speaker mentions text messages or states a channel preference. P10 only says staff currently "juggle the phone, email, and the person at the desk." |
| 3 | "A 10-minute grace period would likely feel fair for late arrivals." | The only grace values in the interview are 15 (P06) and 20 (P12), and they conflict. Nobody rates any value as fair, and Jordan says the software should not invent policy (P21). |
| 4 | "The strongest feature would be a QR-code self-check-in" | No QR code or self-check-in is mentioned, and no speaker ranks features. Priya's only feature remarks are a compliment (P14) and a prediction (P15). |
| 5 | "so a borrower can preserve a reservation without waiting for a desk worker." | In INT-01, check-in happens at the desk with an ID check (P02, P17), and holds are recorded by staff (P04, P21). Nothing establishes that a borrower could or should preserve a reservation without staff. |
| 6 | "Students who lose a reservation are likely willing to accept a different brand of camera or light automatically, as long as the general equipment category is the same." | Priya took another kit after waiting (P13), but she chose it at the desk. Nothing in the interview mentions brand, automatic substitution, or what students in general are willing to accept. |
| 7 | "Equipment technicians would probably prefer to receive one batch of released-reservation updates" | The technicians were never interviewed (P19, P21), so nothing is known about their preferences. Jordan explicitly says to ask them before deciding how their part works. |
| 8 | "every 30 minutes instead of individual updates." | No update interval appears anywhere in INT-01, so the 30-minute value is invented. |

Not listed, because INT-01 supports them:

- That students move between classes (P12, P13).
- The closing paragraph's statement that late arrival, staff-recorded holds, checked-in reservations, equipment preparation, and waitlist handoff matter (P04, P06, P09, P17, P19, P21).

## Part 7. Traceability and ledger

Matrix from `traceability/template.csv`:

```csv
evidence_id,requirement_id,acceptance_criterion_id,test_name
E-3,R-2,AC-1,test_ac1_checked_in_stays_active
E-1;E-4,R-3,AC-2,test_ac2_staff_hold_stays_held
E-5,R-4,AC-3,test_ac3_unprepared_kit_not_offered
```

The provenance ledger is `LEDGER.md` at the repository root (Entries 1 to 10). Every prompt it references is in `prompts/`.

## Verification

Final output of `python -m pytest -q`:

```text
....                                                                     [100%]
4 passed in 0.01s
```
