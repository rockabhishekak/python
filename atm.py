def atm_simulation():
    balance = 1000  # Initial account balance
    pin = "1234"    # Pre-set PIN for authentication

    print("Welcome to the Python ATM!")

    # PIN Authentication
    attempts = 0
    while attempts < 3:
        entered_pin = input("Enter your 4-digit PIN: ")
        if entered_pin == pin:
            print("PIN accepted. Access granted.")
            break
        else:
            attempts += 1
            print(f"Incorrect PIN. {3 - attempts} attempts remaining.")
    else:
        print("Too many incorrect attempts. Your card is blocked.")
        return

    # Main ATM Menu
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print(f"Your current balance is: ${balance:.2f}")
        elif choice == '2':
            try:
                deposit_amount = float(input("Enter amount to deposit: $"))
                if deposit_amount > 0:
                    balance += deposit_amount
                    print(f"${deposit_amount:.2f} deposited successfully.")
                    print(f"New balance: ${balance:.2f}")
                else:
                    print("Deposit amount must be positive.")
            except ValueError:
                print("Invalid input. Please enter a numerical amount.")
        elif choice == '3':
            try:
                withdraw_amount = float(input("Enter amount to withdraw: $"))
                if withdraw_amount > 0:
                    if balance >= withdraw_amount:
                        balance -= withdraw_amount
                        print(f"${withdraw_amount:.2f} withdrawn successfully.")
                        print(f"New balance: ${balance:.2f}")
                    else:
                        print("Insufficient funds.")
                else:
                    print("Withdrawal amount must be positive.")
            except ValueError:
                print("Invalid input. Please enter a numerical amount.")
        elif choice == '4':
            print("Thank you for using the Python ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Run the ATM simulation
atm_simulation()