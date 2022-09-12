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
            pyautogui.typewrite(list(word), interval=random_between(0.025, 0.05))
            time.sleep(random_between(0.05, 0.1))
            pyautogui.typewrite(' ')
        pyautogui.typewrite('\n')
        time.sleep(random_between(0.5, 1))
