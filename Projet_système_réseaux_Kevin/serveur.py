import socket
import threading


List_clients=[]
def threaded(c,nom):
    while True:
        data = c.recv(1024)
        if not data:
            print('Deconnection de ',nom)
            break
        dat=data.decode()
        if dat=="stop":
            print('Deconnection de ',nom)
            break
        for i in List_clients:
            if i !=c:
                i.send(("message de "+str(nom)+": "+dat).encode())
    List_clients.remove(c)
    c.close()


def main():
    Host = 'localhost'
    Port = 5001
    s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    s.bind((Host, Port)) 
    s.listen(2)
    print("serveur demarrer")
    while True:
        c,addr = s.accept()
        List_clients.append(c)
        nom = c.recv(1024)
        name=nom.decode()
        print('Connection de ',name)
        thread_all = threading.Thread(target = threaded,args=[c,name])
        thread_all.start()
    thread_all.stop()
    s.close()
 
if __name__ == '__main__':
    main()