#
# Author  : Phil Hall, October 2022
# Licence : MIT
#

from microbit import *
import radio
import speech

radio.config(channel = 3)
radio.on()

while True:
    message = radio.receive()
    if message != None:
        display.show(Image.SQUARE)
        print(message)
        speech.say(message)

    display.show(' ')
    
    if button_a.is_pressed():
        message = input('Message : ')
        if message != '':
            radio.send(message)

    sleep(100)
