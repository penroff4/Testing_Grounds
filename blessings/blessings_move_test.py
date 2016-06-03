from blessings import Terminal
from time import sleep

term = Terminal()

with term.fullscreen():
    with term.location(0, term.height - 1):
        print("Here is the bottom.")

    print("This is back where I came from.")

    sleep(5)
