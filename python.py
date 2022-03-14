class BankAccount:
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
    
    def make_deposit(self,amount):
        self.balance += amount
        return self

    def make_withdrawal(self,amount):
        if (self.balance - amount)>= 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        return f"{self.balance}"

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self  

class User:
    def __init__(self,name):
        self.name = name
        self.account = BankAccount(0.5, 1000) 

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account.display_account_info()}")
        return self

    def transfer_money(self,amount,user):
        self.amount -= amount
        self.amount += amount
        self.display_user_balance()
        
jp = User("Jp")

jp.account.make_deposit(5000)
jp.display_user_balance()

