class Account:
    def __init__(self, acc_number, balance=0):
        self.acc_number = acc_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrew:", amount)
        else:
            print("Insufficient funds")

    def display(self):
        print(f"Account {self.acc_number} - Balance: {self.balance}")

class SavingsAccount(Account):
    def __init__(self, acc_number, balance=0):
        super().__init__(acc_number, balance)

# Example
acc = SavingsAccount("001", 1000)
acc.deposit(500)
acc.withdraw(300)
acc.display()
