#!/bin/env/python
import speech_recognition as sr
import scipy.io.wavfile as wav
import sounddevice as sd
import subprocess
import os

def dostuff():
    # Record the audio, 44100 = the sample rate and 5 is the duration of the recording
    print("Recording audio for 5 seconds...")
    audio = sd.rec(int(5*44100), samplerate=44100, channels=1)
    sd.wait()

    print("Saving audio...")
    wav.write('audio.wav', 44100, audio)
    print("Audio saved successfully")

    command = ["ffmpeg", "-i", 'audio.wav', "-f", "wav", "-acodec", "pcm_s16le", "-ac", "1", "-ar", "16000", 'audio_converted.wav']
    subprocess.check_call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Start voice recognition
    r = sr.Recognizer()


    filename = "audio_converted.wav"
    # open the file
    try:
        with sr.AudioFile(filename) as source:
            # listen for the data (load audio to memory)
            audio_data = r.record(source)
            # recognize (convert from speech to text)
            text = r.recognize_google(audio_data)
            print("\n"+text)
    except sr.UnknownValueError:
        print("Silence detected. skipping")
        return False

    os.remove("audio.wav")
    os.remove("audio_converted.wav")
    return text