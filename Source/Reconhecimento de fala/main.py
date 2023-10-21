import speech_recognition as sr

rec = sr.Recognizer()

with sr.Microphone() as mic:
    rec.adjust_for_ambient_noise(mic)
    print("Gravando....")
    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language="pt-BR")
    print(texto)

with open('../Hack_OLX/Source/Reconhecimento de fala/saida.txt', 'w') as arquivo:
    arquivo.write(texto)