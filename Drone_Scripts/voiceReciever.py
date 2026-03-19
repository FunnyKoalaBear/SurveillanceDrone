import sounddevice as sd
import numpy as np
import socket, struct 

#audio setup 
duration = 20
fs = 44100  #sample rate
float32 = 4
bufferSize = duration * fs * float32 
sd.default.device = (0, 1) #connects to raspberry speaker
sd.default.samplerate = fs
sd.default.channels = 1 #mono audio 

#python3 -m sounddevice #to check supported output/input devices 

#network setup 
HOST = "192.168.1.120"  # The server's hostname or IP address
PORT = 1234  # The port used by the server


#function to receive entire audio byte or fill it 
def recvall(sock, n):
    data = bytearray() 

    while len(data) < n:
        packet = sock.recv(n - len(data)) #reading the header/payload byte by byte

        if not packet:
            return None

        data.extend(packet)
    
    return data #returns header/payaload


#recieving audio 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True: 
        #Below is information to decode recieved binary: 
        #float32 format, little-endian, mono audio, 44100 sample rate
        #4 byte header, variable size message payload

        #Below is code for recieving and decoding binary audio:
        
        #finding message length from header (4 byte size)
        raw_msglen = recvall(s, 4)
        if not raw_msglen:
            print("Connection closed.")
            break
            
        #unpack the 4 bytes into an integer (Little Endian <, Unsigned Int I format for header)
        msglen = struct.unpack('<I', raw_msglen)[0] 
        print(f"Receiving {msglen} bytes of audio...")

        #read data based on msglen
        data = recvall(s, msglen)
        if not data:
            break

        #playing audio 
        audio = np.frombuffer(data, dtype='<f4')
        sd.play(audio, fs)
        sd.wait()
        print("Playback finished.")