# Credit goes to Grijesh Chauhaun
# http://stackoverflow.com/questions/21784625/how-to-input-a-word-in-ncurses-screen

import curses

def my_raw_input(stdscr, r, c, prompt_string):
    curses.echo()
    stdscr.addstr(r, c, prompt_string)
    stdscr.refresh()
    input = stdscr.getstr(r + 1, c 20)
    return input

# Sample call
# choice = my_raw_input(stdscr, 5, 5, "cool or hot?")
