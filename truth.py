#
# Author  : Phil Hall, October 2022
# Licence : MIT
#

from microbit import *
import random

while True:
    display.show(' ')
    if button_a.is_pressed() or button_b.is_pressed():
        if random.choice([True, False]):
            display.show(Image.YES)
        else:
            display.show(Image.NO)

        while button_a.is_pressed() or button_b.is_pressed():
            sleep(100)

    sleep(100)
