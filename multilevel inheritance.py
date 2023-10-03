# oru class ah innoru class oda inherits pandrathu multi-level inheritance
class Add:
    def plus(self):
        a=int(input("enter the a value:"))
        b=int(input("enter the b value:"))
        c=a+b
        print("addtion of a and b is:",c)
class Sub(Add):
    def minus(self):
        a=int(input("enter the a value:"))
        b=int(input("enter the b value:"))
        c=a-b
        print("subtraction of a and b is:",c)
class Callfunc(Sub):
    def call(self):
        self.plus()
        self.minus()
o1=Callfunc()
o1.call()