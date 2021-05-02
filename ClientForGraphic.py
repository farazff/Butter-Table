import socket
class ClientForGraphic:
    def __init__(self):
        self.__host = '127.0.0.1'
        self.__port = 8080
    def send(self,whichInputFile,whichMethod):
        strForSend=str(whichInputFile) +"_"+str(whichMethod)
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((self.__host, self.__port))
                sock.sendall(bytes(strForSend, 'utf-8'))
                # data = sock.recv(1024)
                print(strForSend  , " -> Sent")
        except ConnectionRefusedError:
            print("\nNot sent ,Turn on graphic server !")



