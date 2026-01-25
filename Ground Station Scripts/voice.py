import sounddevice as sd
import numpy as np


#recording setup 
duration = 10.5
fs = 44100
sd.default.samplerate = fs
sd.default.channels = 2

#recording 
recording = sd.rec(int(duration*fs)) #returns immediatley, and runs in background 


