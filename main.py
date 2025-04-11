def input_int():
    """This function the starting balance from user by validating.
    This will ask user to input a correct integer rather than entering a string."""
    while True:
        try:
            start_price = int(input("Enter starting balance: "))
            if start_price <= 0:
                print("Please enter a value greater than 0.")
            else:
                return start_price
        except ValueError:
            print("Invalid input. Please enter an integer.")


def add_input_int():
    """This function the addition amount from user by validating.
    This will ask user to input a correct integer rather than entering a string"""
    while True:
        try:
            start_price = int(input("Add to balance: "))
            if start_price <= 0:
                print("Please enter a value greater than 0.")
            else:
                return start_price
        except ValueError:
            print("Invalid input. Please enter an integer.")


def sub_input_int():
    """This function the subtract amount from user by validating.
    This will ask user to input a correct integer rather than entering a string"""
    while True:
        try:
            start_price = int(input("Subtract from balance: "))
            if start_price <= 0:
                print("Please enter a value greater than 0.")
            else:
                return start_price
        except ValueError:
            print("Invalid input. Please enter an integer.")


def show_info(value_list, type_list, desired_type):
    """"This function will show the information of transactions"""
    count = 0
    total = 0
    for i in range(len(value_list)):
        if type_list[i] == desired_type: # Check if transaction equal to desired type.
            count = count + 1
            total = total + value_list[i]
    print(desired_type + " count: " + str(count))
    print(desired_type + " total: " + str(total))


def main():
    """Main function"""
    transaction_amounts = []
    transaction_types = []

    print("Welcome to Balance_Tracker!")
    balance = input_int()
    original_price = balance

    while True:
        print("\nCurrent balance: " + str(balance))
        print("Choose an option:")
        print(" [A]ddition")
        print(" [S]ubtraction")
        print(" [H]istory")
        print(" [I]nformation")
        print(" [Q]uit")

        choice = str(input("Enter your choice: "))

        if choice == 'a' or choice == 'A':
            amount = add_input_int()
            balance = balance + amount
            transaction_amounts.append(amount)
            transaction_types.append("Addition")
        elif choice == 's' or choice == 'S':
            amount = sub_input_int()
            balance = balance - amount
            transaction_amounts.append(amount)
            transaction_types.append("Subtraction")
        elif choice == 'h' or choice == 'H':
            print("\nTransaction History:")
            print("Starting balance was: " + str(original_price))
            for i in range(len(transaction_amounts)):
                print("Transaction " + str(i + 1) + ": " + transaction_types[i] + " of " + str(transaction_amounts[i])) # Prints the transaction type and transaction amount from two lists.
        elif choice == 'i' or choice == 'I':
            print("\nTransaction Information:")
            show_info(transaction_amounts, transaction_types, "Addition")
            show_info(transaction_amounts, transaction_types, "Subtraction")
        elif choice == 'q' or choice == 'Q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter A, S, H, I, or Q.")
main()
