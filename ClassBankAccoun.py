class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0  # Initialize balance to 0 by default

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account Number: {self.account_number}, Balance: {self.balance}"

# Create an instance of the BankAccount class
account = BankAccount("123456789")

# Deposit some money
account.deposit(1000)

# Withdraw some money
account.withdraw(250)

# Display the account's balance
print(account.get_balance())

# Print the account's details using the __str__ method
print(account)
