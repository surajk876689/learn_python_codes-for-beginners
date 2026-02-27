import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("hello i am suraj choudhary")
engine.runAndWait()
'''this code will convert the text "hello i am suraj choudhary" into speech and play it.
You can change the text to whatever you want to convert into speech.'''