Tiny soundboard software.
I wanted to have multiple sounds attached to the same hotkey. By pressing the hotkey, a random sound linked to that hotkey is played.
The idea is that any of the sounds convey the same sentiment, but instead of reusing the same sound over and over, some variation is allowed while not running out of hotkeys and not being difficult to memorize dozens of hotkeys.
The Soundboard works even when out of focus.

tested on python 3.10.

### Installation
modules used:
simpleaudio
keyboard

to install them, use pip
`pip install simpleaudio keyboard`

### Usage

Put the .WAV files inside the sounds directory.
Create a file named config.py. Use default_config.py as a model.
to run, simply type
`py main.py`
Press ctrl+i and it should play waw.wav
ctrl+o stops the sounds and ctrl+c stops the entire script.

I recommend using youtube-dl to extract the audio from videos. You can easily do that with following the command:
`youtube-dl -x --audio-format wav -o sounds/mynewsound <youtube-url-here>`
