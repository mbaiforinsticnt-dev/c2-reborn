# C2 Reborn v4.4 fix sequence

Generated from the maximum-depth audit. Evidence order remains physical owner C2-01, SDK emulator, official guide. Preserve the frozen third-party audit snapshot until a later deploy is approved.

## P0: stop false or destructive behavior

1. Fix active-call RSK: `Loudsp.` toggles loudspeaker state and never ends the call. Keep END as the hang-up control. Implement center `Menu`, Options End call, Hold/Mute, and contact display resolution (A-081, A-085 to A-088).
2. Gate LSK by the rendered left-softkey action. Blank LSK must be inert. Separate hardware OK semantics from the visible center label (A-025, A-026, A-067).
3. Guard empty `calview` and clamp all state-backed selections before drawing or acting (A-022, A-032, A-068).
4. Escape every state-backed text value before inserting it in HTML. Version and deeply migrate `c2state`; expose reset demo data (A-093, A-101).
5. Make the complete handset fit 320x568 and 360x640 without clipped controls; verify pixels and hit targets (A-063).

## P1: restore truthful interaction depth

6. Replace the 111 confirmed default-state generic Options notices. First hide or disable impossible/empty-state actions, then implement the core messaging, call, Web, Contacts and Organiser paths (A-035, A-079 to A-084).
7. Make mutable state the single source for Contacts, threads, drafts/sent, calendar, notes, calls and list lengths. Fix fourth-contact arrow reachability and preserve `(page, selection, scroll)` in history (A-095 to A-100, A-103).
8. Implement recipient choice and per-conversation fictional threads. Correct SMS segment/encoding counter and run T9/multitap conformance sequences against emulator (A-054 to A-056, A-097).
9. Split 44 generic placeholders into truthful native empty screens, sourced settings lists and functional Camera/Video/Radio/Recorder/Timer/Stopwatch apps. Remove fake selectable title rows (A-001, A-019, A-041).
10. Rebuild Settings, Apps, Log and Call trees only after matching live SDK root captures. Skip Orange custom rows (A-038 to A-046).

## P2: physical and visual parity

11. Rebuild silhouette from normalized owner-photo landmarks: body bounds, LCD, deck, D-pad, call keys, keypad rows and bottom taper. Match the compact owner proportions while keeping a clean, non-scratched finish (A-071 to A-077).
12. Replace wrong standby treatment with physical-evidence dark default and pale-blue softkey band. Retain theme switching only where sourced (A-057, A-076).
13. Build an explicit `(page,row)->asset` manifest. Remove the fallback icon appearing on 122 unrelated rows. Integrate exact SDK assets, including evidence-backed 0570, and leave unknown icons neutral until captured (A-036, A-064 to A-066).
14. Add authentic status families from sourced captures: Bluetooth, alarm, lock/profile/message/audio/data. Implement call display dim timing (A-078, A-088).
15. Add native list scroll indicators, exact abbreviations and terminology cleanup (A-002, A-018, A-030, A-031, A-049).

## P3: product-quality finish

16. Complete accessible labels, focus announcements, full desktop keyboard controls, pressed states and later long-press behavior (A-034, A-089, A-090).
17. Replace generic Help notices with relevant content or remove them. Implement Main menu view/Organise only when real behavior exists (A-091, A-092).
18. Remove fixed relative-date contradictions and duplicate gallery capacity constants (A-098, A-102).
19. Re-run all matrices after every tier: 89-state render, 1,958 key probes, 83 static routes, 178 Options, responsive geometry, core functional smoke, then exact public-byte and pixel validation.
