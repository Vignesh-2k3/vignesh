class account:
    def __init__(self,name,balance,min_bal):
        self.name=name
        self.balance=balance
        self.min_bal=min_bal
    def deposit(self,amount):
        self.balance=self.balance+amount
    def withdraw(self,amount):
        if self.balance-amount >= self.min_bal:
            self.balance=self.balance-amount
        else:
            print("sorry! insufficient balance")
    def printstatement(self):
        print("account bal:",self.balance)
class current(account):
    def __init__(self,name,balance,min_bal):
        super().__init__(name,balance,min_bal-1000)
    def __str__(self):
        return "Hello! {}, your current account balance is {} ".format(self.name,self.balance)
class savings(account):
    def __init__(self,name,balance):
        super().__init__(name,balance,min_bal=0)
    def __str__(self):
        return "This is {}'s savings account with balance is {}".format(self.name,self.balance)
s=savings("Dharshan",10000)
print(s)
s.deposit(5300)
s.printstatement()
s.withdraw(300)
s.withdraw(16000)

print(s)

