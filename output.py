import pyttsx3
#`145`
# engine = pyttsx3.init()
# rate = engine.getProperty('rate')
# voices = engine.getProperty('voices')
# engine.setProperty('rate', 200)
# engine.setProperty('voice', voices[9].id)
# engine.say("Are u the strongest because you are gojo satoru, or are you gojo satoru because you are the strongest")
# engine.runAndWait()



def read_text(response_text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(response_text)
    engine.runAndWait()
