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

C5 = 523
B4b = 466
G4 = 392
E5 = 659
F5 = 698

play_note(w, 4000, C5)
play_note(w, 4000, C5)
play_note(w, 4000, B4b)
play_note(w, 4000, C5)
play_note(w, 0, C5)
play_note(w, 4000, G4)
play_note(w, 0, C5)
play_note(w, 4000, G4)
play_note(w, 4000, C5)
play_note(w, 4000, F5)
play_note(w, 4000, E5)
play_note(w, 4000, C5)
