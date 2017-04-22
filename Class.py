class Account(object):
    def __init__(self,initial):
        self.balance=initial
    def deposit(self,amount):
        self.balance= self.balance+amount
    def withdraw(self,amount):
        self.balance= self.balance-amount
    def getbalance(self):
        return self.balance

Suj=Account(500)
Mayur=Account(1000.00)

Suj.deposit(100)
Suj.withdraw(200.5)

Mayur.deposit(432.34)
Mayur.withdraw(34.43)

print Suj.getbalance(), Mayur.getbalance()
