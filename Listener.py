import speech_recognition as SR

def ListenToYou():
    Speech = SR.Recognizer()
    with SR.Microphone() as Source:
        print("Listening")
        Speech.pause_threshold = 1
        AudioResponse = Speech.listen(Source)
    
    try:
        RecognisedText = Speech.recognize_google(AudioResponse, language='en-gb')
        print(RecognisedText)
    except Exception as Ex:
        print("Something went wrong trying to recognise speech: " + Ex)
        return(False)
    return(RecognisedText)