# class P1:
#     def m1(self):
#         print("Parent 1")
# class P2:
#     def m2(self):
#         print("Parent 2")
# class C(P1,P2):
#     def m3(self):
#         print("child class")
#
# c=C()
# c.m1()
# c.m2()
# c.m3()



# --METHOD RESOLUTION ORDER--(MRO)
# class P1:
#     def m1(self):
#         print("Parent 1")
# class P2:
#     def m1(self):
#         print("Parent 2")
# class C(P1,P2):
#     def m2(self):
#         print("child class")
#
# c=C()
# c.m1()
# c.m2()

class Add:
    def plus(self):
        a=int(input("enter the a value:"))
        b=int(input("enter the b value:"))
        c=a+b
        print("addtion of a and b is:",c)
class Sub:
    def minus(self):
        a=int(input("enter the a value:"))
        b=int(input("enter the b value:"))
        c=a-b
        print("subtraction of a and b is:",c)
class Result(Add,Sub):
    def out(self):
        self.plus()
        self.minus()
obj1=Result()
obj1.out()
