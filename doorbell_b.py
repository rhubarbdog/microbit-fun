#
# Author  : Phil Hall, October 2022
# Licence : MIT
#

from microbit import *
import music
import radio

radio.config(channel = 1)
radio.on()


while True:
    play = radio.receive()
    if play != None:
        display.show(Image.SQUARE)
        music.play(eval(play))
        display.show(' ')
        
    sleep(100)
