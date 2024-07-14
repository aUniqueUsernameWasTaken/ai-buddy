# main
import voice_recognition
import tts
import audioplaymodule

count = 0

while True:
    try:
        tts.texttospeach(voice_recognition.dostuff())
        audioplaymodule.play("output.mp3")
    except:
        print("couldnt record audio,")
        print("error: \n"+ Exception)

