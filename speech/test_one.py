import speech_recognition as sr
r = sr.Recognizer()
hallo = sr.AudioFile('/Users/Peregrine/Downloads/Downloads - unknown album/hallo.flac')
with hallo as source:
    audio = r.record(source)
print(r.recognize_google(audio))