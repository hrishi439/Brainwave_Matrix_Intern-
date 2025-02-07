class ATM:
    def __init__(self, balance=0):
        self.balance = balance
        self.pin = self.set_pin() 

    def set_pin(self):
            pin = input("Set your 4-digit PIN: ")
            if pin.isdigit() and len(pin) == 4:
                print("PIN set successfully!\n")
                return int(pin)
            else:
                print("Invalid PIN. Please enter exactly 4 digits.")

    def authenticate(self):
        attempts = 3
        while attempts > 0:
            entered_pin = input("Enter your PIN: ")
            if entered_pin.isdigit() and int(entered_pin) == self.pin:
                print("Authentication successful!\n")
                return True
            else:
                attempts -= 1
                print(f"Incorrect PIN. {attempts} attempts remaining.")
        print("Authentication failed. Exiting.")
        return False

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}\n")

    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}\n")
        else:
            print("Invalid deposit amount.\n")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn ${amount}. New balance: ${self.balance}\n")
        else:
            print("Invalid withdrawal amount or insufficient funds.\n")

    def start(self):
        if not self.authenticate():
            return
        
        while True:
            print("ATM Menu:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            
            choice = input("Choose an option: ")
            
            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                print("Thank you for using our ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.\n")


atm = ATM(balance=1000)  # Default balance of $1000
atm.start()
