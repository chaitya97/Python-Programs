class BankingSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_balance):
        if account_number in self.accounts:
            raise ValueError("Account already exists.")
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.accounts[account_number] = initial_balance

    def deposit(self, account_number, amount):
        if account_number not in self.accounts:
            raise ValueError("Account does not exist.")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.accounts[account_number] += amount

    def withdraw(self, account_number, amount):
        if account_number not in self.accounts:
            raise ValueError("Account does not exist.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.accounts[account_number] < amount:
            raise ValueError("Insufficient funds.")
        self.accounts[account_number] -= amount

    def get_balance(self, account_number):
        if account_number not in self.accounts:
            raise ValueError("Account does not exist.")
        return self.accounts[account_number]
    
    def transfer(self, from_account, to_account, amount):
        if from_account not in self.accounts:
            raise ValueError("Source account does not exist.")
        if to_account not in self.accounts:
            raise ValueError("Destination account does not exist.")
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        if self.accounts[from_account] < amount:
            raise ValueError("Insufficient funds in source account.")
        
        self.accounts[from_account] -= amount
        self.accounts[to_account] += amount
    
# Example usage 
if __name__ == "__main__":
    bank = BankingSystem()
    print("Welcome to the Banking System")
    while True:
        print("\nMenu:")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transfer")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            while True:
                account_number = input("Enter account number: ")
                try:
                    if len(account_number) <4 or len(account_number) > 6:
                        raise ValueError("Account number must be between 4 and 6 digits.")
                    if not account_number.isdigit():
                        raise ValueError("Account number must be numeric.")
                    break
                    
                except ValueError as e:
                    print(e)

            while True:
                initial_balance = float(input("Enter initial balance: "))
                try:
                    if not initial_balance >1000:
                        raise ValueError("Minimum initial deposit shoud me more than 100 to open an account")
                    break
                    
                except ValueError as e:
                    print(e)

            bank.create_account(account_number, initial_balance)
            print(f"Account {account_number} created with balance {initial_balance}.")

        elif choice == '2':
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            try:
                bank.deposit(account_number, amount)
                print(f"Deposited {amount} to account {account_number}.")
            except ValueError as e:
                print(e)
        
        