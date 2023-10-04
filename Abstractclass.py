from abc import *
class fruit(ABC):
    @ abstractmethod
    def taste(self):
        pass

f=fruit()
f.taste()


from abc import *
class vehicle(ABC):
    @ abstractmethod
    def noofwheels(self):
        pass
class bus(vehicle):
    pass

b=bus()

from abc import *


class vehicle(ABC):
    @abstractmethod
    def wheels(self):
        pass


class bus(vehicle):
    def wheels(self):
        return 7

class auto(vehicle):
    def wheels(self):
        return 4


b = bus()
c =  auto()
print(b.wheels())
print(c.wheels())

class test:
    x=10
    _y=20
    __z=100
    def m1(self):
        print(test.x)
        print(test._y)
        print(test.__z)

t=test()
t.m1()
print(test.x)
print(test._y)
print(test.__z)