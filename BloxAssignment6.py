# Banking works by transferring money from account A to account B. Most of the time account A is in one bank while account B is another bank.

# Suppose someone writes an implementation for such a money transfer.
# What are the test cases?
# What are the issues in such a system?
# What can we do to mitigate some of the issues ?
# Write the code yourself to demonstrate the mitigations.

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False

    def deposit(self, amount):
        self.balance += amount


def transfer_funds(source_account, target_account, amount):
    if source_account.withdraw(amount):
        target_account.deposit(amount)
        return True
    else:
        return False


# Account of sender
account_A = BankAccount("A12345", 1000)

# Account of receiver
account_B = BankAccount("B98765", 500)

transfer_amount = int(input('Enter Amount to transfer: '))

print("Before transfer:")
print("Account A balance:", account_A.balance)
print("Account B balance:", account_B.balance)

# Here we can get the status of the transaction
transaction_status = transfer_funds(account_A, account_B, transfer_amount)

print("\nTransfer status:", transaction_status)

print("\nAfter transfer:")
print("Account A balance:", account_A.balance)
print("Account B balance:", account_B.balance)
input()
