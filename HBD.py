import subprocess
import keyboard
import time
import pyautogui
from textwrap import *
import pyperclip


subprocess.call(["cmd", "/c", "start", "/max", "C:\\Windows\\notepad.exe"])
time.sleep(1)



poo  = """
⠀⠀⠀⢼⡿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣾⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⣿⣿⣿⡟⠥⣛⠽⢢⣄⡀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⢿⠿⣿⣷⠊⡡⢚⡽⠛⣉⣷⣮⣀⢹⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣯⡴⢩⢖⡿⠟⠉⠀⢻⡍⠳⢶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⠉⠙⢷⠋⠀⠀⢠⣦⠀⠹⢶⣼⣧⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⢧⡀⠀⠀⠀⠀⠈⢹⣿⡾⠉⠻⣿⢿⠈⡎⠙⢷⡢⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢻⡀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⡼⢠⠇⠀⠀⠉⣿⢿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢳⡀⠀⠀⠀⠀⠀⠈⢿⣶⣋⢠⠎⠀⠀⠀⠀⣼⠸⡧⠤⢤⣀⣀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠸⣟⠓⠖⠒⢲⡶⠦⠤⣀⠙⡣⣿⣆⣠⢶⣿⣿⣿⣀⣗⢒⣶⠶⣋⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠉⠱⠦⣤⣝⠃⠹⣿⣿⣿⣿⣿⣏⣩⠥⠔⠒⠊⠈⣧⠀
⠀⠀⠀⠀⠀⠀⠀⢠⠇⢠⠀⠀⠀⠀⠀⡴⠋⠉⠓⠒⠛⠛⠛⠛⢣⡀⠀⠀⣀⡀⠤⠊⣽⠃
⠀⠀⠀⠀⠀⠀⠠⣯⡀⠀⠑⢤⣀⡀⢸⡀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣹⣿⣭⡤⠔⠒⠉⣽⣦
⠀⠀⠀⠀⠀⠀⠀⢸⠉⠓⠤⣀⡈⠉⠳⢽⠓⢒⣶⠶⡶⣴⠒⠋⠀⠀⠀⠀⢀⣠⠴⠊⣡⠟
⠀⠀⠀⠀⠀⠀⢀⡏⠀⠀⠀⠀⠀⠀⠈⠉⠉⠀⠀⢠⡇⢻⣿⣿⣿⣻⣏⣹⣥⡴⠶⠛⠁⠀
⠀⠀⠀⠀⠀⠀⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡀⠀⡇⠀⠀⠀⠀⢀⣀⡤⢄⣀⠀⠀⠀⢀⡇⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣰⠋⠉⠳⣼⡀⠀⠀⡖⠉⠀⠀⠀⠈⠙⠲⢤⣈⡜⢀⠴⠒⢢⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⡞⠁⣦⡀⠀⠀⠙⢦⣀⠹⣄⠀⠀⠀⠀⠀⠀⠀⠉⢲⠇⡰⠀⠘⡇⠀⠀⠀⠀⠀⠀⠀⠀
⢸⡇⠀⠈⢻⢤⣀⠀⢀⣈⡹⠖⠛⠢⠤⢄⣀⠀⠀⠀⠸⢠⡇⠀⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢣⣀⣠⠏⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⢤⡀⠸⠃⣀⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣀⣤⣴⣶⣖⣶⣶⣶⠶⠾⠿⠿⠿⠿⢿⣿⣿⡿⠿⢿⡿⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

cake = f"""
  ____________________________
| Here's a slice of cake for u! |
 ==================
         {chr(92)}
           {chr(92)}
             {chr(92)}              
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡖⠙⡢⠀⠀⠀⠀⠀⠀                                                         ⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⡿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠶⠞⠛⠿⣿⣿⡿⣿⣇⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠋⢠⠄⠀⠀⠀⠀⠈⠉⡉⠈⠛⢦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣤⠀⠀⠀⠀⠀⠻⢦⣴⣀⣀⠀⠀⠀⠀⢈⠁⣀⡄⠀⠹⣆⠀⠀⠀
⠀⠀⠀⠀⢰⠓⡄⠀⠀⠀⠀⠀⢸⡇⠉⠉⠙⠛⠛⠛⠛⠛⠉⠀⠀⠀⠹⣆⠀⠀
⢠⣒⣊⢍⣩⢙⣩⣍⡩⡇⠀⠀⢸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡀⠀
⣸⣀⣈⣁⣀⣉⣀⣀⣠⣇⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡆⠘⣇⠀
⠉⠉⠉⠛⠿⠻⣯⠉⠉⠉⠀⢀⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⢿⠀
⠀⠀⠀⠀⠀⠀⠈⢳⣄⠀⢠⡞⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⢸⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠋⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠁⠀⠘⣇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠀⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠟⠁⠀⠀⢻
"""


three = """
333333
    33
