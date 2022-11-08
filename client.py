import socket      
import threading  

def listen_msg(s):
    while True:
        print(s.recv(1024).decode())
        global stop
        if stop == True: 
            break

 
s = socket.socket()        
 
port = 1234         
 
s.connect(('127.0.0.1', port))
 
threading._start_new_thread(listen_msg, (s, ))

while True:
    stop = False
    msg = input()
    s.send(msg.encode())
    if msg == "exit":
        stop = True
        s.close()
        break