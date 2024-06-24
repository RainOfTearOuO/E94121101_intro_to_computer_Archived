import socket

HOST = '192.168.137.97' #server ip & port
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print('Connected to ' + HOST)

    while True:
        outdata = input('The Fibonacci(n) when n = ') #data which is sent to server
        s.send(outdata.encode())

        indata = s.recv(1024) #data which is received from server
        if (outdata=='exit' or len(indata) == 0): # connection closed
            s.close()
            print('Connection Closed.')
            break

        print('The answer is ' + indata.decode())
