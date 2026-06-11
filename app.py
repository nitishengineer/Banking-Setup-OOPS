from abc import ABC, abstractmethod
from random import randint

# 1. Properly inherit from ABC
class Account(ABC):
    # 2. Added 'self' to all methods, removed unnecessary 'return 0'
    @abstractmethod
    def create_account(self, name: str, initial_deposit: float):
        pass

    @abstractmethod
    def authenticate(self, name: str, account_number: int) -> bool:
        pass

    @abstractmethod
    def withdraw(self, amount: float):
        pass

    @abstractmethod
    def deposit(self, amount: float):
        pass

    @abstractmethod
    def display_balance(self):
        pass


class SavingAccount(Account):
    def __init__(self):
        # 3. Changed key to integer for consistency with randint and int(input())
        self.saving_accounts = {11111: ["hemil", 100.0]} 
        self.current_account_number = None

    def create_account(self, name: str, initial_deposit: float):
        account_number = randint(10000, 99999)
        # Ensure the generated number is unique (simple check)
        while account_number in self.saving_accounts:
            account_number = randint(10000, 99999)
            
        self.saving_accounts[account_number] = [name, initial_deposit]
        print(f"Your account is successfully created. Your account number is: {account_number}")

    def authenticate(self, name: str, account_number: int) -> bool:
        # 4. Safe dictionary lookup prevents KeyError
        if account_number in self.saving_accounts:
            if self.saving_accounts[account_number][0] == name:
                print("Authentication Successful!")
                self.current_account_number = account_number
                return True
            else:
                print("Authentication failed: Name does not match.")
                return False
        else:
            print("Authentication failed: Account number not found.")
            return False

    def withdraw(self, amount: float):
        current_balance = self.saving_accounts[self.current_account_number][1]
        if amount > current_balance:
            print("Insufficient Balance.")    
        else:
            self.saving_accounts[self.current_account_number][1] -= amount
            print("Withdrawal Successful.") 
            self.display_balance()

    def deposit(self, amount: float):
        self.saving_accounts[self.current_account_number][1] += amount
        print("Deposit Successful.") 
        self.display_balance()

    def display_balance(self):
        balance = self.saving_accounts[self.current_account_number][1]
        print(f"Available balance: ${balance:.2f}")


# --- Main Application Loop ---
if __name__ == "__main__":
    saving_account = SavingAccount()

    while True:
        print("\n--- Main Menu ---")
        print("1. Open an account")
        print("2. Access existing account")
        print("3. Exit")
        
        try:
            user_choice = int(input("Enter your choice (1/2/3): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if user_choice == 1:
            name = input("Enter your name: ")
            try:
                initial_deposit = float(input("Enter initial deposit: $"))
                saving_account.create_account(name, initial_deposit)
            except ValueError:
                print("Invalid deposit amount.")

        elif user_choice == 2:
            name = input("Enter name: ")
            try:
                account_number = int(input("Enter account number: "))
            except ValueError:
                print("Invalid account number.")
                continue
                
            if saving_account.authenticate(name, account_number):
                # Nested menu for logged-in users
                while True:
                    print("\n--- Account Menu ---")
                    print("1. Withdraw")
                    print("2. Deposit")
                    print("3. Display Balance")
                    print("4. Logout / Exit to Main Menu")
                    
                    try:
                        action_choice = int(input("Enter your choice (1/2/3/4): "))
                    except ValueError:
                        print("Invalid input.")
                        continue

                    if action_choice == 1:
                        try:
                            withdraw_amount = float(input("Enter withdrawal amount: $"))
                            saving_account.withdraw(withdraw_amount)
                        except ValueError:
                            print("Invalid amount.")
                    elif action_choice == 2:
                        try:
                            deposit_amount = float(input("Enter deposit amount: $"))
                            saving_account.deposit(deposit_amount)
                        except ValueError:
                            print("Invalid amount.")
                    elif action_choice == 3:
                        saving_account.display_balance()
                    elif action_choice == 4:
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice.")

        elif user_choice == 3:
            print("Thank you for using our banking system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
