# ChatGPT v4.6 audit reconciliation - 15 Sep 2026

Source audited: exact public v4.6 bytes, SHA-256 `21ee5b344bcdab227b13fa794f0ca9dee4cbfc3b4e650f0e25d2dad287416285`. Each claim was replayed against that source and checked against owner-video/emulator evidence where available.

## Accepted

| Priority | Claim | Decision and evidence |
|---|---|---|
| P0 | Apps center-select routes are dead. | ACCEPT. `screens.apps` exists but there is no `route.apps` or Apps-specific OK handler. Games, Collection, Memory card and Downloads do nothing. |
| P0 | Web center-select routes are dead. | ACCEPT. `screens.store` exists but there is no `route.store` or Store-specific OK handler. Nokia.com, Home, Bookmarks, Go to address and Last web addr. do nothing. |
| P0 | Gallery is cosmetic. | ACCEPT. Gallery OK is literally `notice=screens.gallery[sel]+' opened'`; no destination/state exists. Owner video 2 independently proved nested folders/files/contextual Options. |
| P0 | Media placeholders. | ACCEPT for Camera, Video camera, Radio, Voice recorder and Equaliser in public v4.6. Owner video 2 independently established required state-machine depth. Media player alone has depth. |
| P0/P1 | 29 addressable placeholder screens. | ACCEPT as a truthful breadth census of v4.6. Prior draw coverage must never be reported as feature coverage. Implement by evidence and dependency clusters, not by replacing disclosures with fake notices. |
| P1 | Displayed center actions do nothing. | ACCEPT. Sent Open, To-do Open, Notes Open and call-list center Call have no matching OK handlers. Received/Dialled share the same gap. |
| P1 | 103/178 Options fall through generically. | ACCEPT as a coverage signal, not an exact completion percentage. Current default fallback confirms the issue class. Each option requires paired emulator outcome evidence before implementation. |
| P1 | Alarm config does not fire. | ACCEPT. Only player redraw interval exists; no clock watcher/alarm lifecycle. |
| P1/P2 | Player UI duration logic is internally inconsistent. | ACCEPT in part: UI says 01:30, timing caps at 180s, and progress width is not wired. Total-duration consistency and control state must be corrected against SDK/owner evidence. |
| P2 | Accessibility incomplete. | ACCEPT for the web product: zoom is disabled and LSK/RSK/OK lack accessible names. Adding labels/zoom does not claim Nokia firmware behavior. |

## Disputed or held for evidence

| Claim | Decision and evidence |
|---|---|
| In-call elapsed timer should be displayed. | DISPUTE. The live S40 SDK reference is already documented as having no in-call duration timer. `callStarted`/`fmtTime()` being unused is dead code, not evidence that the UI should show a timer. Remove or retain internal timing only if another real action needs it; do not display a timer contrary to firmware. |
| Media player must display a live elapsed counter. | DISPUTE as stated. The SDK's observed media elapsed counter is frozen at 00:00 during real playback. Match that quirk visually. Accept only the separate internal 01:30-versus-03:00 inconsistency and any progress/control behavior established by paired probes. |
| T9 prefix rendering is inaccurate to S40. | HOLD FOR PAIRED EVIDENCE. The source does use prefix matching and can display a longer dictionary word early, exactly as ChatGPT reports. Whether the target C2-01 firmware truncates candidates to entered digit length must be established with paired emulator keystrokes before changing the engine. Candidate cycling itself passed. |

## Already fixed on dev after v4.6

Paired firmware Home probes exposed and dev now fixes:
- Go to content/order begins Lock keypad, Profiles, Alarm clock, Camera, Video recorder, with real routes.
- Home Up/Down are no-op, matching firmware.
- Home Left/Right cycle standby shortcut focus rather than launching apps immediately.
- Names softkeys match Options / Details / Exit.
- Direct-dial End clears the buffer and returns cleanly.

These are banked as WIP on remote dev commit `280b5fb297a42c0f036c378c269a3346f4ba1e79`; they were not part of the audited v4.6 public snapshot.

## Fix order

1. Finish Batch 01 paired menu/Organiser results and repair every proven divergence.
2. Build shared real-route and contextual-Options architecture, then Gallery nested hierarchy.
3. Implement Apps and Web center routes so top-level sections are not dead.
4. Rebuild Media state machines from owner video 2 plus paired emulator probes: Equaliser, Voice recorder, Radio, player/video, Gallery viewers.
5. Fix displayed center actions and then Options entries in evidence-backed feature clusters.
6. Implement alarm, Countdown and Stopwatch state machines.
7. Resolve player duration/progress against firmware while preserving its frozen elapsed-counter quirk.
8. Run paired T9 prefix probes, then change only if the emulator proves divergence.
9. Add accessibility names and allow browser zoom.
10. Full semantic, state, responsive and visual regression before the next public checkpoint and mandatory Drive audit handoff.
