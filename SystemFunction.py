import os

def Shutdown():
    os.system("shutdown -s -t 0")
    
def Logout():
    os.system("shutdown -l")

def Restart():
    os.system("shutdown -r -t 0")