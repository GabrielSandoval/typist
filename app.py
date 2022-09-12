import time
import random
import pyautogui

def random_between(lower, upper):
    return lower + random.random() * (upper - lower)

print("STARTING IN 5 SECONDS...")
time.sleep(5)

with open('test.txt') as f:
    lines = f.readlines()
    for line in lines:
        for word in line.split():
            pyautogui.typewrite(list(word), interval=random_between(0.05, 0.1))
            time.sleep(random_between(0.1, 0.2))
            pyautogui.typewrite(' ')

        pyautogui.typewrite('\n')
        pyautogui.typewrite('\n')
        time.sleep(random_between(0.4, 1))
