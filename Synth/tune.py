import os
import struct
import sys
import wave

sys.path.insert(0, os.path.dirname(__file__))

C5 = 523
B4b = 466
G4 = 392
E5 = 659
F5 = 698
VOLUME = 12000

notes = [
    [VOLUME, C5],
    [VOLUME, C5],
    [VOLUME, B4b],
    [VOLUME, C5],
    [0, C5],
    [VOLUME, G4],
    [0, C5],
    [VOLUME, G4],
    [VOLUME, C5],
    [VOLUME, F5],
    [VOLUME, E5],
    [VOLUME, C5],
]

from fade import fade
from gain import gain
from repeat import repeat
from square import square_wave

all_samples = []
quarter_second = 44100 // 4
for volume, frequency in notes:
    samples = square_wave(int(44100 / frequency // 2))
    samples = gain(samples, volume)
    samples = repeat(samples, quarter_second)
    samples = fade(samples, quarter_second)
    all_samples.extend(samples)

all_samples = [int(sample) for sample in all_samples]

w = wave.open('music.wav', 'wb')
w.setnchannels(1)
w.setsampwidth(2)
w.setframerate(44100)
w.writeframes(struct.pack('<' + 'h' * len(all_samples), *all_samples))
