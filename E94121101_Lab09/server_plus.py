import socket
import threading

HOST = '192.168.137.97'
PORT = 8000

def func(n):
    li=[0,1]
    if(n==0 or n==1):
        pass
    else:
        for i in range(2,n+1):  #in math interval notation: [2,n] or [2,n+1), i is an int
            li.append(li[i-1]+li[i-2])
    return li[n]

class ThreadedServer():
    def __init__(self, HOST, PORT): #constructor and initialization
        self.HOST = HOST
        self.PORT = PORT
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind((self.HOST, self.PORT))

    def listen(self):
        self.s.listen(5)
        print('Waiting for connection...')
        while True:
            conn, addr = self.s.accept()
            print('Add connection from ' + str(addr))
            threading.Thread(target = self.listenToClient, args = (conn, addr)).start()
    
    def listenToClient(self, conn, addr):
        while True:
            indata = conn.recv(1024)

            if (len(indata)) == 0: # connection closed
                conn.close()
                print('Connection Closed.')
                break
            print('Received from ' + str(addr) + ': ' + indata.decode())

            if indata.decode() == 'exit':
                conn.close()
                print('Connection Closed.')
                break
            outdata = str(func(int(indata.decode())))
            print('Send to ' + str(addr) + ': ' + outdata)
            conn.send(outdata.encode())

ThreadedServer(HOST, PORT).listen()
