from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    #concrete method
    def descript(self):
        return "This is a shape."
#concrete class : circle
class circle (shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
    def perimeter(self):
        return 2*3.14*self.radius
        
Circel= circle(5)
#Rectangle=rectangle(4,56)
print("circle area",circle.area())
print("circle perimeter",circle.perimeter())
print("circle descrp")           