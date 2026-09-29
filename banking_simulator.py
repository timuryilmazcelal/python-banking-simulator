def show_balance(balance):
    print(f"Your balance is ₺{balance:.2f}")

def deposit():
    try:
        amount = float(input("Enter amount to deposit: "))

        if amount < 0:
            print("Sorry, you cannot deposit negative amount")
            return 0
        else:
            return amount
    except ValueError:
        print("Invalid input, try again with a valid number")
        return 0

def withdraw(balance):
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance :
            print("Insufficient funds")
            return 0
        elif amount < 0:
            print("Sorry, you cannot withdraw negative amount")
            return 0
        else:
            return amount
    except ValueError:
        print("Invalid input, try again with a valid number")
        return 0
def main():
    balance = 0
    is_running = True

    while is_running:
        print("****************")
        print("Banking Program")
        print("****************")
        print("1) Show balance")
        print("2) Deposit")
        print("3) Withdraw")
        print("4) Exit")
        print("************")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input, try again with a valid number")
            continue

        if choice == 1:
            show_balance(balance)
        elif choice == 2:
            balance += deposit()
        elif choice == 3:
            balance -= withdraw(balance)
        elif choice == 4:
            print("Thank you for choosing us")
            break
        else:
            print("************")
            print("That is not a valid choice")
            print("************")

if __name__ == "__main__":
    main()
