def play(filename):
    from pydub import AudioSegment
    from pydub.playback import play

    audio = AudioSegment.from_mp3(filename)
    play(audio)
