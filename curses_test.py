import time
import curses
from curses.textpad import Textbox, rectangle

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    i = 0
    while True:
        stdscr.clear()
        while stdscr.getch() != 10:
            stdscr.addstr(1, 1, str(stdscr.getch()))
        stdscr.refresh()
        time.sleep(0.1)
# Left 260
# Right 261
# Backspace 263
# Enter 10

def textBox(stdscr):
    stdscr.addstr(0, 0, "Enter IM message: (hit Ctrl-G to send)")

    y = 5
    x = 10
    h = 5
    w = 30
    editwin = curses.newwin(h,w, y,x)
    rectangle(stdscr, y-1,x-1, y+h, x+w)
    stdscr.refresh()

    box = Textbox(editwin)

    # Let the user edit until Ctrl-G is struck.
    box.edit()

    # Get resulting contents
    message = box.gather()
    return message

print(curses.wrapper(textBox))
