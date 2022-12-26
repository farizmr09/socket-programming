import socket      
import threading  

def listen_msg(s):
    while True:
        msg = s.recv(1024).decode()
        print(msg)
        global stop
        if stop == True: 
            break

 
s = socket.socket()        
 
port = 3000
uname = input("Enter your Username: ") 

s.connect(('', port))
 
threading._start_new_thread(listen_msg, (s, ))

while True:
    stop = False
    msg = input()
    reformatted = uname + " : " + msg
    s.send(reformatted.encode())
    # s.send(msg.encode())
    if "/exit" in msg:
        stop = True
        s.close()
        break