# microbit-fun

Simple programs for one or two version 2 micobits.


*Door Bell*

This requires 2 microbits one to be the button outside on the front door, the second is some where inside where it can be heard.

There are 2 programs doorbell_a.py the button and doorbell_b.py the bell.

*Intercom*

This requires 2 microbits both are running the program `intercom.p`y. Press a button on one microbit the other plays a note high notes for button b, low ones for button a.  Try sending morse code messages using button a for dash and button b for dot.

*2 Way Talker*

`talker.py` requires 2 microbits and you have to be running a REPL session to type messsages in or to read them. Press button a to break out of listen mode and type your message, press enter to send it and resume listening. Load `talker.py` onto 2 microbits and send and recieve simple e-mail messages.

*Truth Machine*

Use `truth.py` to determine if you have a liar in your circle.  Ask a friend a question then test their answer with the truth machine, get them to press either button a or button b.  A tick for truth or a cross for lies will be displayed.

*Jokers Truth Machine*

`joker.py` like `truth.py` is used for interrogation. The trick here is ask a friend a question and get their response.  Now ask tem "Which button do you inntend to press to reveal to determine truth or lies?".  You now say something that makes the outcome funny or embarassing for your friend and get them to press the button.  The trick here is that, button a always displays a tick and button b a cross.