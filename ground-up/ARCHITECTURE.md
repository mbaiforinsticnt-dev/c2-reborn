# C2-01 Ground-Up architecture

## Software module

`index.html` contains the 240x320 LCD DOM and Black-theme styling. `screen.js` owns software state, routing, drawing, and reactions to semantic keys.

## Hardware/controller module

The outer `.hardware` shell and `.controller` keypad are separate from the `.software` LCD. `controller.js` owns physical pointer input. It publishes `c2-key` events with `{key, source: "hardware-controller"}` and does not mutate screen state or DOM.

The controller exposes left/right softkeys, call/end, four navigation directions, OK, and all twelve number-pad keys. Keyboard input and LCD softkey touch controls enter through the same software key dispatcher for test parity.

Hardware proportions are a functional scaffold until front-on RM-721 measurement evidence is available. The LCD remains exactly 240x320 content pixels.
