# Provenance ledger

Use exactly this format for every entry. Write each entry when the work is done, one entry per reviewable change.

```text
## Entry <n>
artifact:  what this entry covers: a file, a commit SHA, a document, or an experiment
tool:      product name, model name, model version, and the date of use
prompts:   one-line summary each; the verbatim prompts live in prompts/ and are
           referenced here by file path
review:    what you read, what you changed, what you rejected, and why
checks:    the commands you ran and their results
evidence:  the requirement, test, or evidence ID this traces to
risk:      what remains unverified after this change

For an experiment, add three fields:
dataset:   task set identifier and its commit SHA or version
result:    metric, N, and the result table or its file path
changed:   what you did differently as a result
```

Add your entries below this line, starting with Entry 1.

---

## Entry 1
artifact:  evidence/evidence_log.md (Part 1 evidence log), first draft
tool:      Claude Code, Claude Opus 5.5 (claude-opus-5-5), 2026-10-17
prompts:   asked the agent to build the Part 1 evidence log;
           prompts/draft_evidence_and_requirements_prompt.txt
review:    agent drafted 10 entries (E-1 to E-6, A-1, Q-1 to Q-3). It logged the 15 vs 20
           minute grace conflict (P06, P12) as Q-1 rather than as an E fact, kept P14
           (compliment) and P15 (prediction) out of E, and assigned Q-2 to the technicians.
           Student review: re-read each cited INT-01 paragraph and accepted the draft unchanged.
checks:    grep: 10 rows, all IDs E-/A-/Q-; every source uses INT-01:Pxx; no SYN-01 citation
evidence:  E-1 to E-6, A-1, Q-1, Q-2, Q-3
risk:      E-3 and E-4 partly rest on Priya's expectations (P17), which are stated wishes,
           not observed events; A-1 has not been confirmed with Jordan

## Entry 2
artifact:  requirements/requirements.md (Part 3 requirements, INVEST, AC-1 to AC-3), first draft
tool:      Claude Code, Claude Opus 5.5 (claude-opus-5-5), 2026-10-17
prompts:   asked the agent to generate the Part 3 requirements and acceptance criteria;
           prompts/draft_evidence_and_requirements_prompt.txt
review:    agent wrote R-1 to R-4 in Connextra form using a configured grace value G, not 15
           or 20. INVEST fails are R-3 S and R-4 I/E, each with a named problem. The three
           acceptance criteria sit on R-2, R-3 and R-4, and the P10 message was kept out of
           any criterion because it cannot be tested. Student review: re-read each cited INT-01 paragraph and accepted the draft unchanged.
checks:    grep: no 15 or 20 in any requirement or criterion; each criterion has one When;
           AC-2 checks G + 5 inside a hold ending at G + 10, away from both boundaries
