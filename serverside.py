import socket
from threading import Thread


# Multi-threaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread):

    def __init__(self, ip, port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        # print("[+] New server socket thread started for " + ip + ":" + str(port))

    def run(self):
        while True:
            data = conn.recv(2048)
            if not data:
                print(ip, " closed the connection")
                break
            print(ip, " >", data.decode())
            msg = input("Me > ")
            if msg == 'exit':
                conn.close()
                break
            conn.send(msg.encode())   # echo


# Multi-threaded Python server
TCP_IP = ''
TCP_PORT = 2004
BUFFER_SIZE = 20  # Usually 1024, but we need quick response

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpServer.bind((TCP_IP, TCP_PORT))
threads = []

while True:
    tcpServer.listen(4)
    print("Multi-threaded Python server : Waiting for connections from TCP clients...")
    (conn, (ip, port)) = tcpServer.accept()
    print("[+] New server socket thread started for " + ip + ":" + str(port))
    new_thread = ClientThread(ip, port)
    new_thread.start()
    threads.append(new_thread)

    for t in threads:
        t.join()
