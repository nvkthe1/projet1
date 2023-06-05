import socket
import threading

def recu(c):
    while True:
        data = c.recv(1024)
        if not data:
            print('deconnection')
            c.close()
            return
        dat=data.decode()
        print(dat)

def Main():
    Host = 'localhost'
    Port = 5001
    c = socket.socket(socket.AF_INET6,socket.SOCK_STREAM)
    c.connect((Host, Port))
    nom = input('entrez votre nom: ')
    c.send(nom.encode())
    thread_reicv = threading.Thread(target = recu,args=[c])
    thread_reicv.start()
    while True:
    
        message = input('')
        c.send(message.encode())
        if message=="stop":
            c.close()
            return
    thread_reicv.stop()

if __name__ == '__main__':
    Main()