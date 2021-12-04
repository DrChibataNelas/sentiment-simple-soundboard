import keyboard
import simpleaudio as sa
from time import sleep

from simpleaudio.shiny import stop_all
#from logging import basicConfig, INFO, info, debug, DEBUG
from random import choice
from pathlib import Path
try:
    from config import *
except ModuleNotFoundError:
    from default_config import *
    

sounds_dir = Path("sounds")
hotkeys = {k:[sa.WaveObject.from_wave_file(f"{sounds_dir / val}") for val in v] for k,v in hotkeys.items()}

def play_sound(hotkey):
    choice(hotkeys[hotkey]).play()

    
for key in hotkeys:
    keyboard.add_hotkey(key, play_sound, args=(key,))
keyboard.add_hotkey(stop_key, stop_all)
    

if __name__ == "__main__":
    while True:
        # is there a better way to this? I just want the script to listen to keyboard events
        sleep(3600) 