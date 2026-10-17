# Part 6. AI audit and synthetic-user critique

## Audit adjudication

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

## Synthetic-user critique

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
