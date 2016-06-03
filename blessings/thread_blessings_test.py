#! python3

import threading
from blessings import Terminal
from time import strftime, sleep
######################################################################

thread_lock = threading.Lock()
term = Terminal()

######################################################################


# Return initial results
def get_first_results():

    print("\n{} || Return result 1".format(strftime("%H:%M:%S")))
    sleep(1)
    print("{} || Return result 2".format(strftime("%H:%M:%S")))
    sleep(1)
    print("{} || Return result 3\n".format(strftime("%H:%M:%S")))

##################################


# Check for new result
def check_for_new_site():

    for i in range(1, 11):
        with term.location():
                    print(term.move(0, 1) + "\nworking")
                    sleep(3)
                    if i < 10:
                        print(term.move(0, 1) + "\nStill the old result")
                    else:
                        print(term.move(0, 1) + "\nIt's a new result!")
                        get_new_result()

##################################


def get_new_result():

    print("Getting new result")
    sleep(1)
    print("{} || Return new result\n".format(strftime("%H:%M:%S")))

##################################


def cmd_input():

        cmd = input("> ")

        if cmd == 'n':
            print("Moving to next result...\n")

        elif cmd == 'b':
            print("Moving to previous result...\n")

        elif cmd == 'q':
            print("Quitting...\n")

##################################


def threader():

    """
    while True:
        # gets a worker from the queue
        worker = q.get()

        # Run func with available worker in queue (thread)
        # func(worker)

        # Indicate completed func
        q.task_done()
    """

######################################################################

if __name__ == "__main__":

    get_first_results()

    thread_checker = threading.Thread(target=check_for_new_site)
    # thread_cmd_input = threading.Thread(target=cmd_input())

    thread_checker.daemon = True
    thread_checker.start()
    #thread_cmd_input.start()

    while True:
        cmd_input()
