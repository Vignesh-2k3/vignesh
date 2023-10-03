# class Parent:
#     def __init__(self,name,age,msg):
#         self.name=name
#         self.age=age
#         self.message=msg
#     def info(self):
#         print("my name is:",self.name)
#         print("my age is:",self.age)
#         print(self.message)
#
# class Child(Parent):
#     def __init__(self,name,age,msg,details):
#         super().__init__(name,age,msg)
#         self.details=details
#     def demo(self):
#         super().info()
#         print(self.details)
#
# c=Child('jana',20,'Hii everyone',"B+ve")
# c.demo()

class Insta:
    def __init__(self,post,stry):

        self.post=post
        self.story=stry

    def act(self):

        print(self.post)
        print(self.story)


class Whatsapp:
    def __init__(self,post,stry,chat,calls):
        super().__init__(post,stry)
        self.chat=chat
        self.call=calls
    def act2(self):
        print(self.chat)
        print(self.call)

class Yann(Insta,Whatsapp):
    def __init__(self,post,stry,chat,calls):
        super().__init__(post,stry,chat,calls)

    def act3(self):
        self.act()
        self.act2()




o=Yann('bike pic','bday','hii ','vdo calls')
o.act3()