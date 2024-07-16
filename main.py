# main
import voice_recognition
import tts
import audioplaymodule
import mistral

count = 0

while True:
    print("remember to check if you entered a mistral AI API key in mistral.py")
    tts.texttospeach(mistral.aishit(voice_recognition.dostuff()), counter=count)
    
    audioplaymodule.play("outputs/output"+str(count)+".mp3")
    
    count += 1

