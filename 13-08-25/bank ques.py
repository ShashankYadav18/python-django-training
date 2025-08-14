import random

# Parent Class
class BankAccount:
    def __init__(self, name, balance):
        self.account_holder = name
        self.balance = balance
        self.account_number = self.generate_account_number()

    def generate_account_number(self):
        return "".join([str(random.randint(0, 9)) for _ in range(16)])

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")

    def display_balance(self):
        print(f"Current Balance: ₹{self.balance:.2f}")


# SavingAccount (Child)
class SavingAccount(BankAccount):
    interest_rate = 4  # in %

    def apply_interest(self):
        interest = (self.balance * SavingAccount.interest_rate) / 100
        self.balance += interest
        print(f"Interest of ₹{interest:.2f} applied at {SavingAccount.interest_rate}% rate.")


# CurrentAccount (Child)
class CurrentAccount(BankAccount):
    overdraft_limit = 20000  # Fixed

    def withdraw(self, amount):
        if amount > 0 and (self.balance - amount) >= -CurrentAccount.overdraft_limit:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Withdrawal exceeds overdraft limit or invalid amount.")


# ---------------- Main Program ----------------
print("Enter account type (saving/current): ", end="")
acc_type = input().strip().lower()
name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))

if acc_type == "saving":
    account = SavingAccount(name, balance)
    print("\nYour account has been created successfully.")
    print(f"Account Number: {account.account_number}")
    print(f"Interest Rate (Bank Fixed): {SavingAccount.interest_rate}%")
elif acc_type == "current":
    account = CurrentAccount(name, balance)
    print("\nYour account has been created successfully.")
    print(f"Account Number: {account.account_number}")
    print(f"Overdraft Limit (Bank Fixed): ₹{CurrentAccount.overdraft_limit}")
else:
    print("Invalid account type selected.")
    exit()

# Menu-driven loop
while True:
    print("\nChoose operation:")
    if isinstance(account, SavingAccount):
        print("1. Deposit\n2. Withdraw\n3. Display Balance\n4. Apply Interest\n5. Exit")
    else:
        print("1. Deposit\n2. Withdraw\n3. Display Balance\n5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amt = float(input("Enter amount to deposit: "))
        account.deposit(amt)

    elif choice == "2":
        amt = float(input("Enter amount to withdraw: "))
        account.withdraw(amt)

    elif choice == "3":
        account.display_balance()

    elif choice == "4" and isinstance(account, SavingAccount):
        account.apply_interest()

    elif choice == "5":
        print("Thank you for banking with us!")
        break
    else:
        print("Invalid choice. Try again.")
