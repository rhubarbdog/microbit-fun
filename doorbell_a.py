#
# Author : Phil Hall, October 2022
# Licence : MIT
#

from microbit import *
import music
import radio

radio.config(channel = 1)
radio.on()


while True:
    if button_a.is_pressed():
        radio.send('["G4:4", "C4:4"]')
        display.show(Image.SQUARE)
        sleep(1000)
        display.show(' ')
        
    sleep(100)
