from gtts import gTTS

def texttospeach(text, counter):
    tts = gTTS(text)
    tts.save("outputs/output"+str(counter)+".mp3")