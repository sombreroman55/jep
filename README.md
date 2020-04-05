# Jep!
Simple Jeopardy game in Python using the PyQt5 framework.
I made this primarily for usage with my friends for use over
video chats, where I serve as the host and they buzz in their
answers.

## Overview
Below is a screenshot of the program. The game is played the same as
normal Jeopardy. If you don't know how to play Jeopardy, see
[here](https://en.wikipedia.org/wiki/Jeopardy!)

![Jep! screenshot](./resources/img/README-screenshot.png)

The game controls are detailed below.

## Dependencies
This project depends heavily on the PyQt5 framework.
In order to play the sounds, the mpv media player must 
be installed on your system as well.

## Controls
The game is controlled primarily through the keyboard, with the mouse
being used to click on the clues.

| Key       | Action (Normal Mode)      | Action (Wager Mode)       |
| --------- | ------------------------- | ------------------------- |
| q         | Quit application          | Quit application          |
| w         | Toggle wager mode         | Toggle wager mode         |
| 0-9       | Select player             | Edit wager amount         |
| Space     | (On clue screen) Reveal answer | (On clue screen) Reveal answer |
| k         | Increase selected player score by selected clue amount | Increase selected player score by wager amount |
| j         | Decrease selected player score by selected clue amount | Decrease selected player score by wager amount |
| Escape    | (On clue screen) Exit back to categories | - |
| n         | (On card) Move to next screen | (On card) Move to next screen |
| c         | - | Reset current wager amount to 0 |
| s         | (On Final Jeopardy screen) Play Jeopardy theme | - |

## License
This software is licensed under the MIT License. Do whatever you want
with it according to that license.
