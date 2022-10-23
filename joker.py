#
# Author  : Phil Hall, October 2022
# Licence : MIT
#

from microbit import *
import random

while True:
    if button_a.is_pressed():
       display.show(Image.YES)
    elif button_b.is_pressed():
        display.show(Image.NO)
    else:
        display.show(' ')

    sleep(100)
