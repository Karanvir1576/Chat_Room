import socket
import select
import sys

host = ''
port = 9000
recv_buffer = 4096
socket_list=[]
def chat_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server.bind((host,port))
    server.listen(10)

    socket_list.append(server)
    print("Chat server started on"+str(port))

    while True:
        #Declare the select list
        r_to_read,r_to_write,errorlist = select.select(socket_list,[],[],0)

        for sock in r_to_read:
            #when server is ready to read then it can accept connection
            if sock == server:
                conn,addr=server.accept()
                socket_list.append(conn)
                print("CLient",addr,"connected\n")
                
                broadcast(server,conn,"[%s,%s]entered in chattingroom\n"% addr)
            #client is readable,server reads msg and broadcasts
            else:
                
                try:
                    data = sock.recv(recv_buffer)
                    if data:
                        #data is sent bt client
                        broadcast(server,sock,"\r"+'['+str(sock.getpeername())+']'+data)
                except:
                    broadcast(server,sock,"Client[%s,%s] is offline"%addr)
                    print("Client",addr,"is offline")
                    sock.close()
                    socket_list.remove(sock)
                    continue
              
    server.close()
#FUNCTION TO SEND MSG TO CLIENTS
def broadcast(server_sock,client,message):
    for socket in socket_list:
        if (socket!= server_sock) & (socket!= client):
            try:
                socket.send(message)
            except:
                #broken socket connection
                socket.close()
                #remove broken socket

                if socket in socket_list:
                    socket_list.remove(socket)
   

if __name__=="__main__":
    chat_server()
                    
            
            