333333
    33
333333
"""

two = """
222222
     2
222222
2
222222
"""


one = """
1111
  11
  11
  11
111111
"""


big_cake = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡆⠀⣴⠂⠀⠀⡀⠀⠀⢀⣄⠀⠀⡀⢀⡀⠀⠀⣰⣷⠟⠀⠀⠀⠀⠀⠀⠀⢠⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⡄⠀⠀⠀⡇⢰⢃⡴⢀⡾⠁⢰⡇⣸⢣⠀⠀⢻⢸⠇⠀⢰⣿⠏⠀⠀⠀⠀⡀⠀⢀⡿⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣏⢧⠀⠀⠘⢧⡞⣾⢁⡟⠀⠀⡾⢀⣷⡏⠀⠀⢸⢸⠀⢠⣿⠇⠀⣴⠃⢸⢻⡇⠀⢸⢿⠇⣰⠆⢀⡴⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣤⡀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠙⣞⣧⡄⡀⠘⣹⢡⠞⠀⠀⢀⡇⠸⣼⠁⠀⠀⠸⠈⢀⣾⡟⢀⡾⠁⠀⢸⣾⠀⢠⡟⡞⣠⠋⣠⠞⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢨⡿⢦⡙⢷⣄⠀⠀⠀⠀⠀⠀⠹⣎⢘⣿⠈⠁⠀⠀⠀⠀⣸⠁⢠⠇⠀⠀⠀⠀⢠⡾⠉⠀⠞⠁⠀⠀⢸⡿⠀⠈⢱⠏⢁⡼⢫⠞⠁⠀⠀⠀⠀⠀⢀⡤⠄⣠⡴⠃⠀⠀
⠀⠀⠀⠘⢷⣄⠙⢦⡙⢦⡀⠀⢠⡆⠀⠀⠘⣾⠋⡇⠀⠀⠀⠀⠠⠿⠀⠈⠀⠀⠀⠀⣰⣻⠇⠀⠀⠀⠀⠀⠀⠈⠁⠀⢠⣿⡄⢘⡴⠋⠀⠀⠀⠀⠀⣠⡴⣋⡵⠛⠉⠀⠀⠀⠀
⡆⠀⠀⠀⠀⠉⠳⣄⡙⢶⡝⢢⣿⡇⠀⠀⠀⠹⣾⡇⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⢸⣧⡟⠀⠀⠀⠀⢰⡄⠀⠀⠀⠀⣾⣸⠃⠈⠀⠀⠀⠀⠀⣠⡞⠁⠀⢉⣀⣠⡤⠴⠶⠀⠀
⡀⠰⠶⣄⣀⠀⠀⠀⠙⢶⡀⢿⢨⡇⠀⠀⠀⢲⣮⢿⡇⠀⠀⠀⣾⢷⠀⠀⠀⠀⠀⣾⣿⡆⠀⠀⠀⠀⣼⢻⡄⠀⠀⢀⣽⣯⡆⠀⠀⠀⠀⢀⡼⣿⠀⠘⠉⠭⠶⠶⠶⠶⠿⠂⠀
⠛⠓⠦⠤⣌⣙⣓⠦⡄⠀⠀⢸⣿⣃⠀⠀⠀⢸⡇⢸⡇⠀⠀⠀⠻⣸⡇⠀⠀⠀⠀⡇⠀⡇⠀⠀⠀⠀⢷⣸⠇⠀⠀⠘⡟⢹⡇⠀⠀⠀⠀⣼⣴⠇⠀⢠⣀⣀⡀⠒⠒⠦⠤⠤⠄
⠀⠀⠀⠀⠀⢈⣉⣙⣲⡄⠀⣿⠿⢻⡄⠀⠀⢸⡇⢸⡇⠀⠀⠀⢤⣿⣧⡀⠀⠀⠀⡇⠀⡇⠀⠀⠀⠀⣮⣿⣤⠀⠀⠀⡇⢸⠃⠀⠀⠀⢸⠿⣽⡄⠀⠸⣍⡉⠉⠉⠛⠒⠒⠒⠶
⠐⠒⢒⣛⣯⣭⠭⠝⢋⡀⠀⢻⠀⢸⡇⠀⠀⢸⡇⢸⡇⠀⠀⠀⢸⠉⢿⡇⠀⠀⠀⡇⠀⡇⠀⠀⠀⠀⢻⠉⣿⠀⠀⠀⡇⢸⡆⠀⠀⠀⣿⠀⣿⠀⠈⠓⠮⣭⡓⠲⢦⣄⠀⠀⠀
⠈⠉⠉⠀⣀⣤⠶⠒⠉⠁⠀⢸⠀⢸⣇⠀⠀⠘⡇⢸⡇⠀⠀⠀⢸⠀⢸⡇⠀⣀⢀⡇⠰⣧⠀⠀⠀⠀⢼⠀⢻⠀⠀⠀⡇⢸⠇⠀⠀⢀⡇⢰⡿⠀⠀⠀⠀⠀⠉⠙⠶⢧⣦⣀⡀
⡤⠶⠚⠋⠁⠀⠀⠀⠀⠀⠀⢸⡄⠘⣿⣀⣠⣤⡇⢸⣷⠖⠚⠛⢻⠀⢸⡏⠉⠉⠉⡇⠀⣟⠉⠛⠛⠛⣿⠀⣸⠷⠶⣤⡇⢸⣆⡀⠀⢸⠁⣸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡼⣇⠀⣿⠀⠈⢿⣻⣾⣿⡷⠀⠀⢸⠄⢸⡇⠀⠰⣾⢿⣼⣟⣶⠀⠀⠀⢸⠀⢸⠀⢸⣜⡇⢸⣇⣉⠙⣿⠀⣿⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⠁⢀⣿⠀⣿⡀⠀⠀⠉⠉⠉⠀⠀⠀⢸⠀⢸⡇⠀⠀⠈⠛⠛⠛⠉⠀⠀⠀⢸⡄⢸⡀⠈⢷⣿⣿⣷⠛⢠⡿⢠⡇⠀⠙⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⡏⠀⠀⢿⡙⠶⣟⣿⠇⠀⠀⠀⠀⠀⠀⠀⣸⠀⢸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣽⣇⣸⣷⡀⠀⠀⠀⠀⢰⡾⣇⣼⣧⡄⠀⠈⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⠃⠀⠀⠈⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠻⣍⣳⣿⣯⡿⠀⠀⠀⠀⠈⠀⠀⠈⠹⣷⣭⣿⣾⠓⠀⠀⠀⠀⠘⠷⠮⠿⠾⠇⠀⠀⣹⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣼⡟⠀⣠⣤⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣀⠀⢠⡷⣄⢹⣇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠻⣶⡿⠋⢱⡏⠀⣀⣤⣤⣄⠀⠀⠀⠀⠀⠀⣠⣤⣤⣄⠀⠀⠀⠀⠀⣠⣶⣶⣴⡶⢶⡀⣠⣴⡶⠖⠲⣤⣄⠀⠀⢸⣿⠁⠙⠳⣼⠇⢻⡿⠛⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⡇⠀⠀⠉⠉⠉⠁⠀⠈⠳⣤⣄⣤⣶⠿⠋⠁⠀⠉⠳⣄⠀⢀⣴⡿⠃⠈⠉⠀⠈⠉⠉⠁⠀⠀⠀⠀⠉⠳⢦⣼⡿⠀⠀⠀⠀⠀⢸⣯⣧⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣾⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡅⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣆⠀⢀⡀⠀⠀⠀⠀⠀⢀⣴⣿⣿⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣀⣠⣴⢿⣿⣾⣝⡶⢤⣀⣀⡀⠀⠰⣖⠺⠻⣿⣤⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⠿⠘⢛⣿⣧⡤⢤⢤⣞⣿⠽⠿⠉⣿⠐⠛⠉⠉⠉⠉⠙⠛
⣤⠶⠛⠉⠀⠀⣼⣿⠀⠙⠻⢦⣯⣭⣉⣿⣿⣿⡇⣀⠻⡿⣯⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⡿⢻⡄⣀⣸⣷⡺⠿⠟⠛⠛⠁⠀⠀⠀⢻⢺⡇⠀⠀⠀⠀⠀⠀
⠁⠀⠀⠀⠀⠀⢻⡿⣆⠀⠀⠀⠀⠀⠉⠉⠉⠻⠟⠋⠳⢿⣧⣿⣝⢻⡖⠶⢶⠤⢤⣤⣤⡤⠤⠶⢖⣺⣋⣭⣗⣯⣾⣴⠋⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⣠⡾⣼⡷⠀⠀⠀⠀⠀⠀
⡿⠿⠛⠀⠀⠀⠀⠙⢿⡻⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠳⠿⠿⢿⣿⣶⡶⢶⣻⣿⡿⠿⣿⡿⠃⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡴⢞⡽⠾⠏⠀⠀⠀⠀⠀⠀⠶
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⢷⣭⣳⠦⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡤⢶⣛⣹⠿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣤⣤⡼⠿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⠴⠾⢯⣝⣿⣶⣤⠤⠤⢤⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣠⣤⠤⣤⣤⢴⠚⣛⣫⣭⡶⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣤⣀⣤
⠀⢿⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠓⠲⠦⠾⠻⢿⣯⡽⠿⢿⣭⡽⠛⠳⠶⠶⠚⠉⠉⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣩⡿⠃⠀
⠀⠀⠙⠓⢶⣶⣤⣤⣶⡿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⣀⠀⠀⠀⠀⣀⣠⣴⡶⠛⠉⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⢿⣤⣀⣀⣀⣀⣀⣀⣠⣶⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⢶⣿⠶⠶⠿⠟⠛⠉⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠛⠛⠉⠻⢶⣤⣄⣀⣀⣀⣀⠀⣀⣀⣠⣞⣿⠗⠀⠀⠀⠀⠀⠀⣠⣾⡟⠀⠀⠀⠀⠀⠀⢀⣠⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠛⠛⠛⠛⡻⣧⣤⣤⣤⣤⣤⡤⠴⢟⣛⢻⡦⠦⠤⠴⠶⢾⠛⠛⡉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

congrats = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡿⣿⣿⠿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⡟⠁⢀⣾⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⡏⣀⣴⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⣿⣿⣿⣧⣴⣶⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⠟⣻⣿⣿⠦⠀⠀⠀⣠⣤⣤⣄⣀⠀⠀⠀⠀⣀⡀⠀⠀⢀⣀⣀⡀⠀⠀⣄⣀⡀⠀⣠⣤⣤⡄⠀⠀⣾⣶⠀⠀⣿⣟⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⣿⣿⠃⢠⣿⣿⠃⠀⠀⢠⣾⣿⡿⠿⢿⣿⡄⠀⠀⠀⢹⣿⣿⣴⣿⣿⣿⣧⠀⠀⢹⣿⣿⣾⡿⠿⣿⣷⡀⠀⣿⣿⡆⠀⢻⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠻⠿⠃⢠⣿⣿⠏⠀⢀⣤⣿⣿⠏⠀⠀⣸⣿⡄⠀⠀⠀⢸⣿⣿⣿⠃⠈⣿⣿⡆⠀⢸⣿⣿⡿⠀⠀⣿⣿⡇⣠⣿⣿⣇⠀⣾⣿⣿⣿⣧⠀⠀⢀⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⠏⣠⣴⣿⠏⣿⣿⡄⠀⣠⣿⣿⡇⠀⣦⡄⢸⣿⣿⡇⠀⢠⣿⣿⣷⡾⠃⣿⣿⡇⠀⢠⣿⣿⣿⠟⠉⠿⣿⣿⡿⠇⢿⣿⣿⣠⣾⣿⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⠟⠁⠀⠘⢿⣿⣿⣿⣿⣿⣇⣼⣿⣩⣿⣿⣿⡇⣠⣿⡿⠟⠉⢠⣾⣿⣿⣇⣴⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠉⠉⠀⠻⣿⡿⠟⣽⣿⠛⣿⣿⡟⠛⠉⠀⠀⢀⣿⡏⢿⣿⣯⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡟⠀⣿⣿⡇⠀⠀⠀⠀⣸⣿⠃⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⡿⢹⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⣿⣿⠇⠀⠀⠀⠀⢿⣿⡄⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠄⢰⣿⡿⠁⣼⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣷⣴⣿⣿⠀⠀⠀⠀⠀⠸⣿⣷⣼⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⣴⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⠛⠁⠀⠀⠀⠀⠀⠀⠈⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⡿⠋⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⡀⠀⢠⣾⣿⣿⠟⠁⣸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⡈⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢼⣧⣠⣿⣿⡿⠁⣀⣼⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⡀⠀⠀⠀⠀⢰⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⣿⣿⣿⣿⣶⣿⠿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⢀⣴⣿⣿⢿⣿⣆⠀⠀⠀⢸⣿⡏⠈⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠕⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣼⣿⣿⡿⣄⣀⡀⠀⠀⠀⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⠀⠀⣼⣿⣿⠃⢠⣿⡟⠀⠀⠀⢸⣿⣇⠀⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠈⢺⣿⣶⣄⠀⠀⠂⠀⠀⠀
⢰⣿⣿⣿⣿⠿⢿⣿⣶⢶⣾⣿⠛⠁⠀⣠⣶⡄⠀⠀⠀⣤⣤⣾⣿⡏⠀⢰⣿⣿⢃⣴⣿⠟⠁⠀⠀⠀⠸⣿⣿⣼⣿⠃⠀⠀⠀⣀⣠⣄⠀⠀⢿⣿⡄⠀⢻⣿⣿⣷⡀⠀⠀⠀⠀
⢿⣿⡿⠉⠀⠀⠀⣿⣿⣾⣿⣿⠉⠁⠙⢿⣿⣇⣀⣀⡀⢉⣿⣿⣿⢿⡇⣸⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠀⢻⣿⣿⠁⠀⠀⢠⣿⡿⠛⢿⣇⠀⠘⣿⣷⡀⠈⣿⣿⣿⣿⡄⢀⣾⡷
⣿⣿⣦⣀⣀⣠⣾⣿⣿⣿⣿⠇⢀⣀⠀⣾⡿⢻⣿⡿⠀⢠⣿⣿⠋⠀⠘⣿⣿⣿⣾⣿⣿⣶⠄⠀⠀⣠⣤⣭⣿⣿⡄⠀⢠⣿⣿⠁⠀⢸⣿⡆⠀⣿⣿⣷⣾⡿⠠⢻⣿⣿⣾⡿⠁
⠀⠈⠛⠿⠿⠿⠟⠋⣿⣿⣏⣴⣿⣟⣼⠟⠀⣼⣿⠃⠀⢸⣿⣿⠀⠀⠀⢹⣿⣿⡟⢠⣿⡟⠀⠀⣾⣿⠟⠙⠻⣿⣿⣄⣾⡿⣿⣧⣠⣼⣿⣷⣽⣿⠀⠉⠉⠀⠀⠈⣿⣿⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⡿⣿⣿⠏⠀⢠⣿⡿⠀⣴⣾⣿⡿⠀⣀⣴⣿⣿⣿⠡⣸⣿⠇⢀⣴⣿⣿⡀⡀⢠⣿⡿⣿⡟⠀⠊⠛⡛⠛⠙⠛⠛⠃⠀⠀⠀⠀⢠⣿⣿⣿⣿⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠙⠃⠀⠀⢸⣿⣧⣾⡿⢹⣿⣿⣶⣿⡿⠁⠀⠀⠀⣿⣿⣠⣿⠟⠈⠻⠿⠿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⣀⣿⣿⠈⣿⣿⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠿⠋⠁⠀⠻⠿⠟⠁⠀⠀⠀⠀⠀⠙⠿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⢀⣿⣿⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠘⣿⣿⣿⣿⡿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠄⢀⠀⠈⠛⠛⠛⠁⠀⠀
"""


