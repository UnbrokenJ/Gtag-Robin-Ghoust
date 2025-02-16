#Robin's AI.
#Uses python.
#An AI, with help from AI!
import pyautogui
import time
import random
import os

Codes=["Robin", "Robin666"] #Defines what codes Robin can join
running = True

def Start_Gtag():
    Gtag=("") #Insert Gotilla Tag's path here
    os.startfile(Gtag)

def hold_key_for_duration(key, hold_time):
        start_time = 1
        while start_time < hold_time: # Release the key after the specified time
            start_time+=1
            pyautogui.keyDown(key) 

Start_Gtag

while running:
    print("Starting Robin (CRTL C to Quit)")

    #Join code sequence
    pyautogui.typewrite(random.choice(Codes))

    #Movment Sequence
    hold_key_for_duration('up', 5)
