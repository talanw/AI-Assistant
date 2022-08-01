import datetime
import Speaker
#could do with showing this as a AM or PM with some better formatting of the words
def CurrentTime():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    Speaker.Speak(Time)

#need to make this more user friendly.
def CurrentDate():
    Year = int(datetime.datetime.now().year)
    Month = int(datetime.datetime.now().month)
    Day = int(datetime.datetime.now().day)
    Speaker.Speak(Day)
    Speaker.Speak(Month)
    Speaker.Speak(Year)