#
# Author  : Phil Hall, October 2022
# Licence : MIT
#

from microbit import *
import radio
import music

radio.config(channel = 2)
radio.on()

while True:
    note = radio.receive()
    if note != None:
        display.show(Image.SQUARE)
        play = []
        play.append(note)
        music.play(play)

    display.show(' ')

    if button_a.is_pressed():
        note = 'c4:4'
    elif button_b.is_pressed():
        note = 'g4:4'
    else:
        note = None
        
    if note != None:
        display.show(Image.HEART)
        radio.send(note)
        sleep(400)

    sleep(50)
