import keyboard as kb
import os

while True:
    if kb.is_pressed('win'):
        os.system('shutdown /s /t 3')
    if kb.is_pressed('ctrl+enter'):
        os.system('shutdown /a')
        break