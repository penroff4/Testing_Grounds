#!/usr/bin/env python3

import curses
from os import system

def get_param(prompt_string):
    screen.clear()
    screen.border(0)
    screen.addstr(2,2, prompt_string)
    screen.refresh()
    var = screen.getstr(10,10,60)
    return var

def execute_cmd(cmd_string):
    system("clear")
    a = system(cmd_string)
    print("")
    if a == 0:
        print("Command executed correctly")
    else:
        print("Command terminated with error")
    input("Press enter")
    print("")

x = 0

while x != ord('4'):
    screen = curses.initscr()

    screen.clear()
    screen.border(0)
    screen.addstr(2,2,"Please enter a number...")
    screen.addstr(4,4,"1 - add a user")
    screen.addstr(5,4,"2 - Restart Apache")
    screen.addstr(6,4,"3 - Show disk space")
    screen.addstr(7,4,"4 - Exit")
    screen.refresh()

    x = screen.getch()
        
    if x == ord('1'):
        username = get_param("Enter the username")
        homdir = get_param("Enter the home dir")
        groups = get_param("Enter comma separated groups")
        shell = get_param("Enter shell")
        curses.endwin()
        execute_cmd("echo " + str(username) + " " + str(homdir) + " "
                + str(groups) + " " + str(shell))

    if x == ord('2'):
        curses.endwin()
        execute_cmd("echo apachectl restart")

    if x == ord('3'):
        curses.endwin()
        execute_cmd("echo df -h")

curses.endwin()
