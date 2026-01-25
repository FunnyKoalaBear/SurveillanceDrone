import sounddevice as sd
import numpy as np
import socket

#recording setup 
duration = 1 #sec
fs = 44100  #sample rate
sd.default.samplerate = fs
sd.default.channels = 1 #mono 
#d.default.device = (2, 1) #output, input
gain = 20

#python3 -m sounddevice #to check supported output/input devices 

#socket setup 
HOST = "127.0.0.1"
PORT = 1234

#TCP transmission 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept() #(clientsocket, address) = serversocket.accept()

    with conn:
        print(f"Connected by {addr}") #logging new connection 

        while True:

            #recording audio 
            recording = sd.rec(int(duration*fs), dtype='float32') #returns immediatley, and runs in background 
            sd.wait() #to check if recording is finished

            #increasing recording volume
            louderRecording = np.clip(recording * gain, -1.0, 1.0) 

            #sending data 
            conn.sendall(louderRecording)
            print("Next recording")





#upgrade this program by doing it with classes so function can be called before audio is sent 
#https://docs.python.org/3/howto/sockets.html
#for now i will leave this at a working prototype
#on demand audio transfer button will be needed once the drone control application is made 

#upgrade 2 
#voice modulation features 