import random

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_number = self.generate_account_number()
        self.account_holder = account_holder
        self.balance = balance

    @staticmethod
    def generate_account_number():
        return str(random.randint(10**15, (10**16) - 1))

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrawn ₹{amount}. New balance: ₹{self.balance}")

    def display_balance(self):
        print(f"Current Balance: ₹{self.balance}")


class SavingAccount(BankAccount):

    interest_rate = 4

    def apply_interest(self):
        interest = (self.balance * SavingAccount.interest_rate) / 100
        self.balance += interest
        print(f"Interest of ₹{interest:.2f} applied at {SavingAccount.interest_rate}%.")
        self.display_balance()


class CurrentAccount(BankAccount):
    overdraft_limit = 50000

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if self.balance - amount < -CurrentAccount.overdraft_limit:
            print("Overdraft limit exceeded.")
        else:
            self.balance -= amount
            print(f"Withdrawn ₹{amount}. New balance: ₹{self.balance}")


def main():
    print("Welcome to the Bank System")
    account_type = input("Enter account type (saving/current): ").strip().lower()
    name = input("Enter account holder name: ")
    initial_balance = float(input("Enter initial balance: "))

    if account_type == "saving":
        account = SavingAccount(name, initial_balance)
        print(f"Saving Account created successfully.\nAccount Number: {account.account_number}")
        print(f"Bank Fixed Interest Rate: {SavingAccount.interest_rate}%")
    elif account_type == "current":
        account = CurrentAccount(name, initial_balance)
        print(f"Current Account created successfully.\nAccount Number: {account.account_number}")
        print(f"Bank Fixed Overdraft Limit: ₹{CurrentAccount.overdraft_limit}")
    else:
        print("Invalid account type.")
        return

    while True:
        print("\nChoose an operation:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Balance")
        if account_type == "saving":
            print("4. Apply Interest (Bank-decided rate)")
            print("5. Exit")
        else:
            print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "3":
            account.display_balance()
        elif account_type == "saving" and choice == "4":
            account.apply_interest()
        elif (account_type == "saving" and choice == "5") or (account_type == "current" and choice == "4"):
            print("Thank you for banking with us.")
            break
        else:
            print("Invalid choice.")


main()