evidence:  R-1 to R-4; AC-1 to AC-3; E-1 to E-5; Q-1, Q-2; A-1
risk:      R-1 treats "releasable at exactly G" as settled, based on P06 ("At 15 minutes...
           we can release"); R-4 depends on the undefined technician signal (Q-2)

## Entry 3
artifact:  evidence/evidence_audit.md (Part 2 seven-row evidence audit), first draft
tool:      Claude Code, Claude Opus 5.5 (claude-opus-5-5), 2026-10-17
prompts:   asked the agent to draft the Part 2 audit; prompts/draft_evidence_audit_prompt.txt
review:    agent chose P06/P12 (contradiction), P07 (vague amount), P10 (unclear who),
           technicians (missing stakeholder), P14 (compliment), P15 (prediction), and P13
           (strongest past event, ahead of P04). The contradiction row names both values
           without choosing one. Student review: re-read each cited INT-01 paragraph and accepted the draft unchanged.
checks:    awk/grep: every "why it matters" cell has 2 sentences (limit is 2)
evidence:  Q-1, Q-2, Q-3, E-5, E-6; INT-01:P06, P07, P10, P12, P13, P14, P15, P19
risk:      the two ambiguity rows are judgment calls; P19/P21 "temporary hold" (no length)
           and "actually ready" (P09, P21) were other candidates

## Entry 4
artifact:  evidence/evidence_log.md (E-4) and requirements/requirements.md (R-3 trace), rubric review revisions
tool:      Claude Code, Claude Opus 5.5 (claude-opus-5-5), 2026-10-17
prompts:   asked the agent to review Parts 1 to 3 against HANDOUT.md and RUBRIC.md;
           prompts/review_parts_1_to_3_prompt.txt
review:    agent added INT-01:P06 to E-4 so that Jordan's statement, not only Priya's
           expectation, supports "a recorded hold prevents release". It also made R-3's
           reliance on A-1 explicit: R-1 plus R-3 implied a hold can only extend, which the
           interview never settles, so R-3 is now labeled `Assumption` with clarifying
           questions. Student review: re-read each cited INT-01 paragraph and accepted the draft unchanged.
checks:    grep: 10 log entries; no SYN-01 citation; no 15 or 20 in requirements or criteria
evidence:  E-4, A-1, R-1, R-3
risk:      hold-before-grace and hold end-minute behavior remain unconfirmed by Jordan

## Entry 5
artifact:  spec/spec_template.md (Part 4 spec for R-4) and evidence/evidence_log.md (E-5 source)
tool:      Claude Code, Claude Opus 5.5 (claude-opus-5-5), 2026-10-17
prompts:   asked the agent to draft the Part 4 specification; prompts/draft_spec_prompt.txt
review:    agent chose R-4 because its core rule (releasable and prepared) is settled by P09,
           P13, P17 and P21, and took the undefined preparation signal as a bool input. It
           added P21 to E-5 so settled decision 1 traces to the log. The spec has 4
           preconditions, 5 postconditions, 1 invariant, 5 edge cases, 1 non-goal, 4 settled
           decisions and 6 open questions. Student review: read the spec against the evidence log and rubric and accepted it unchanged.
checks:    grep: 0 lines with return/if/raise inside the signature block (body is `...`);
           exactly 1 Non-goal section
evidence:  R-4; E-2, E-3, E-4, E-5; Q-1, Q-2, Q-3, A-1
risk:      open questions 5 (hold after release) and 6 (waitlist order) are not in the
           evidence log; "no record means False" relies on P09, not on a technician answer

## Entry 6
artifact:  tests/test_student_acceptance.py (Part 5 tests) and traceability/template.csv (Part 7 matrix)
tool:      Claude Code, Claude Opus 5.5 (claude-opus-5-5), 2026-10-17
prompts:   asked the agent to turn AC-1 to AC-3 into tests; prompts/draft_tests_prompt.txt
review:    agent wrote one test per criterion, with the AC ID in each test name and an
           adjacent comment. Expected values come from each criterion's Then, not from the
           reference code. GRACE_MINUTES = 12 is commented as a configured test value,
           chosen so as not to pick 15, 20, or SYN-01's 10. Student review: compared each test with its AC and accepted the inputs and asserts;
           renamed the tests to test_ac1_checked_in_stays_active, test_ac2_staff_hold_stays_held,
           and test_ac3_unprepared_kit_not_offered (matrix updated to match).
checks:    python -m pytest -q -> 4 passed in 0.01s; git status: reference/ and
           tests/test_reference_smoke.py unmodified; every matrix ID found in the evidence
           log and requirements, and every matrix test name defined in the test file
evidence:  AC-1/R-2/E-3; AC-2/R-3/E-1;E-4; AC-3/R-4/E-5
risk:      tests exercise one configured G only; A-1 boundary cases are deliberately untested

## Entry 7
artifact:  results/ambiguity_audit.md (Part 6 AI ambiguity audit, the one required run)
tool:      Claude Code, Claude Opus 5.5 (claude-opus-5-5), 2026-10-17; run as a subagent
           with a fresh context
prompts:   the provided audit prompt, unchanged, followed by the full pasted text of
           transcripts/interview.txt; prompts/ambiguity_audit_prompt.txt
review:    the response (8 findings) is saved unedited below a short provenance header; only
           the tool's reply indentation was removed. Student review: checked every finding against INT-01; response kept unedited.
checks:    exactly one run; the subagent's input contained only the prompt and the transcript
           (no SYN-01, no evidence log)
evidence:  INT-01:P02-P21; Q-1, Q-2, Q-3, A-1
risk:      model output is not evidence; finding 5 cites P13, which contains no hold

## Entry 8
artifact:  report/part6_adjudication.md (Part 6 adjudication and synthetic-user critique)
tool:      Claude Code, Claude Opus 5.5 (claude-opus-5-5), 2026-10-17
prompts:   asked the agent to adjudicate the audit findings and critique SYN-01;
           prompts/draft_part6_prompt.txt
review:    agent classified all 8 findings as true positives, each with paragraph IDs and one
           sentence of reasoning, and flagged finding 5's weak P13 citation. It listed 8
           unsupported SYN-01 claims, splitting QR check-in from "without a desk worker" and
           batching from "every 30 minutes", and excluded 2 claims INT-01 supports.
           Student review: checked each finding and each SYN-01 claim against INT-01 and
           accepted the classifications.
checks:    grep: 16 table rows (8 findings, 8 claims); each listed claim checked for absence
           in INT-01
evidence:  audit findings 1-8; SYN-01; INT-01:P02-P21
risk:      the same model family produced both the audit and its adjudication; finding 8
           could reasonably be judged a false positive

## Entry 9
artifact:  LEDGER.md and traceability/template.csv (Part 7 review)
tool:      Claude Code, Claude Opus 5.5 (claude-opus-5-5), 2026-10-17
prompts:   asked the agent to review and complete Part 7; prompts/review_part7_prompt.txt
review:    agent split the old Entry 1 into one entry for Part 1 and one for Part 3, replaced
           placeholder review/checks/risk text with what was actually done and checked, and
           kept one marked line per entry for the student's own review. The matrix needed no
           changes. Student review: supplied the review decisions recorded in Entries 1-8.
checks:    script: every prompts/ path in this ledger exists; all 3 matrix rows have 4 filled
           columns; all IDs resolve; all test names exist
evidence:  traceability/template.csv rows for AC-1, AC-2, AC-3
risk:      none beyond the per-entry risks above

## Entry 10
artifact:  tests/test_student_acceptance.py and traceability/template.csv (test renames),
           LEDGER.md (student review lines), report/REPORT.md (assembled report)
tool:      Claude Code, Claude Opus 5.5 (claude-opus-5-5), 2026-10-17
prompts:   asked the agent to collect the student's review decisions and apply them;
           prompts/student_review_round_prompt.txt
review:    the student decided to keep R-1's "releasable at exactly G" as settled (P06), keep
           audit finding 8 as a true positive, keep spec open questions 5 and 6, and keep P13
           alone for Part 2 row 7. The student asked for the tests to be renamed; the agent
           chose the shorter names and updated the matrix to match. The agent assembled
           report/REPORT.md from the part files.
checks:    python -m pytest -q -> 4 passed in 0.01s; grep: no "[fill in]" left in LEDGER.md;
           every matrix test name is defined in the test file
evidence:  AC-1/R-2/E-3; AC-2/R-3/E-1;E-4; AC-3/R-4/E-5
risk:      the commit SHA must still be written into the PDF; the PDF itself is not in the repo
