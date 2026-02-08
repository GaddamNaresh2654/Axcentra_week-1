balance = 5000
correct_pin = "1234"

def check_balance():
    print(f"\nYour current balance is: ₹{balance}")

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: ₹"))
    if amount > 0:
        balance += amount
        print(f"₹{amount} deposited successfully.")
    else:
        print("Invalid amount!")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: ₹"))
    if amount <= 0:
        print("Invalid amount!")
    elif amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        print(f"₹{amount} withdrawn successfully.")

def atm_menu():
    while True:
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

pin = input("Enter your PIN: ")
if pin == correct_pin:
    print("Login successful!")
    atm_menu()
else:
    print("Incorrect PIN. Access denied!")
