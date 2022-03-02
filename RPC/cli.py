import socket

class Client:
        
    def __init__(self, host : str, port : int):
        self.host=host
        self.port=port
        self.adress=(self.host,self.port)
    
    def connection(self):
        self.client=socket.socket()
        self.client.connect(self.adress)
        
    def work(self):
        while True:
            self.client.send(input('Сделай свой выбор (paper/rock/scissors):').encode('utf-8'))
            self.data=self.client.recv(2048) #получаем то,что нам возвращается от сервера от recieve
            self.endgame=self.data.decode('utf-8')
            
            print(self.endgame)
            return self.endgame
        
        
put=Client('127.0.0.1',10000)
put.connection()
put.work()