hbd = """
o * ‘ ‘’ ’ * o .             . o * ‘ ‘’ ’ * o .             . o * ‘ ‘’ ’ * o .             . o * ‘ ‘’ ’ * o              
                   ‘ * – * ’                       ‘ * – * ’                       ‘ * – * ’                      
   : : : : : : : :    A__A    : * : * : * : * : * : * : * : * : * . * . * . * . * . * . * . * . * . * . 
   : : : : : : :    (   ‘ V ‘ )    : : Happy Birthday Gracie!! : : : : : : : : : : : : : : :
   : * : * : * :   (   (‘’)(‘’)     * : * : * : * : * : * : * : * : * : * : * : * : * : * : * : * : * : * :
* - . , . - * - . , . - * - . , . - * - . , . - * - . , . - * - . , . - * - . , . - * - . , . - * - . , . - 
o * ‘ ‘’ ’ * o .             . o * ‘ ‘’ ’ * o .             . o * ‘ ‘’ ’ * o .             . o * ‘ ‘’ ’ * o     
                   ‘ * – * ’                       ‘ * – * ’                       ‘ * – * ’                                      
"""


text = """
Halo Gracie! Diz iz mei Joho da kimmy kim!
Thank you for being a muy muy demasiado goodie sister and an amazing person!
I hope you have a happi birthday!
Heres your birthday cake!!
Wait let me get the cake for ya
"""



