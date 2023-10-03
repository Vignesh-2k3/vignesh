# class Test:
#     def m1(self):
#         print("No-argument")
#     def m1(self,a,b):
#         print("two argument")
#     def m1(self,a):
#         print("one arguments")
# t=Test()
# # t.m1()
# # t.m1(18)
# t.m1(12)

# class Sum:
#     def add(self,a=None,b=None,c=None):
#         if a!=None and b!=None and c!=None:
#             print("the sum is",a+b+c)
#         elif a!=None and b!=None:
#             print("the sum of a and b is",a+b)
#         else:
#             print("please provide 2 or 3 arguments")
# s=Sum()
# s.add(12,13)
# s.add(10,12,13)
# s.add()

class Test:
    def m1(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("Three arguments:",a,b,c)
        elif a!=None and b!=None:
            print("Two arguments:",a,b)
        elif a!=None:
            print("One argument:",a)
        else:
            print("No argument!")
t=Test()
t.m1(12,13,14)
t.m1(12,13)
t.m1(12)
t.m1()
