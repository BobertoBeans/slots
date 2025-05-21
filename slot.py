import curses
import random
import keyboard

screen = curses.initscr()

curses.curs_set(0)

screen.refresh

def slot():
  window= curses.newwin(100,100,10,50)
  window.addstr(1,2, '║')
  window.addstr(2,2, '║')
  window.addstr(3,2, '║')
  window.addstr(4,2, '║')
  window.addstr(5,2, '║')
  window.addstr(1,24, '║')
  window.addstr(2,24, '║')
  window.addstr(3,24, '║')
  window.addstr(4,24, '║')
  window.addstr(5,24, '║')
  window.addstr(6,2, '╚')
  window.addstr(6,24, '╝')
  window.addstr(0,2, '╔')
  window.addstr(0,24, '╗')
  line = '═'*21
  window.addstr(0,3, line)
  window.addstr(6,3, line)
  window.addstr(3, 12, '#')
  window.addstr(3, 13, '#')
  window.addstr(3, 14, '#')
  balance = 1000
  window.addstr(8, 6, "Balance:$" + str(balance))
  window.addstr(9, 3,  "Press space to start!")
  window.refresh()
  x=0
  y=0
  z=0
  bool=True

  while True:
    keyboard.read_key()
    if keyboard.is_pressed('space'):
        while(bool==True):
         x=random.randint(1,9)
         window.addstr(3,12, str(x))
         window.refresh()
         curses.napms(250)
         if keyboard.is_pressed('esc'):
           bool=False
           continue
    if keyboard.is_pressed('space'):
        while(bool==True):
         x=random.randint(1,9)
         window.addstr(3,13, str(x))
         window.refresh()
         curses.napms(250)
         if keyboard.is_pressed('esc'):
           bool=False
           continue
slot()