import asyncio
import time

@async.coroutine
def check_website:
    print("I'm checking the website!")
    sleep(10)
    # Notify that function is ready to check site again
    return True

@async.coroutine
def await_input:
    print("I'm awaiting input!")

event_loop = asycnio.get_event_loop()

try:
    task = event_loop.create_task(check_website())
    hile True:

# run checker
# await input
""" 10 seconds passes """
# cancel input