respect = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⢠⠀⢠⠀⢀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⡄⠀⠀⠀⢰⠀⠀⡇⡆⢸⠀⢸⠀⣸⢀⡀⠀⢀⡔⠀⢀⡔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⠀⠀⠘⢦⡀⠀⢸⡇⠀⣿⣧⢸⠀⡎⠀⡇⣸⠁⢠⠏⠀⡠⢋⠀⢀⡔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣄⠈⠑⢄⡀⠈⢳⣄⢈⣇⣈⣿⣿⣸⣂⣇⣸⢡⠇⢠⠏⢀⠞⣡⠊⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠦⣈⠙⢦⣀⠙⢦⣤⣿⣿⣿⣿⣿⣿⣟⠋⠉⠛⠻⣴⠋⡴⢋⡞⢁⠜⠁⢀⠔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⢄⡘⢧⣄⡘⢧⣼⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠘⢿⣠⡟⣠⠟⢀⡸⠃⠀⡠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠦⣄⡉⠲⢬⡻⣿⣿⣿⣿⠛⢿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠈⢻⡶⢁⡴⠋⢀⡴⠋⠀⣀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠉⠓⠦⣀⡉⠓⠶⣭⣿⣿⠋⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⡆⠀⠀⠈⣗⠉⣠⠖⠁⣀⠴⠋⢀⠀⠀⡠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠉⠓⠢⢄⣉⠳⢶⣤⣽⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⡄⠀⠀⢸⠟⣁⡴⠊⢁⡤⠚⣁⠴⠋⠀⠀⡠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠉⠓⠲⢤⣈⡉⠲⢮⣽⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣧⠀⠀⢸⠟⣁⣤⠞⣉⡴⠚⠁⢀⣠⠖⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠒⠦⢤⣈⠙⠛⠶⣶⣿⣿⣗⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⡄⠀⠘⡿⣋⣴⠞⠉⢀⣤⠖⠉⣀⠴⠊⢀⡠⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠲⠤⣄⡀⠀⠀⠉⠓⠲⢤⣍⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⢻⣿⣇⠀⡄⠹⣏⣡⣴⠞⠋⣀⡴⠚⢁⡠⠖⠉⢀⡴⠊⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠒⠲⢤⣉⡙⠓⠶⢶⣤⣄⣈⠙⣿⣿⣿⣷⡤⠤⠔⠋⠀⠀⢀⡿⣿⡄⢰⠀⠈⠻⣄⣴⠚⣁⣤⠞⠉⠀⣠⠖⠁⢀⡤⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠐⠲⠤⣄⡀⠀⠀⠉⠙⠒⠦⣬⣉⢛⣿⢻⣿⣿⣿⣧⣀⣀⣠⠤⠖⠋⠀⠸⣿⡜⡆⠀⠀⠀⠙⠻⣏⠁⣠⡴⠋⢀⡤⠞⠁⣀⡴⠊⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠒⠦⢤⣀⡀⠉⠙⠓⠶⣶⣤⣴⣠⡿⠋⠁⠀⣿⡏⠁⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣧⠀⠀⠀⠀⠀⠀⠙⠧⣤⠞⠋⣠⡴⠊⠁⣀⠤⠂⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠤⢤⣀⠀⠀⠉⠙⠲⢦⣤⣤⣩⡿⠋⠀⠀⠀⠀⢻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠃⠹⣿⡄⠀⠀⠀⠀⠀⠀⠀⠙⢶⠟⢁⣠⡶⠚⢁⡠⠖⠈⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠉⠒⠒⠦⢤⣤⣈⣉⣻⡿⠃⠀⠀⠀⠀⠀⢸⣷⠀⢠⣀⡀⠀⠀⠀⠀⠀⢸⠀⠀⣻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⠾⢋⣡⠴⠊⢁⡠⠴⠂⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠂⠠⠤⠤⣀⣀⡈⢹⡿⠁⠀⠀⠀⠀⠀⠀⢸⣿⢀⣟⡹⡷⡀⠀⠀⠀⠀⡾⣀⣰⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣗⣋⣤⠶⠚⠉⣀⡠⠄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠉⠙⠓⠲⠦⠤⣤⣤⣄⣉⡿⠁⠀⠀⠀⠀⠀⠀⢠⣿⡇⣾⣿⠰⡘⣽⣄⠀⠀⢀⡇⢠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡏⣀⡤⠔⠋⢁⣠⠤⠂⠀⠀⠀⠀
⠀⠀⢀⣀⡁⠛⠒⠲⠤⠤⢤⣄⣉⣿⠃⠀⠀⠀⠀⠀⠀⣠⣿⣿⢱⡟⣏⠃⠃⠀⢸⡀⠀⣼⢀⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣡⡤⠶⠛⢉⣀⠤⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠉⠉⠛⠳⠶⢶⣦⣤⣼⠇⠀⠀⠀⠀⠀⠀⣰⣿⣿⣡⣼⣇⢹⠀⠀⠀⢸⣷⣴⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣅⡤⠔⠊⠉⢀⣀⡀⠀⠄⠀⠀
⠀⠀⠀⠀⠀⠐⠒⠂⠤⠤⢤⣩⡏⠀⠀⠀⠀⠀⠀⣼⣿⠟⢻⠁⣿⢿⡈⢧⠀⠀⣰⡿⡇⢹⠛⠿⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠴⠖⠚⠉⣉⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠉⠉⠛⠒⠶⠦⢤⣤⣾⠀⠀⠀⠀⠀⠀⣺⣿⠃⠀⢸⡀⠸⡄⢹⣶⣷⡋⠁⢀⠇⢸⡇⠀⢻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡗⠒⠋⣉⣀⣀⠤⠤⠀⠀⠀
⠀⠀⠀⠀⠐⠒⠤⠤⠤⣀⣸⠃⠀⠀⠀⠀⠀⠀⢿⡇⠀⠀⠀⢳⡀⠹⠔⢻⣿⠳⣄⠞⠀⡾⠀⠀⠸⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⠛⠋⢉⣀⣀⡀⠀⠀⠀⠀
⠀⠉⠉⠐⠒⠒⠶⠶⢶⣶⡟⠀⠀⠀⠀⠀⠀⠀⢸⣧⠀⠀⠀⠀⠳⣄⠀⢸⣷⠀⠙⠀⡼⠁⠀⠀⠀⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠋⣋⣉⣀⠤⠤⠐⠀⠀⠁
⠀⠀⠠⠤⠤⠤⢤⣄⣠⣸⡇⠀⠀⠀⠀⠀⠀⠀⠈⣿⠀⠀⠀⢀⣠⣾⣿⣿⣿⡶⢶⣾⡁⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣏⣉⣀⠠⠄⠄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⢠⡞⠉⢰⣿⣿⣿⣿⣷⢸⣿⡟⢳⣦⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣧⣴⣤⣤⣤⣤⣤⣤⡄⠀
⠀⠀⠀⠀⠉⠉⠉⠉⠛⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⡟⠉⠀⢠⣿⣿⣿⣿⣿⣿⠸⣿⡇⠈⣿⠉⠲⢤⣸⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣟⣋⣉⣉⣉⡀⡀⠀⠀⠀
⠀⠀⠐⠒⠒⠒⠒⠒⠒⢺⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡇⠀⠀⣿⣿⣿⡏⣿⣿⣿⠦⣿⡇⠀⣿⠀⠀⠀⠈⢻⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣧⣤⣤⣤⡤⠤⠤⠤⠤⠀
⠀⠀⠀⠤⠤⠤⠴⠶⠶⠾⠃⠀⠀⠀⠀⠀⠀⠀⢠⣿⡇⠀⠀⠀⠛⠻⠁⠉⠿⠿⠀⢿⣧⠀⣿⠀⠀⠀⠀⠀⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠧⠤⠤⠄⠀⠀⠀⠐⠒⠂
⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠐⠠⠀⠀⠈⠀⠁⠀⠁⠈⠁⠈⠈⠀⠀⠀⠀
_________________________________________________________________________________
⠀⠀⣀⣀⠀⠀⣀⣀⠀⢀⣀⠀⣀⣀⠀⢀⣀⣀⠀⠀⣀⣀⢀⣀⣀⡀⠀⠀⣀⣀⡀ ⢀⣀⡀⠀  ⠀⣀⠀⠀ ⠀⣀⣀⠀ ⡀⢀⣀⣀⠀⠀
⠀⠀⡇⠀⡇⠀⡇⠀⠐⣇⠀⠀⡇⠀⢱⢸⠀⠀⢠⠋⠀⠀⠀⢸⠀⠀⠀⠀⡞⠀⠀⠀ ⢸⠀⢹⠀  ⢀⠛⡄⠀ ⡎⠀⠀⠀ ⡇⢸⠀⠀⠀⠀
⠀⠀⡏⠙⡄⠀⡏⠉⠀⠈⠑⡄⡟⠚⠁⢸⠉⠉⠸⡀⠀⠀⢸⠀⠀⠀⣇⠀⠉⡇  ⢸⠉⢇⠀  ⡼⠤⢷⠀⡇⠀⠀⠀  ⡇⢸⠉⠉⠀⠀
⠀⠀⠃⠀⠘⠀⠓⠒⠀⠒⠊⠀⠃⠀⠀⠘⠒⠒⠀⠙⠒⠂ ⠘⠀⠀⠀⠀⠈⠒⠒⠁⠘⠀⠈⠒ ⠁⠀⠀⠃⠈⠒⠒⠀   ⠃⠘⠒⠒⠀⠀
_________________________________________________________________________________⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⢀⣀⠀⠀⠀⠀⢀⣀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡿⠋⠙⢷⣄⠙⠛⠀⠀⠘⠛⠉⣰⡿⠙⠻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠈⠛⠷⣦⣤⣤⣤⡶⠟⠋⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡟⠀⠀⠀⠀⣠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡄⠀⠀⠀⠹⣿⣿⣿⣿
⣿⣿⣿⡿⠀⠀⠀⠀⣼⠏⠀⠀⢀⣤⣴⣶⣤⣄⠀⠀⠈⢿⣆⠀⠀⠀⢹⣿⣿⣿
⣿⣿⣿⠇⠀⠀⠀⣼⠏⠀⠀⣴⠟⠁⢸⡇⠈⠙⣷⠀⠀⠀⢻⡆⠀⠀⠀⣿⣿⣿
⣿⣿⣿⠀⠀⠀⣴⣿⣶⣶⣶⣿⠀⠀⢸⡇⠀⠀⢸⣶⣶⣶⣾⣿⡄⠀⠀⢹⣿⣿
⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿
⣿⣿⣿⣦⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣼⣧⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣾⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣼⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
"""

final ="""
And have lots of fun todai!
Let me show respect before I end this program
"""


# Define a function for repetitive typing with a given delay
def type_text(text, delay):
    for char in text:
        pyautogui.typewrite(char)
        time.sleep(delay)

# Type text with small delay
type_text(text, 0.001)

time.sleep(1)  # Give some time to focus on the input field

# Type 'poo'
keyboard.write(poo)
time.sleep(5)

# Repeat a block of actions with increasing indentation for 'poo'
for i in range(12):
    poo = indent(poo, '                 ')
    pyperclip.copy(poo)
    time.sleep(.1)
    pyautogui.press("backspace")
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(.2)

# Type 'three', 'two', 'one' with a delay
for item in [three, two, one]:
    pyperclip.copy(item)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)

# Type 'big_cake', 'congrats', 'hbd', 'cake' with a delay
for item in [big_cake, congrats, hbd, cake]:
    keyboard.write(item)
    time.sleep(5)




# Type final with very small delay
type_text(final, 0.0001)

time.sleep(2)
keyboard.write(respect)
