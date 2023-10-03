# class Book:
#     def __init__(self,pages):
#         self.pages=pages
#     def __add__(self, other):
#         return self.pages+other.pages
# b1=Book(100)
# b2=Book(200)
# print(b1+b2)

class Assignment:
    def __init__(self,mark):
        self.mark=mark
    def __add__(self, other):
        return self.mark+other.mark
    def __sub__(self, other):
        return self.mark-other.mark
    def __mul__(self, other):
        return self.mark*other.mark
m1=Assignment(300)
m2=Assignment(200)
print(m1+m2)
print(m1-m2)
print(m1*m2)

