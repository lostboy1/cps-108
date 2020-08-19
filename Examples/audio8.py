import struct
import wave

def square_wave(volume, frequency):
    samples = []
    waveforms = frequency // 4
    width = 44100 // frequency // 2
    for i in range(waveforms):
        for j in range(width):
            samples.append(volume)
        for j in range(width):
            samples.append(-volume)
    return samples

def fade(samples, seconds):
    new = []
    for i, sample in enumerate(samples):
        gain = max(0, 1 - i / 44100 / seconds)
        new.append(int(sample * gain))
    return new

def synth(volume, frequency):
    return fade(square_wave(volume, frequency), 0.25)

C5 = 523
B4b = 466
G4 = 392
E5 = 659
F5 = 698

samples = []

samples.extend(synth(4000, C5))
samples.extend(synth(4000, C5))
samples.extend(synth(4000, B4b))
samples.extend(synth(4000, C5))
samples.extend(synth(0, C5))
samples.extend(synth(4000, G4))
samples.extend(synth(0, C5))
samples.extend(synth(4000, G4))
samples.extend(synth(4000, C5))
samples.extend(synth(4000, F5))
samples.extend(synth(4000, E5))
samples.extend(synth(4000, C5))

w = wave.open('music.wav', 'wb')
w.setnchannels(1)
w.setsampwidth(2)
w.setframerate(44100)
w.writeframes(struct.pack('<' + 'h' * len(samples), *samples))
