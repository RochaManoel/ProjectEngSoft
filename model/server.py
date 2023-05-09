import socket
from threading import Thread
from dataBase.users.dataBaseUser import DataBaseUser
from dataBase.products.dataBaseProduct import DataBaseProduct

class Server:
    def __init__(self, nameServer, serverAddress, serverPort):
        self.serverName = nameServer
        self.serverAddress = serverAddress
        self.serverPort = serverPort
        self.socketServer = ''

    def start(self):
        print('Servidor ', self.serverName,' está Online!')
        self.socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socketServer.bind((self.serverAddress, self.serverPort))
        self.socketServer.listen(10)
        self.active()

    def active(self):
        while True:
            socketClient, clienteAddr = self.socketServer.accept()
            Thread(target=self.process, args=(socketClient, clienteAddr)).start()
    
    def process(self,socketClient, clienteAddr):
        dataReceived = socketClient.recv(1024)
        dataReceived = dataReceived.decode()
        if(dataReceived.startswith("GET")):
            self.methodGET(dataReceived=dataReceived,socketClient=socketClient)
        elif(dataReceived.startswith("POST")):
            self.methodPOST(dataReceived=dataReceived,socketClient=socketClient)

    def methodGET(self,dataReceived,socketClient):
        header = dataReceived.split('\r\n')[0]
        try:
            pathFile = self.getPathRequestGET(header = header)
            respondeHead = f'HTTP/1.1 200 OK\r\n\r\n'
            if self.isTXT(pathFile):
                file = open(pathFile,'r', encoding='utf-8')
                response = respondeHead + file.read()
                socketClient.sendall(response.encode('utf-8'))
            else:
                file = open(pathFile, 'rb')
                response = bytes(respondeHead, 'utf-8') + file.read()
                socketClient.sendall(response)
            socketClient.close()
        except FileNotFoundError:
            socketClient.sendall(b'HTTP/1.1 404 File not found\r\n\r\nErro 404')
            return

    def isTXT(self,pathFile):
        if pathFile.split('.')[-1] in ['html','css','js']:
            return True
        return False

    def getPathRequestGET(self,header):
        if header == 'GET / HTTP/1.1' or header == '':
            return 'view\\html\\index.html'
        url = header.split(' ')[1][1:]
        if url in ['index','contato','login','cadastro','redefinirsenha','operacoes','comprarCarros','venderCarros','carro']:
            return 'view\\html\\' + url + '.html'
        elif url == 'UserData.json':
            return 'dataBase\\users\\' + url
        elif url == 'productData.json':
            return 'dataBase\\products\\' + url
        return url

    def methodPOST(self,dataReceived,socketClient):
        headerPost = dataReceived.split('\r\n')[0]
        data = dataReceived.split('\r\n')[-1]
        try:
            path = self.getPathRequestPOST(headerPost=headerPost)
            if path == 'setUser':
                db = DataBaseUser()
                db.setUser(data)
                print('Usuário setado com Sucesso!')                
                socketClient.sendall(b'HTTP/1.1 201 OK\r\n\r\nSucesso')
            elif path == 'sendCode':
                db = DataBaseUser()
                db.sendEmail(data)
                print('Enviado com sucesso')                
                socketClient.sendall(b'HTTP/1.1 201 OK\r\n\r\nSucesso')
            elif path == 'setPassword':
                db = DataBaseUser()
                db.setPassword(data)
                print('Enviado com sucesso')                
                socketClient.sendall(b'HTTP/1.1 201 OK\r\n\r\nSucesso')
            elif path == 'setProduct':
                db = DataBaseProduct()
                db.setProduct(data)
                print('Enviado com sucesso')                
                socketClient.sendall(b'HTTP/1.1 201 OK\r\n\r\nSucesso')
            elif path == 'sendMessage':
                db = DataBaseUser()
                db.sendMessage(data)
                print('Enviado com sucesso')                
                socketClient.sendall(b'HTTP/1.1 201 OK\r\n\r\nSucesso')
            socketClient.close()
        except:
            socketClient.sendall(b'HTTP/1.1 404 File not found\r\n\r\nErro 404')
            return

    def getPathRequestPOST(self,headerPost):
        path = headerPost.split(' ')[1][1:]
        return path
