import pyttsx3

def Speak(Audio):
    Engine = pyttsx3.init()
    Engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0')
    Engine.say(Audio)
    Engine.runAndWait()