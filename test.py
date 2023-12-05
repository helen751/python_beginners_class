import os

# Data storage
accounts = {}
account_number_generator = 1000  # Starting account number


def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def open_account():
    global account_number_generator
    clear_screen()
    print("**** Open Account ****")

    # Get user details
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender: ")
    phone_number = input("Enter Phone Number (numbers only): ")

    # Validate age and phone number
    if age < 15 or not phone_number.isdigit():
        print("Sorry, you are not eligible to open an account.")
        return

    # Create account
    account_number = account_number_generator
    account_number_generator += 1
    balance = 0.00

    # Store account details
    accounts[account_number] = {
        'first_name': first_name,
        'last_name': last_name,
        'age': age,
        'gender': gender,
        'phone_number': phone_number,
        'balance': balance
    }

    print(f"Account successfully created!\nAccount Number: {account_number}\nBalance: {balance}")

    another_operation()


def withdrawal():
    clear_screen()
    print("**** Withdrawal ****")

    # Get user account number
    account_number = int(input("Enter Account Number: "))

    if account_number not in accounts:
        print("Account not found.")
        return

    # Get withdrawal amount
    amount = float(input("Enter Withdrawal Amount: "))

    # Check if sufficient funds
    if amount > accounts[account_number]['balance']:
        print("Insufficient funds.")
    else:
        accounts[account_number]['balance'] -= amount
        print(f"Withdrawal successful!\nUpdated Balance: {accounts[account_number]['balance']}")

    another_operation()


def deposit():
    clear_screen()
    print("**** Deposit ****")

    # Get user account number
    account_number = int(input("Enter Account Number: "))

    if account_number not in accounts:
        print("Account not found.")
        return

    # Get deposit amount
    amount = float(input("Enter Deposit Amount: "))

    # Deposit amount
    accounts[account_number]['balance'] += amount
    print(f"Deposit successful!\nUpdated Balance: {accounts[account_number]['balance']}")

    another_operation()


def loan():
    clear_screen()
    print("**** Loan ****")

    # Get user account number
    account_number = int(input("Enter Account Number: "))

    if account_number not in accounts:
        print("Account not found.")
        return

    # Check eligibility for loan
    if accounts[account_number]['balance'] >= 5000:
        # Get loan amount
        loan_amount = float(input("Enter Loan Amount: "))

        # Credit loan amount to the account
        accounts[account_number]['balance'] += loan_amount
        print(f"Loan credited to your account!\nUpdated Balance: {accounts[account_number]['balance']}")
    else:
        print("Sorry, you are not eligible for a loan.")

    another_operation()


def another_operation():
    choice = input("\nDo you want to perform another operation? (yes/no): ").lower()
    if choice == 'yes':
        main_menu()
    else:
        print("Thank you for using Helpy Bank App!")


def main_menu():
    clear_screen()
    print("**** VICMAS Bank App ****")
    print("1. Open Account")
    print("2. Withdrawal")
    print("3. Deposit")
    print("4. Loan")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        open_account()
    elif choice == '2':
        withdrawal()
    elif choice == '3':
        deposit()
    elif choice == '4':
        loan()
    elif choice == '5':
        print("Exiting VICMAS Bank App. Goodbye!")
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
        main_menu()


if __name__ == "__main__":
    main_menu()