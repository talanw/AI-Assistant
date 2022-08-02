import os
import pyautogui
import psutil

def Shutdown():
    os.system("shutdown -s -t 0")
def Logout():
    os.system("shutdown -l")
def Restart():
    os.system("shutdown -r -t 0")
def Screenshot():
    ScreenshotImg = pyautogui.screenshot()
    ScreenshotImg.save("screenshot.png")
def SystemUsage():
    CPUUsage = str(psutil.cpu_percent())
    BatteryCharge = psutil.sensors_battery()
    DiskUsage = psutil.disk_usage()
    print(DiskUsage.percent)
    return("The CPU usage is " + CPUUsage + " percent. The battery charge is at " + str(BatteryCharge.percent) + " percent")