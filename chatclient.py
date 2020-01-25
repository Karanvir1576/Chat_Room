import socket
import select
import sys

if len(sys.argv)<3:
    sys.stdout.write("USAGE:chat_client.py hostname port")
    sys.exit()

host = sys.argv[1]
port = int(sys.argv[2])

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.settimeout(2)
try:
    s.connect((host,port))
except:
    print("unable to connect")
    sys.exit()
print("CONNECTED TO REMOTE HOST,YOU CAN START CHATTING")
sys.stdout.write('[Me]');sys.stdout.flush()

    
socketnew = socket.socket()
socketnew.bind((host,port))



while True:
    rlist=[s,socketnew]
    read_list,w_list,error_list = select.select(rlist,[],[])

    for socket in read_list:
        if socket == s:
            data = socket.recv(4096)
            if data:
                sys.stdout.write(data)
                sys.stdout.write('[Me]');sys.stdout.flush()
            else:
                print('Disconnected from server')
                sys.exit()
        else:
            msg=sys.stdin.readline()
            socket.send(msg)
            sys.stdout.write('[Me]');sys.stdout.flush()

     
    
    
    

    
