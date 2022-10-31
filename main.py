class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        # your code here
    def withdraw(self, amount):
        self.balance -= amount
        # your code here
        
    def display_account_info(self):
        print(self.balance)
        
    def yield_interest(self):
        self.balance += self.balance * self.int_rate 
        # When you modify a variable you must put it at the front. So self.balance we are changing and adding the self.balance * self.int_rate
        # your code here
        






acct1 = BankAccount(.1, 100)
acct1.deposit(100)
acct1.deposit(100)
acct1.deposit(100)
acct1.withdraw(50)
acct1.yield_interest()
acct1.display_account_info() #No argument need due to self.


acct2 = BankAccount(.1, 200)
acct2.deposit(50)
acct2.deposit(200)
acct2.withdraw(20)
acct2.withdraw(20)
acct2.withdraw(20)
acct2.withdraw(20)
acct2.yield_interest()
acct2.display_account_info()

#SEE IF YOU CAN DO THE LAST ITEM BEFORE TURNING IN





