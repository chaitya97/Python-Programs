class BankingSystem:
    def __init__(self):
        self.accounts = {
            
            "11111": 1000.0,
            "22222": 2000.0,
            "33333": 3000.0,
            "44444": 4000.0,
            "55555": 5000.0

        }

    def create_account(self, account_number, initial_balance):
        errors = []

        if not account_number.isdigit():
            errors.append(f"Error: Provided Account number {account_number}. It must be numeric.")
        
        if len(account_number)<=4 or len(account_number)>=6:
            errors.append(f"Error: Provided Account number {account_number}. Account number should be of 5 digits.")
        
        if account_number in self.accounts:
            errors.append(f"Error: Provided Account number {account_number}. Account already exists. Can't create with the same account number")
        
        if initial_balance < 1000:
            errors.append("Error: Initial deposit must be minimum 1000.")
        
        if errors:
            raise ValueError("\n".join(errors))
        
        self.accounts[account_number] = initial_balance

    def deposit(self, account_number, amount):
        errors = []
        if account_number not in self.accounts:
            errors.append("Account number does not exist with the bank.")
        if amount <= 0:
            errors.append("Deposit amount must be positive.")
        
        if errors:
            raise ValueError("\n".join(errors))
        
        self.accounts[account_number] += amount

    def withdraw(self, account_number, amount):
        errors = []
        if account_number not in self.accounts:
            errors.append("Account does not exist.")
        if amount <= 0:
            errors.append("Withdrawal amount must be positive.")
        if self.accounts[account_number] < amount:
            errors.append("Insufficient funds.")
        
        if errors:
            raise ValueError("\n".join(errors))
        
        self.accounts[account_number] -= amount

    def get_balance(self, account_number):
        if account_number not in self.accounts:
            raise ValueError(f"Error: Provided Account number {account_number} does not exist.")
        return self.accounts[account_number]
    
    def transfer(self, from_account, to_account, amount):
        errors = []
        if from_account not in self.accounts:
            errors.append(f"Error: Source account: {from_account} does not exist.")
        if to_account not in self.accounts:
            errors.append(f"Destination account: {to_account} does not exist.")
        if amount <= 0:
            errors.append("Transfer amount must be positive.")
        if from_account in self.accounts and amount > 0:
            if self.accounts[from_account] < amount:
                errors.append("Error: Insufficient funds in source account.")
            elif self.accounts[from_account] - amount < 1000:
                errors.append("Error: Transfer would reduce source account below minimum required balance of 1000.")
        
        if errors:
            raise ValueError("\n".join(errors))
        
        self.accounts[from_account] -= amount
        self.accounts[to_account] += amount
    
# Example usage 
if __name__ == "__main__":
    bank = BankingSystem()
    print("")
    print("------------------------------")
    print("Welcome to the Banking System")
    print("------------------------------")
    while True:
        print("\n---------------------------")
        print("|   Menu:                 |")
        print("|   1. Create Account     |")
        print("|   2. Deposit            |")
        print("|   3. Withdraw           |")
        print("|   4. Check Balance      |")
        print("|   5. Transfer           |")
        print("|   6. Exit               |")
        print("---------------------------")
        
        print("")
        choice = input("Enter your choice: ")
        print("")

        if choice == '1':
            print("----------------------------------------------------")
            print("Guidlines to open an account:")
            print("1. Account must be numeric and should be of 5 digits")
            print("2. Minimum amount to open an account is 1000.")
            print("")
            account_number = input("Enter account number: ")
            initial_balance = float(input("Enter initial balance: "))
            print("")
            
            try:
                bank.create_account(account_number, initial_balance)
                print(f"Success: Account {account_number} created with balance {initial_balance}.")
            
            except ValueError as e:
                print(e)
                print("Error: Account was not created.")
        
        elif choice == '2':
            account_number = input("Enter account number for the deposit: ")
            amount = float(input("Enter amount to deposit: "))
            print("")
            
            try:
                bank.deposit(account_number, amount)
                print(f"Success: Deposited {amount} to account {account_number}.")
            
            except ValueError as e:
                print(e)
                print("Error: Amount didn't get deposited in the account.")
        
        elif choice == '3':
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            print("")
            try:
                bank.withdraw(account_number, amount)
                print(f"Success: Withdrew {amount} from account {account_number}.")
            except ValueError as e:
                print(e)
                print("Error: Couldn't perform withdaw from the account.")
        
        elif choice == '4':
            account_number = input("Enter account number: ")
            print("")
            try:
                balance = bank.get_balance(account_number)
                print(f"Success: Balance for account {account_number}: {balance}")
            except ValueError as e:
                print(e)
                print("Error: Coundn't check the balance of the account.")
        
        elif choice == '5':
            from_account = input("Enter source account number: ")
            to_account = input("Enter destination account number: ")
            amount = float(input("Enter amount to transfer: "))
            print("")
            
            try:
                bank.transfer(from_account, to_account, amount)
                print(f"Transferred {amount} from {from_account} to {to_account}.")
            
            except ValueError as e:
                print(e)
                print("Error: Transfer could not be possible.")
        
        elif choice == '6':
            print("Exiting the Banking System.")
            break
        
        else:
            print("Invalid choice. Please try again.")