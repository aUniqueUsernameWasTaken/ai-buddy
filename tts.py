from gtts import gTTS

def texttospeach(text, counter):
    tts = gTTS(text, slow=False)
    tts.save("outputs/output"+str(counter)+".mp3")