class Pet:
     def __init__(self):
        self.tail=True
        self.paws=4
        self.appetite=100
    
class FromVillage:
    
    def protect_area(self):
        pass


class Cat(Pet):
        
    def get_eat(self):
        print('meow')
        
class Dog(Pet,FromVillage):
     def get_eat(self):
        print('auf')
    
c=Cat()
d=Dog()


d.get_eat()