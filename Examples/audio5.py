import struct
import wave

w = wave.open('music.wav', 'wb')
w.setnchannels(1)
w.setsampwidth(2)
w.setframerate(44100)

def play_note(w, volume, frequency):
    waveforms = frequency // 4
    width = 44100 // frequency // 2
    for i in range(waveforms):
        amplitude = volume - volume * i // waveforms
        for j in range(width):
            w.writeframes(struct.pack('<h', amplitude))
        for j in range(width):
            w.writeframes(struct.pack('<h', -amplitude))

play_note(w, 4000, 523)
play_note(w, 4000, 523)
play_note(w, 4000, 466)
play_note(w, 4000, 523)
play_note(w, 0, 523)
play_note(w, 4000, 392)
play_note(w, 0, 523)
play_note(w, 4000, 392)
play_note(w, 4000, 523)
play_note(w, 4000, 698)
play_note(w, 4000, 659)
play_note(w, 4000, 523)
