def wish(*a,**b):
    print(a)
    print(b)
    for s in a:
        print(s)
        for k,v in b.items():
            print(k,v)

wish('jana','bala','surya',city='mumbai',age='20')