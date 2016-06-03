from blessings import Terminal

term = Terminal()
with term.location(2, 5):
    print('Hello, world!')
    for x in range(1, 11):
        print("I can do it {} times!".format(x))

