import math

class WinDoor:
    def __init__(self,length,width):
        self.length=length
        self.width=width
        self.wd_square=length*width
            
        
    def __repr__ (self):
        return f'{self.length}x{self.width}'
    
class Room:
    def __init__(self):
        self.wd=[]
        
    def addWD(self,length,width):            
        self.wd.append(WinDoor(length,width))
    
    def square_room(self,x,y,h):
        self.all_square=2*h*(x+y) #полная площадь
        return self.all_square
    
    def worksurface(self):   
        work_square=self.all_square
        for i in self.wd:
            work_square-=i.wd_square #оклеиваемая площадь           
        return work_square
    
    def roll(self,l_r,w_r):
        self.roll_square=l_r*w_r
        return self.roll_square


a=Room()
question=input('Есть ли у вас неоклеиваемые элементы (y/n):')
while question=='y':
    a.addWD(float(input('Длина элемента:')),float(input('Ширина элемента:')))
    question=input('Есть ли у вас еще неоклеиваемые элементы (y/n):')

a.square_room(float(input('Введите ширину самой широкой стены:')),
                float(input('Введите ширину самой узкой стены:')),
                float(input('Введите высоту стен:')))

c=a.worksurface()
print(f'Рабочая площадь составляет {c} м2')

d=c/a.roll(float(input('Введите длину рулона:')),float(input('Введите ширину рулона:')))
print(f'Вам понадобится {math.ceil(d)} штука(штук)')
        
        
        
    