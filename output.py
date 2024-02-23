import pyttsx3

def read_text(response_text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(response_text)
    engine.runAndWait()
