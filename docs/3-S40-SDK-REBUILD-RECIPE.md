# Nokia Series 40 6th Edition SDK emulator - rebuild recipe (e2b sandbox, Linux)

## 0. Result
Real S40 6th Ed FP1 device software running under Wine on :99 (Xvfb), full phone OS UI.
Phone window title: "(6260000) Series 40 6th Edition SDK". JRE6 javaw hosts it.

## 1. Downloads
- SDK installer: https://archive.org/download/s-40-6th-edition-sdk/S40_6th_Edition_SDK.exe  (save as /home/sandbox/s40/S40_6th_Edition_SDK.exe)
- JRE 6 installer (jre6.exe) is alongside on the same archive.org item page.
  INSTALL JRE 6 FIRST (the SDK installer needs an existing JRE; newer JREs fail).

## 2. System deps (apt, i386 enabled)
- Wine 11.17 amd64 custom build at /home/sandbox/s40/wine-11.17-amd64/bin (rebuild: standard wine build; prefix PATH).
  (Any modern Wine with 32-bit support works; this build was known-good.)
- dpkg --add-architecture i386; install wine32 deps into /home/sandbox/s40/i386root/lib32
  (extracted .debs; LD_LIBRARY_PATH points there because sandbox user can't write system dirs)
- xvfb, xdotool, imagemagick (import), python3 + PIL.

## 3. Wine prefix
WINEPREFIX=/home/sandbox/s40/prefix  (NOT ~/.wine)
WINEDLLOVERRIDES=mscoree,mshtml=     (kill .NET/IE hooks)
winecfg: Windows version = Windows XP (default fine); no special tweaks needed.
Install JRE 6 into the prefix first, then the SDK:
  wine jre6.exe /s
  wine S40_6th_Edition_SDK.exe /S     (silent; default paths)
SDK lands at: $WINEPREFIX/drive_c/... and a working copy was rsynced to
/home/sandbox/s40/sdk-final/S40_SDK_3rd_Ed_FP1_Component/

## 4. Timeshift shim (media player certificate fix)
The media player rejects playback at the real 2026 date ("Certificate invalid").
Build 64-bit + 32-bit LD_PRELOAD shims overriding clock_gettime/time/gettimeofday
to a fixed 2008 date (June 2008 known-good):
  /tmp/timeshift.so /tmp/timeshift32.so   (regenerate from source in /home/sandbox/s40/timeshift.c if /tmp wiped)
Launch with LD_PRELOAD="/tmp/timeshift.so /tmp/timeshift32.so".

## 5. Launch
pkill -9 wineserver; pkill -9 winedevice   (clean slate)
Xvfb :99 &
DISPLAY=:99 WINEPREFIX=/home/sandbox/s40/prefix \
  WINEDLLOVERRIDES=mscoree,mshtml= \
  LD_PRELOAD="/tmp/timeshift.so /tmp/timeshift32.so" \
  LD_LIBRARY_PATH=/home/sandbox/s40/i386root/lib32 \
  PATH=/home/sandbox/s40/wine-11.17-amd64/bin:$PATH \
  wine /home/sandbox/s40/sdk-final/S40_SDK_3rd_Ed_FP1_Component/bin/S40_6th_Edition_SDK_em.exe &
Wait ~60-90s for phone boot; resolve window id: wmctrl -l | grep "Series 40 6th Edition SDK"
(pick the row whose title does NOT contain "Diagnostics").

## 6. LCD capture
import -window <winid> /tmp/x.png
LCD crop is window-relative (63,114)-(303,483) => 240x369:
  python3 -c "from PIL import Image; Image.open('/tmp/x.png').crop((63,114,303,483)).save('/tmp/x_lcd.png')"

## 7. Keymap (xdotool key --window <winid>)
F9 = left softkey (Options/Yes...) ; F11 = middle select (Select/Menu/Yes)
F12 = right softkey (Back/Names/Exit) ; KP_Subtract = End (red)
Digits enter via multitap; PC keyboard letters do NOT type into text fields (digits only).
Keys drop/queue: one press per 4-6s, verify by capture. First press after idle only un-dims backlight.
Exiting an app can raise "Close application?" (F11 = Yes).
Up during an active call backgrounds the call UI; call stays live (status-bar receiver icon).

## 8. SDK quirks observed
- Media player elapsed counter frozen at 00:00 during real playback.
- In-call screen has NO duration timer (identical at 5s vs 65s).
- Media library index does NOT persist across emulator restarts:
  after each restart, Media player -> Options -> Update library (E: = memory card).
  Sample track: /tmp/sample.mp3 dropped into memory-card dir, appears as "S40 Test Tone" after update.
- Camera/Video recorder has no camera device; deepest screen = landscape "Video recorder on standby / Continue".

## 9. Asset carve (package_c.ppm)
Source: $WINEPREFIX/drive_c/.../bin/Resources/Packages/package_c.ppm
Carve script: /home/sandbox/s40/carve_ppm.py -> /tmp/ppm_img/png_<offset>_<WxH>.png (1433 PNGs)
Builder resource IDs are 0-BASED by ascending carve offset (ID i = i-th file in offset-sorted list).
Map file: /tmp/icon56_list.txt (offset->filename). Full zip: /tmp/sdkassets_png_full.zip + manifest.csv.
Known IDs: 0570 = true Create-message icon (yellow envelope + blue pencil);
Web menu badges: Nokia.com 0590, Home 0581, Bookmarks 1093 (arrow, not checkmark),
Go to address 0578, Last web addr. 0586; main-menu Web plain globe = 0487/0639 (identical dupes).
