#This program checks if Uplay stops downloading and restarts the program after a short delay

import pyautogui
import os
import time
import datetime

running = True
interval = 600 #Interval between checks

DLFails = 0 #Number of download failures
DLThreshold = 20 #Number of download failures to end program.
iconFailures = 0 #Number of icon failures. Resets to 0 once the icon is found
iconThreshold = 100 #Number of failures locatin the icon before exiting the while loop
UPlayInstallDir = "E:/Program Files (x86)/Ubisoft/Ubisoft Game Launcher/Uplay.exe"

print("This was started at " + str(datetime.datetime.now()))
while running:
    dlStopped = pyautogui.locateOnScreen('0B-S.PNG')
    dlStoppedTwo = pyautogui.locateOnScreen('0B-S2.PNG')
    if dlStopped != None or dlStoppedTwo != None:
        print("Download Stopped!")
        print("The current time is " + str(datetime.datetime.now()))
        DLFails = DLFails + 1
        print("Number of failures: " + str(DLFails))
        if DLFails > DLThreshold:
            print("Reached failure threshold. Program will terminate")
            running = False
            break #Something better?
        os.system("taskkill /IM upc.exe") #Kill Uplay program and wait
        time.sleep(600)
        os.system(UPlayInstallDir) #Restart Uplay
        dlIcon = pyautogui.locateOnScreen('DLICON.PNG')
        while dlIcon == None:
            print("Couldnt locate DLICON")
            time.sleep(30)
            dlIcon = pyautogui.locateOnScreen('DLICON.PNG')
            iconFailures = iconFailures + 1
            if iconFailures > iconThreshold:
                dlIcon = 1
                running = False
                print("Icon failure exceeded threshold.")
                break
        iconFailures = 0
        x, y = pyautogui.locateCenterOnScreen('DLICON.PNG')
        pyautogui.click(x, y)
        print("Awaiting next falure. Time interval: " + str(interval) + " seconds")
    time.sleep(interval)
