class BankAccount:
    MIN_BALANCE = 0
    def __init__(self, balance = 30000):
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= BankAccount.MIN_BALANCE:
            self.balance -= amount
    
    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, balance = 30000, interest_rate = 0.02):
        BankAccount.__init__(self, balance)
        self.interest_rate = interest_rate

    def compute_interest(self, compounding_frequency = 12, n_periods = 12):
        return self.balance * ((1 + self.interest_rate / compounding_frequency) ** n_periods) - self.balance


class CheckingAccount(BankAccount):
    def withdraw(self, amount = 1000, fee = 5):
        BankAccount.withdraw(self, amount + fee)

Account_A = BankAccount(50000)
Account_S = SavingsAccount(20000)
Account_C = CheckingAccount()

print('--------------------------------------')
print('Is Account_A a Savings Account? (True/False):', isinstance(Account_A, SavingsAccount))
print('Is Account_S a Bank Account? (True/False):', isinstance(Account_S, BankAccount))

print('--------------------------------------')
Account_S.compute_interest()
print('Account_S will have accrued %.2f balance' % Account_S.compute_interest())

print('--------------------------------------')
print('Account_C originally had %.2f in balances' % Account_C.get_balance())
Account_C.withdraw(10000)
print('Account_C has %.2f in balances after withdrawing'% Account_C.get_balance())



