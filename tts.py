from gtts import gTTS

def texttospeach(text):
    tts = gTTS(text)
    tts.save("output.mp3")