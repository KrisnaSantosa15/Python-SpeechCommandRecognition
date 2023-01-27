# Krisna Santosa - Python SpeechRecognition - 13 January 2021
import os
import pyttsx3
import speech_recognition as sr

class shutdownSR:
    # Method to take choice commands as input
    def takeCommands(self):
        # using recognizer and microphone Method for input voice
        # Commands
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("LISTENING....")
            # number of seconds of non-speaking audio before
            # a pharse is considired complete
            r.pause_threshold = 0.7
            audio = r.listen(source)
            # Voice input is identified
            try:
                # Listening voice commands in american english
                print('Recognizing...')
                Query = r.recognize_google(audio, language='en-in')

                # Displaying voice command
                print("The query is printed'", Query, "'")

            except Exception as e:
                # Displaying exception
                print(e)
                # Handling exception
                print("say that again sir")
                return "None"

        return Query

    def Speak(self, audio):
        # Constructor call for system
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('Voice', voices[1].id)
        engine.say(audio)
        engine.runAndWait()

    # Method to self Shutdown System

    def quitSelf(self):
        self.Speak("Do you want to switch off the computer sir?")
        # Input voice command
        take = self.takeCommands()
        choice = take
        if "yes" in choice:
            print("Shutting down the computer...")
            self.Speak("Shutting the computer")
            os.system("shutdown /s /t 30")

        if "no" in choice:
            print('Thank you sir')
            self.Speak("Thank u sir")

# Driver code
if __name__ == "__main__":
    halo = shutdownSR()
    halo.quitSelf()
