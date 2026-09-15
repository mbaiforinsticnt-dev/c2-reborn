# Paired differential Batch 01 - Home findings

SDK evidence: emulator probes 1-21 with before/after LCD captures from `probe_b1_home_captures`; web replay recorded in `differential-b1-home-web-replay.json`.

| ID | Severity | Divergence | Resolution/status |
|---|---|---|---|
| A-148 | High | Home LSK Go to ordering/content differed. SDK begins Lock keypad, Profiles, Alarm clock, Camera, Video recorder. | Fixed locally: exact observed leading order and real routes. Remaining lower rows await full SDK list census. |
| A-149 | High | Home Up/Down launched Calendar/Names on web; SDK shows no visible change. | Fixed locally: no-op on Home. |
| A-150 | High | Home Left/Right launched Composer/Media player on web; SDK cycles a standby shortcut bar (Web ↔ Gallery) with Options/Select/Exit. | Fixed locally with explicit standby focus state, cycling and Select destinations. |
| A-151 | Medium | Names middle/right softkeys were Open/Back; SDK shows Details/Exit. | Fixed locally. |
| A-152 | High | End from direct dial returned Home but left `dial` buffer in memory; next direct dial could reuse stale digits under alternate entry paths. SDK verified clean clear-and-exit. | Fixed locally: End resets `dial`, `homeFocus` and navigation transient state. Replay proves 2 → End → 3 yields only 3. |
| A-153 | Evidence gap | SDK `#` did not register through keyboard input. | Do not copy artifact. Wait for emulator skin-button result. |
| A-154 | Evidence gap | SDK Call requires clickable green skin button. | Wait for emulator probe; current web Call from Home opens empty dial editor and is not yet certified. |

Replay passed SDK-matched behaviors for Go to, Menu, Names softkeys, Up/Down no-op, Left/Right shortcut focus, idle End, first digit retention, End clear, fresh digit and `*` entry. Visual differences in contacts demo names are expected fictional-public-data substitutions, not a behavior divergence.
