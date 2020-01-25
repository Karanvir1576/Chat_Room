import socket
from threading import Thread
import select
import sys
import msvcrt
rlist=[]
##def send_msg(socket):
##    msg=sys.stdin.readline()
##    socket.send(msg)
##    sys.stdout.write('[ME]');sys.stdout.flush()

def recieve(s):
    while True:
            
        read,write,err = select.select([s],[],[])
        if s in read:
            data = s.recv(4096)
            if data:
                sys.stdout.write(data)
                sys.stdout.write('[Me]');sys.stdout.flush()
            else:
                print("Disconnected form server")
                sys.exit()
def send(s):
    while True:
            
        r,w,e=select.select([],[s],[])
        if len(w):
            data = sys.stdin.readline()
            s.send(data.encode('ascii'))
            sys.stdout.write('[Me]');sys.stdout.flush()
        

if len(sys.argv)<3:
    print("USAGE:chat_client.py hostname port")
    sys.exit()

host = sys.argv[1]
port = int(sys.argv[2])

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.settimeout(2)

#try toconnect to remote host
try:
    s.connect((host,port))
except:
    print("unable to connect")
    sys.exit()

print("Connected to remote host,you can start chatting\n")
sys.stdout.write('[Me]');sys.stdout.flush()
    
    

    #2 cases:client waits for msg from server or when its ready to send data
    #So we define a select function with the list(sys.stdin,s)
    #either input(user needs to send) or socket itself(msg from server)
if __name__=='__main__':
    
    t1=Thread(target=recieve,args=(s,))
    t2 =Thread(target=send,args=(s,))
    t1.start()
    t2.start()
            
    
            
    
