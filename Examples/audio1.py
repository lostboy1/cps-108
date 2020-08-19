import struct
import wave

w = wave.open('music.wav', 'wb')
w.setnchannels(1)
w.setsampwidth(2)
w.setframerate(44100)

w.writeframes(struct.pack('<h', 4000))
w.writeframes(struct.pack('<h', 4000))
w.writeframes(struct.pack('<h', 4000))
w.writeframes(struct.pack('<h', 4000))
w.writeframes(struct.pack('<h', 4000))

w.writeframes(struct.pack('<h', -4000))
w.writeframes(struct.pack('<h', -4000))
w.writeframes(struct.pack('<h', -4000))
w.writeframes(struct.pack('<h', -4000))
w.writeframes(struct.pack('<h', -4000))

w.writeframes(struct.pack('<h', 4000))
w.writeframes(struct.pack('<h', 4000))
w.writeframes(struct.pack('<h', 4000))
w.writeframes(struct.pack('<h', 4000))
w.writeframes(struct.pack('<h', 4000))

w.writeframes(struct.pack('<h', -4000))
w.writeframes(struct.pack('<h', -4000))
w.writeframes(struct.pack('<h', -4000))
w.writeframes(struct.pack('<h', -4000))
w.writeframes(struct.pack('<h', -4000))
