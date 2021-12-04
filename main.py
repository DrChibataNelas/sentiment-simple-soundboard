import keyboard
import simpleaudio as sa
from time import sleep

from simpleaudio.shiny import stop_all
from config import *
#from logging import basicConfig, INFO, info, debug, DEBUG
from random import choice

hotkeys = {k:[sa.WaveObject.from_wave_file(val) for val in v] for k,v in hotkeys.items()}

def play_sound(hotkey):
    choice(hotkeys[hotkey]).play()

    
for key in hotkeys:
    keyboard.add_hotkey(key, play_sound, args=(key,))
keyboard.add_hotkey(stop_key, stop_all)
    

# TODO
# function to play one of x sounds added to the same key, import from random
# config file to link hotkeys to audio_files
if __name__ == "__main__":
    while True:
        sleep(3600) #could do 99999 which is more than 24hhttps://www.youtube.com/watch?v=U1UtRnGn5hc
    # while True:
    #     pass