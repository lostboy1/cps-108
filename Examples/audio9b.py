from random import random, randrange
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

def white_noise(volume):
    samples = []
    for i in range(44100 // 4):
        samples.append(random() * volume)
    return samples

def fade(samples, seconds):
    new = []
    for i, sample in enumerate(samples):
        gain = max(0, 1 - i / 44100 / seconds)
        new.append(int(sample * gain))
    return new

def synth(volume, frequency):
    return fade(square_wave(volume, frequency), 0.25)

def high_hat(volume):
    return fade(white_noise(volume), 0.04)

def mix(samples1, samples2):
    samples = []
    for sample1, sample2 in zip(samples1, samples2):
        samples.append(sample1 + sample2)
    return samples

C5 = 523
B4b = 466
G4 = 392
E5 = 659
F5 = 698

drum_intro = []
drum_intro.extend(high_hat(12000))
drum_intro.extend(high_hat(3000))
drum_intro.extend(high_hat(12000))
drum_intro.extend(high_hat(3000))

samples = []
samples.extend(drum_intro)

for i in range(2):              # throw in a little drum intro
    samples.extend(drum_intro)
    samples.extend(mix(synth(4000, C5), high_hat(12000)))
    samples.extend(mix(synth(4000, C5), high_hat(3000)))
    samples.extend(mix(synth(4000, B4b), high_hat(12000)))
    samples.extend(mix(synth(4000, C5), high_hat(3000)))
    samples.extend(mix(synth(0, C5), high_hat(12000)))
    samples.extend(mix(synth(4000, G4), high_hat(3000)))
    samples.extend(mix(synth(0, C5), high_hat(12000)))
    samples.extend(mix(synth(4000, G4), high_hat(3000)))
    samples.extend(mix(synth(4000, C5), high_hat(12000)))
    samples.extend(mix(synth(4000, F5), high_hat(3000)))
    samples.extend(mix(synth(4000, E5), high_hat(12000)))
    samples.extend(mix(synth(4000, C5), high_hat(3000)))

w = wave.open('music.wav', 'wb')
w.setnchannels(1)
w.setsampwidth(2)
w.setframerate(44100)
w.writeframes(struct.pack('<' + 'h' * len(samples), *samples))
