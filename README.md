# Voice-Recorder
Project to create voice recorder in Python

#Create Virtual Environment
python3 -m venv envo

Create file to write code

#Install sound device 
$ pip3 install sounddevice

#Install Wavio to save the recorded audio in file format
$ pip3 install wavio

#Install portaudio library.
sudo apt-get install libportaudio2

#import required libraries
import sounddevice as sd
import wavio as wv

Sampling frequency
frequency = 44100

Recording duration
duration = 10
(It will create a NumPy array of the recorded audio)

Start recorder with the given values of 
duration and sample frequency
recording = sd.rec(int(duration * frequency),samplerate=frequency, channels=2)

Record audio for the given number of seconds
sd.wait()

#To save the audio file
#Convert the NumPy array to audio file
wv.write("recording1.wav", recording, freq, sampwidth=2)

#Play the recording from the recoding folder

 
 
