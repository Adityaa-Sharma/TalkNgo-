import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Capture audio from the microphone
with sr.Microphone() as source:
    print("Please wait. Calibrating microphone...")
    # Listen for 5 seconds and create the ambient noise energy level
    recognizer.adjust_for_ambient_noise(source, duration=5)
    print("Microphone calibrated")

    while True:
        print("Listening...")
        audio = recognizer.listen(source)
        
        try:
            # Recognize speech using Sphinx
            text = recognizer.recognize_sphinx(audio)
            print("You said: " + text)
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))
