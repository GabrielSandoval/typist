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
            pyautogui.typewrite(list(word), interval=random_between(0.01, 0.03))
            time.sleep(random_between(0.03, 0.05))
            pyautogui.typewrite(' ')
        pyautogui.typewrite('\n')
        time.sleep(random_between(0.1, 0.5))
