from tkinter import messagebox
import random
import socket

class Server:
    def __init__(self, host : str, port : int):
        self.host=host
        self.port=port
        self.adress=(self.host,self.port)
        
    def binding(self):
        self.server=socket.socket()
        self.server.bind(self.adress)
        self.server.listen(1)
        print('Listening...')
        
    def work(self):
        while True:
            user_socket,adress= self.server.accept()
            data=user_socket.recv(2048)
            val=data.decode('utf-8')
            print(val)
            
            ii_desire=['paper','rock','scissors']
            computer_action=random.choice(ii_desire)
            print(computer_action)
            
            if val==computer_action:
                message='Что ж..сильные соперники.Ничья'
            elif val=='rock':
                if computer_action=='scissors':
                    message='А бездушная машина выбрала...Ножницы! Ты спас нас.Победа!!'
                else:
                    message='А бездушная машина выбрала...Бумагу! Это начало конца...Ты проиграл.'
            elif val=='paper':
                if computer_action=='rock':
                    message='А бездушная машина выбрала...Камень! Ты спас нас.Победа!!'
                else:
                    message='А бездушная машина выбрала...Ножницы! Это начало конца...Ты проиграл.'
            elif val=='scissors':
                if computer_action=='paper':
                    message='А бездушная машина выбрала...Бумагу! Ты спас нас.Победа!!'
                else:
                    message='А бездушная машина выбрала...Камень! Это начало конца...Ты проиграл.'
            
            #print(message)
            user_socket.send(message.encode('utf-8'))


out=Server('127.0.0.1',10000)
out.binding()
out.work()
out.close()














#сервер
#server=socket.socket()

#server.bind(('127.0.0.1',9090))# прибиндить(то есть жать серверу адрес,по которому к нам будут включаться)

#server.listen(1)
#print('Server is listening')

#while True:
    #user_socket,adress= server.accept()
    #print('connected:',adress)
    #user_socket.send('You\'re connected'.encode('utf-8'))# обмен инфой между клиентом и сервером осуществляется только при помощи байтов
    #data=user_socket.recv(2048)
    
   # print(data.decode('utf-8'))





