import subprocess
import keyboard
import time
import pyautogui
import pyperclip
from message import *
from textwrap import indent



def open_notepad():
  subprocess.call(["cmd", "/c", "start", "/max", "C:\\Windows\\notepad.exe"])
  time.sleep(1)



# Repetitive typing with a given delay
def type_text(text, delay):
    for char in text:
        pyautogui.typewrite(char)
        time.sleep(delay)




  

  
def CreatePoo():
    keyboard.write(poo)
    time.sleep(5)
    return poo

def MovePoo(poo):
    # Repeat a block of actions with increasing indentation for 'poo'
    for i in range(12):
        poo = indent(poo, '                 ')
        pyperclip.copy(poo)
        time.sleep(.1)
        pyautogui.press("backspace")
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(.2)

def StartCountDown():
    # Type 'three', 'two', 'one' with a delay
    for item in [three, two, one]:
        pyperclip.copy(item)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(1)


def SurpriseGracie():
    # Type 'big_cake', 'congrats', 'hbd', 'cake' with a delay
    for item in [big_cake, congrats, hbd, cake]:
        keyboard.write(item)
        time.sleep(5)


def ShowRespect():
    time.sleep(2)
    keyboard.write(respect)
