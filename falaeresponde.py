import pyttsx3
import speech_recognition as sr

r = sr.Recognizer()

falador = pyttsx3.init()

with sr.Microphone() as s:
    r.adjust_for_ambient_noise(s)

    while True:
        #Aqui ele ouve:
        audio = r.listen(s)
        speech = r.recognize_google(audio, language='pt')
        print('Você disse: ' + speech)
        #Aqui ele fala:
        falador.say(speech)
        falador.runAndWait()
