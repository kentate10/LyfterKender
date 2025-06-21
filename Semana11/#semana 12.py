#semana 12

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0:
            if self.balance - amount < self.minimum_balance():
                print("Withdrawal denied. Balance would fall below minimum required.")
            else:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Withdrawal amount must be positive.")
 

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, min_balance=1000):
        super().__init__(account_number, balance) #Super para llamar al metodos de la clase padre y mandarle el account# y balance
        self.min_balance = min_balance
    def minimum_balance(self):
        return self.min_balance

    