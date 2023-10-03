class Multi:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def product(self):
        print("The product is",self.a * self.b)
class Division:
    def __init__(self,a,b):
        super().__init__(a,b)
    def divi(self):
        print("The division is",self.a / self.b)
class Result(Multi,Division):
    def out(self):
        print("The Product and Division of A and B is")
        self.product()
        self.divi()
obj1=Result(10,2)
obj2=Result(20,5)
obj1.out()
obj2.out()