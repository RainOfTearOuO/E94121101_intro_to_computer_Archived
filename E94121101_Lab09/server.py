import socket

def func(n):
    li=[0,1]
    if(n==0 or n==1):
        pass
    else:
        for i in range(2,n+1):  #in math interval notation: [2,n] or [2,n+1), i is an int
            li.append(li[i-1]+li[i-2])
    return li[n]

HOST = '192.168.137.97' #server ip & port
PORT = 8000

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(5)
        print('Waiting for connection...')
        conn, addr = s.accept()
        print('Add connection from ' + str(addr))

        while True:
            indata = conn.recv(1024) #data which is received from client

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