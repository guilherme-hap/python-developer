menu = """

[d] Deposit
[w] Withdraw
[s] Bank statement
[e] Exit

=> """

balance = 0
limit = 500
bank_statement = ""
number_of_withdrawals = 0
LIMIT_OF_WITHDRAWALS = 3

while True:

    option = input(menu)

    if option == "d":
        value = float(input("Enter the deposit amount: "))
 
        if value > 0:
            balance += value
            bank_statement += f"Deposit: R$ {value:.2f}\n"

        else:
            print("Operation failed! The value entered is invalid.")

    elif option == "w":
        value = float(input("Enter the withdrawal amount: "))

        exceeded_balance = value > balance

        exceeded_limit = value > limit

        exceeded_withdrawals = number_of_withdrawals >= LIMIT_OF_WITHDRAWALS

        if exceeded_balance:
            print("Operation failed! You don't have enough balance.")

        elif exceeded_limit:
            print("Operation failed! The withdrawal amount exceeds the limit.")

        elif exceeded_withdrawals:
            print("Operation failed! Maximum number of withdrawals exceeded.")

        elif value > 0:
            balance -= value
            bank_statement += f"Withdrawal: R$ {value:.2f}\n"
            number_of_withdrawals += 1

        else:
            print("Operation failed! The value entered is invalid.")

    elif option == "s":
        print("\n================ EXTRATO ================")
        print("No movements were made." if not bank_statement else bank_statement)
        print(f"\nBalance: R$ {balance:.2f}")
        print("==========================================")

    elif option == "e":
        break

    else:
        print("Invalid operation, please select the desired operation again.")