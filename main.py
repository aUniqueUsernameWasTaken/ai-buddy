# main
import voice_recognition
import tts
import audioplaymodule
import mistral
import os

count = 0

while True:
    if os.path.exists("audio.wav"):
        os.remove("audio.wav")
    if os.path.exists("audio_converted.wav"):
        os.remove("audio_converted.wav")

    print("remember to check if you entered a mistral AI API key in mistral.py")
    tts.texttospeach(mistral.aishit(voice_recognition.dostuff()), counter=count)
    
    audioplaymodule.play("outputs/output"+str(count)+".mp3")
    
    count += 1

