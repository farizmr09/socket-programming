import socket  
import threading          

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
print ("Socket successfully created")

port = 1234 #Portnya terserah lu         
 
s.bind(('', port)) #Dikosongin == localhost == 127.0.0.1      
print ("socket binded to %s" %(port))
 

s.listen(100) #Maksimal client yang connect 5   
print ("socket is listening")           

def broadcast(msg, c):
    for client in clients:
        if c != client:
            client.send(msg.encode())

def multi_thread(c, addr):
    print('Got connection from', addr)
    c.send('Thank you for connecting'.encode())
    while True:
        msg = c.recv(1024).decode()
        if msg == "exit":
            broadcast((f"{addr} left the chat!"), c)
            c.close()
            clients.remove(c)
            break
        broadcast((f"{addr}: {msg}"), c)

clients = []

while True:
  c, addr = s.accept()    
  clients.append(c)
  threading._start_new_thread(multi_thread, (c, addr, ))
  if len(clients) == 0:
    s.close()

   