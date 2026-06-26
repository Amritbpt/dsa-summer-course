class bank_account:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance

    def deposite(self,amount):
        self.balance+=amount
        return self.balance

    def withdraw(self,amount):
        if amount>self.balance:
            return "insufficient fund"
        else:
            self.balance-=amount

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"owner is :{self.owner}, balance is :{self.balance}"
    

acc=bank_account('Amrit',150)

print(acc.deposite(50))
