# Ambiguity audit result

Run once on 2026-10-17 with Claude Opus 5.5 (claude-opus-5-5), as a Claude Code subagent with a fresh context. Its entire input was the exact text of `prompts/ambiguity_audit_prompt.txt` followed by the full text of `transcripts/interview.txt` pasted in. It received no other files. The complete response follows, unchanged.

---

INT-01 audit: 8 findings. I left P14 and P15 out as evidence because they are hypothetical feature wishes, not reports of what happened.

1. **Grace period value conflict**
   - Paragraphs: P06, P12
   - Excerpt: "The current policy is 15 minutes after the reservation start" vs "The desk's rule is 20 minutes... 20 is the number students hear."
   - Defect type: Direct contradiction
   - Unsafe decision: The team cannot tell which grace value to use as the default or in student-facing messages, or whether the configured value should match what staff tell students.

2. **Release is optional or automatic**
   - Paragraphs: P06, P09, P19
   - Excerpt: "At 15 minutes... we can release the kit"; "when the reservation became releasable"; "We mark the reservation as released"
   - Defect type: Ambiguity
   - Unsafe decision: It is unclear whether the system releases a reservation when the grace period ends or only marks it releasable for staff to decide, and whether "released" and "releasable" are separate states.

3. **Undefined "a little late" leniency**
   - Paragraphs: P07, P06
   - Excerpt: "If someone is only a little late, we try not to give the kit away."
   - Defect type: Ambiguity (it also sits uneasily with the fixed grace rule)
   - Unsafe decision: Nobody says whether this leniency is a rule, a threshold, or staff judgment, or how it fits with the configured grace period, so a developer would have to make up a release rule.

4. **Pre-waitlist message: who gets it, when, and how**
   - Paragraph: P10
   - Excerpt: "They should get a message before it goes to the waitlist."
   - Defect type: Ambiguity / Incompleteness
   - Unsafe decision: "They" could mean the original borrower or the waitlisted student, and nothing says how far ahead, through what channel, or whether a reply changes the outcome.

5. **Hold vs. extension: rules and limits**
   - Paragraphs: P04, P13, P19, P21
   - Excerpt: "wrote 'hold until 2:25'"; "whether staff entered a temporary hold and until when"; "Staff sometimes extend a reservation after a student contacts us"
   - Defect type: Ambiguity / Incompleteness
   - Unsafe decision: Several things are undefined:
     - whether a "hold" and an "extension" are the same thing
     - who may create one
     - how long it can last
     - whether a contact attempt that failed counts (in P13 the student tried twice and got a busy line; in P04 a call that got through led to a hold)

6. **"Check-in" vs. "picked up"**
   - Paragraphs: P02, P17, P21
   - Excerpt: "mark the reservation picked up"; "If I have already checked in at the desk, it should not suddenly disappear"; "a checked-in reservation should remain active"
   - Defect type: Ambiguity
   - Unsafe decision: The current process only describes marking a reservation picked up, so it is unclear whether "checked in" is a separate earlier state, and if so, what triggers it and where it can happen.

7. **Readiness signal from technicians undefined**
   - Paragraphs: P09, P17, P19, P21
   - Excerpt: "The equipment technicians need some way to mark the preparation step, but I cannot tell you what screen or workflow would work for them. We have not asked them yet."
   - Defect type: Incompleteness (stakeholder not consulted)
   - Unsafe decision: The rule that the waitlist only sees ready equipment depends on a readiness signal whose source, steps, and owner are all unknown, and the interviewees explicitly said not to invent it.

8. **Waitlist priority and substitute kits**
   - Paragraphs: P13, P09, P21
   - Excerpt: "A waitlisted student was there... The desk worker... wrote my name on a paper list. I waited until 3:38, when another kit came back. I took that one"
   - Defect type: Incompleteness
   - Unsafe decision: Several things are unspecified:
     - how the waitlist is ordered
     - whether a released original borrower joins it, and in what position
     - whether a different kit of the same type can be given out instead
     - what happens when the waitlisted person is already at the counter
