import sounddevice as sd
import numpy as np
import socket, struct 

#setup 
duration = 1 
fs = 44100  #sample rate
float32 = 4
bufferSize = duration * fs * float32 

sd.default.samplerate = fs
sd.default.channels = 1 #mono 
sd.default.device = (2, 1) #output, input


#network setup 
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 1234  # The port used by the server


#recieving audio 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True: 
        #information to decode recieved binary
        #float32 format, little-endian, mono audio, 44100 sample rate 
        #sameplerate/4 bytes (float 32), means buffer size is 11025

        #recieving and decoding binary audio 
        data = s.recv(bufferSize)
        audio = np.frombuffer(data, dtype='<f4') #little endian, and 32bit float 


        #playing recording 
        sd.play(audio, fs)
        sd.wait() 