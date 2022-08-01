import datetime
import json
import DateTime
import Speaker
import Listener
import WikiSearch
import SendMail
import ChromeSearch
import SystemFunction

def Greeting():
    Hour = datetime.datetime.now().hour
    if Hour >= 6 and Hour < 12:
        Speaker.Speak("Morning Boss")
    elif Hour >= 12 and Hour < 18:
        Speaker.Speak("Afternoon Boss")
    elif Hour >= 18 and Hour < 24:
        Speaker.Speak("Evening Boss")
    else:
        Speaker.Speak("Boss, why are you awake?")

if __name__ == "__main__":
    Greeting()
    while True:
        try:
            TextFromSpeech = Listener.ListenToYou().lower()
        except:
            print("Unable to recognise speech")
            TextFromSpeech = "Unable to recognise speech"
            
        if "time" in TextFromSpeech:
            Speaker.Speak("The current time is")
            DateTime.CurrentTime()
        elif "date" in TextFromSpeech:
            Speaker.Speak("The current date is")
            DateTime.CurrentDate()
        elif "wiki" in TextFromSpeech:
            Speaker.Speak("Searching...")
            Response = WikiSearch.Search(TextFromSpeech)
            Speaker.Speak(Response)
        elif "email" in TextFromSpeech:
            try:
                File = open("SMTPSettings.json")
                EmailInfo = json.load(File)
                To = EmailInfo["smtpto"]
                Speaker.Speak("OK, what would you like to say?")
                Content = Listener.ListenToYou().lower()
                Speaker.Speak("OK, attempting to send email now")
                SendMail.SendEmail(To, Content)
                Speaker.Speak("Email has been sent.")
            except Exception as Ex:
                Speaker.Speak("I was unable to send an email for you.")
                print(Ex)
        elif "google" in TextFromSpeech:
            Speaker.Speak("What should I Search for?")
            SearchContents = Listener.ListenToYou().lower()
            ChromeSearch.SearchChrome(SearchContents)
        elif "logout" in TextFromSpeech:
            SystemFunction.Logout()
        elif "shutdown" in TextFromSpeech:
            SystemFunction.Shutdown()
        elif "restart" in TextFromSpeech:
            SystemFunction.Restart()
        elif "remember" in TextFromSpeech:
            Speaker.Speak("What do you need me to remember?")
            ContentsToRemember = Listener.ListenToYou().lower()

        elif "quit" in TextFromSpeech or "goodbye" in TextFromSpeech or "goodnight" in TextFromSpeech:
            quit()
