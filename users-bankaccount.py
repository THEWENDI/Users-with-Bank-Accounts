class BankAccount:
    accounts = []
    def __init__(self, int_rate = 0.01, balance = 0): 
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.accounts.append(self)
# your code here! (remember, instance attributes go here)
# don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if(self.balance - amount < 0):
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    
    def display_account_info(self):
        print("Balance: ",self.balance)
        return self

    def yield_interest(self):
        if(self.balance > 0):
            self.balance += self.balance * self.int_rate
        else:
            return 0 
        return self

    @classmethod    

    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

mr_x_bankaccount = BankAccount()
mr_y_bankaccount = BankAccount()

mr_x_bankaccount.deposit(300).deposit(300).deposit(300).withdraw(100).yield_interest().display_account_info()
mr_y_bankaccount.deposit(200).deposit(400).withdraw(700).withdraw(200).withdraw(200).withdraw(100).yield_interest().display_account_info()

BankAccount.print_all_accounts()

class User:
    def __init__(self, name):
        self.name = name
        self.account = BankAccount()
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        self.account.display_account_info()

tom = User("tom")

tom.make_deposit(1000).display_user_balance()