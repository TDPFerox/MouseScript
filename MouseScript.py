import pyautogui as pg
import time
import keyboard

i = 0
print('Press the "S" Key to stop the Script')
print('The Cursor must be in the console to recognize pressing "S"')
time.sleep(3)
while i == 0:
    pg.moveRel(0, 1)
    pg.moveRel(0, -1)
    if keyboard.is_pressed("S"):
        print('MouseScript Stopped')
        break
input('Please press any key to continue')
