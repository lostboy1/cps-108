import struct
import wave

w = wave.open('music.wav', 'wb')
w.setnchannels(1)
w.setsampwidth(2)
w.setframerate(44100)

for i in range(125):
    amplitude = 4000 - i * 32
    for j in range(24):
        w.writeframes(struct.pack('<h', amplitude))
    for j in range(24):
        w.writeframes(struct.pack('<h', -amplitude))
