import struct
import wave

w = wave.open('music.wav', 'wb')
w.setnchannels(1)
w.setsampwidth(2)
w.setframerate(44100)

for i in range(500):
    for j in range(24):
        w.writeframes(struct.pack('<h', 4000))

    for j in range(24):
        w.writeframes(struct.pack('<h', -4000))
