from imaplib import Int2AP


class Bank():
    def __init__(self, owner, balance :int ):
        self.owner = owner
        self.balance  = balance 

    def deposit(self, plus_money : int):
        self.balance = self.balance + plus_money

    def withdraw(self, minus_money :int):
        if(minus_money > self.balance):
            print(f' Sorry, {self.owner} U cant take {minus_money} money, because it is  more than ur balalnce: {self.balance}')
        else:
            self.balance = self.balance - minus_money
        
    def show(self):
        print(f'{self.owner} ur balance is {self.balance}')
    

myname = str(input())
start_balance = int(input())
money = Bank(myname, start_balance)

pl_money = int(input())
money.deposit(pl_money)
money.show()

mi_money = int(input())
money.withdraw(mi_money)
money.show()