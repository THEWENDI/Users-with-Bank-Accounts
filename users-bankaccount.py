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
        return self.balance
        

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
        self.account = {
            "checking" : BankAccount(),
            "saving" : BankAccount()
        }
    
    def display_user_balance(self):
        print("User: ",self.name , "Checking Balance: ",self.account['checking'].display_account_info())

tom = User("tom")

tom.account['checking'].deposit(1000)
tom.display_user_balance()

# # answer:
# class BankAccount:
#     accounts = []
#     def __init__(self,int_rate,balance):
#         self.int_rate = int_rate
#         self.balance = balance
#         BankAccount.accounts.append(self)

#     def deposit(self, amount):
#         self.balance += amount
#         return self

#     def withdraw(self,amount):
#         if(self.balance - amount) >= 0:
#             self.balance -= amount
#         else:
#             print("Insufficient Funds: Charging a $5 fee")
#             self.balance -= 5
#         return self
    
#     def display_account_info(self):
#         return f"{self.balance}"

#     def yeild_interest(self):
#         if self.balance > 0:
#             self.balance += (self.balance * self.int_rate)
#         return self

#     @classmethod
#     def print_all_accounts(cls):
#         for account in cls.accounts:
#             account.display_account_info()


# class User:

#     def __init__(self, name):
#         self.name = name
#         self.account = {
#             "checking" : BankAccount(.02,1000),
#             "savings" : BankAccount(.05,3000)
#         }
        

#     def display_user_balance(self):
#         print(f"User: {self.name}, Checking Balance: {self.account['checking'].display_account_info()}")
#         print(f"User: {self.name}, Savings Balance: {self.account['savings'].display_account_info()}")
#         return self

#     def transfer_money(self,amount,user):
#         self.amount -= amount
#         user.amount += amount
#         self.display_user_balance()
#         user.display_user_balance()
#         return self


# adrien = User("Adrien")

# adrien.account['checking'].deposit(100)
# adrien.display_user_balance()