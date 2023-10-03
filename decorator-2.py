def decor(func):
    def inside(a,b):
        if b==0:
            print("How can i divided by Zero!")
        else:
            func(a,b)
    return inside
@decor
def div(a,b):
    c=a/b
    print(c)
div(10,2)
div(5,0)