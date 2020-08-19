from random import randrange
import struct
import wave

w = wave.open('music.wav', 'wb')
w.setnchannels(1)
w.setsampwidth(2)
w.setframerate(44100)

def play_note(w, volume, frequency, drum_volume):
    waveforms = frequency // 4
    width = 44100 // frequency // 2
    k = 0
    for i in range(waveforms):
        amplitude = volume - volume * i // waveforms
        for j in range(width):
            sample = max(0, int(drum_volume * (2200 - k) / 2200))
            drum = randrange(-sample, sample + 1)
            w.writeframes(struct.pack('<h', amplitude + drum))
            k += 1
        for j in range(width):
            sample = max(0, int(drum_volume * (2200 - k) / 2200))
            drum = randrange(-sample, sample + 1)
            w.writeframes(struct.pack('<h', -amplitude + drum))
            k += 1

C5 = 523
B4b = 466
G4 = 392
E5 = 659
F5 = 698

play_note(w, 4000, C5, 12000)
play_note(w, 4000, C5, 3000)
play_note(w, 4000, B4b, 12000)
play_note(w, 4000, C5, 3000)
play_note(w, 0, C5, 12000)
play_note(w, 4000, G4, 3000)
play_note(w, 0, C5, 12000)
play_note(w, 4000, G4, 3000)
play_note(w, 4000, C5, 12000)
play_note(w, 4000, F5, 3000)
play_note(w, 4000, E5, 12000)
play_note(w, 4000, C5, 3000)
