import sounddevice as sd
import wavio as wv

frequency= 44100
duration = 10
recording = sd.rec(int(duration * frequency), samplerate=frequency, channels=2)

sd.wait()
wv.write("recording1.wav", recording, frequency, sampwidth=2)