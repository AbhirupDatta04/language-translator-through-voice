import speech_recognition as s
from googletrans import Translator
from gtts import gTTS 
from playsound import playsound

listener=s.Recognizer()


def lan_trans():
    with s.Microphone() as input:
        print("Listening.....")
        input_given = listener.listen(input)
        texts = listener.recognize_google(input_given)
        translator= Translator()    
        trans=translator.translate(texts,dest='bn')
        print(trans.text)
        voice = gTTS(text = trans.text,long='bn')
        voice.save("lang.mp3")
        playsound("lang.mp3")
        print(texts)