def withdraw(value):
    balance = 500
    if balance >= value:
        print("Amount successfully withdrawn!")
        print("Withdraw your money at the till.")

    print("Thank you for being our customer, have a great day!\n")

def deposit(value):
    saldo = 500
    saldo += value
    print("Deposit successfully made!")

withdraw(100)
deposit(500)