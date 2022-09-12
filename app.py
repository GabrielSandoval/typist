import time
import random
import pyautogui

def random_between(lower, upper):
    return lower + random.random() * (upper - lower)

print("STARTING IN 5 SECONDS...")
time.sleep(5)

with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        print(line)
        for word in line.split():
            pyautogui.typewrite(list(word))
            pyautogui.typewrite(' ')
        pyautogui.typewrite('\n')
