# main
import voice_recognition
import tts
import audioplaymodule
import mistral
import os

count = 0

stuffaskedbefore = {
    "question": "What are you?",
    "answer": "Im Mistral AI!"
}

while True:
    if os.path.exists("audio.wav"):
        os.remove("audio.wav")
    if os.path.exists("audio_converted.wav"):
        os.remove("audio_converted.wav")

    text = voice_recognition.dostuff()
    aiResponseText = mistral.aishit(text, stuffaskedbefore=stuffaskedbefore)

    try:
        tts.texttospeach(aiResponseText, counter=count)
    except TypeError:
        print("remember to check if you entered a mistral AI API key in mistral.py")   

     
    audioplaymodule.play("outputs/output"+str(count)+".mp3")
    
    count += 1
    stuffaskedbefore.update({f"question{count}": text, f"answer{count}": aiResponseText})
