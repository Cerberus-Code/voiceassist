import pyttsx3
import speech_recognition as sr
# Importing required modules

class AI():
    __name = ""
    __skill = []


    def __init__(self, name=None):
        self.engine = pyttsx3.init()
        # Define the Text-to-Speech engine
        voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", voices[5].id)
        # Set the TTS voice
        name = voices[5].name
        # Set the TTS name
        self.r = sr.Recognizer()
        # Define the recognizer for Speech Recognition
        self.m = sr.Microphone()
        # Define the microphone for Speech Recognition

        # for voice in voices:
        #     print(voice, voice.id, voice.name)


        if name is not None:
            self.__name = name
        # Ensures name definition

        # print("I'm listening.")

        # with self.m as source:
        # # Define microphone as audio source
        #     self.r.adjust_for_ambient_noise(source)
        #     # Adjust microphone audio for ambient noise

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        print("My name is {self.__name}")

        self.__name = value
    # Name setter

    def say(self, content):
        self.engine.say(content)
        # Tells TTS Engine what to say
        self.engine.runAndWait()
        # Tells TTS Engine to run

    def listen(self):
        phrase = ""

        print("Say something.")

        with self.m as source:
        # Define microphone as audio source
            try:
                audio = self.r.listen(source)
                # Try detecting audio from source
                print("Audio caught.")
            except:
            # Cannot detect audio from source
                print("No audio detected.")

        try:
            phrase = self.r.recognize_google(audio, show_all=False, language="en_US")
            # Try to detect language from audio
            phrase = str(phrase)

            print("You said, \"{phrase}\".")
        except:
            print("I couldn't catch that.")

        return phrase 

