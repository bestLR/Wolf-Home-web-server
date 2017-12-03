import random
from socket import *
ResponseHeader=b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nAccept-Ranges: bytes\r\n\r\n"

def get_host_ip():
    try:
        s = socket(AF_INET,SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))       
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip
HOST=get_host_ip()
PORT=7921
ADDR=(HOST,PORT)
print(str(HOST)+':'+str(PORT))
s=socket(AF_INET,SOCK_STREAM)
s.bind(ADDR)
s.listen(5)
while True:
    c,addr=s.accept()
    buff=c.recv(1024)
    if buff.find(b'GET')>=0 and buff.find(b'HTTP')>0 and buff.find(b'date.txt')<0:
        c.send(ResponseHeader)
        f=open('index.html','r')
        while True:
            line=f.readline()
            c.send(bytes(line,encoding='utf-8'))
            if not line:
                break
        f.close()
    if buff.find(b'GET')>=0 and buff.find(b'date.txt')>0:
        c.send(ResponseHeader)     
        c.send(bytes(str(random.uniform(0,50)),encoding='utf-8'))           
    c.close()
