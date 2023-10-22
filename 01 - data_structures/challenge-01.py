import textwrap


def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDeposit
    [w]\tWithdraw
    [s]\tDisplay statement
    [ru]\tRegister user
    [ca]\tCreate account
    [la]\tList accounts
    [e]\tExit
    => """
    return input(textwrap.dedent(menu))

def display_statement(balance, /, *, statement):
    print("\n================ STATEMENT ================")
    print("No movements were made." if not statement else statement)
    print(f"\nBalance:\tR$ {balance:.2f}")
    print("===========================================")

def deposit(balance, value, statement, /):
    if value > 0:
        balance += value
        statement += f"Deposit:\tR$ {value:.2f}\n"
        print("\n=== Deposit successfully made! ===")

    else:
        print("\n@@@ Operation failed! The value entered is invalid. @@@")

    return balance, statement

def withdrawal(*, balance, value, statement, limit, number_of_withdrawals, limit_of_withdrawals):
    exceeded_balance = value > balance
    exceeded_limit = value > limit
    exceeded_withdrawals = number_of_withdrawals >= limit_of_withdrawals

    if exceeded_balance:
        print("\n@@@ Operation failed! You don't have enough balance. @@@")

    elif exceeded_limit:
        print("\n@@@ Operation failed! The withdrawal amount exceeds the limit. @@@")

    elif exceeded_withdrawals:
        print("\n@@@ Operation failed! Maximum number of withdrawals exceeded. @@@")

    elif value > 0:
        balance -= value
        statement += f"Withdrawal:\tR$ {value:.2f}\n"
        number_of_withdrawals += 1
        print("\n=== Withdrawal successfull! ===")

    else:
        print("\n@@@ Operation failed! The value entered is invalid. @@@")
    
    return balance, statement

def register_user(users):
    cpf = input("Enter your CPF (numbers only): ")
    user = filter_users(cpf, users)

    if user:
        print("\n@@@ There is already a user with this CPF! @@@")
        return
    
    name = input("Enter your full name: ")
    birth_date = input("Enter your birth date (dd-mm-yyyy): ")
    address = input("Enter your address (street, number - neighborhood - city/state abbreviation): ")

    users.append({"name": name, "birth_date": birth_date, "cpf": cpf,"address": address})

    print("=== User registered successfully! ===")

def filter_users(cpf, users):
    filtered_users = [user for user in users if user["cpf"] == cpf]
    return filtered_users[0] if filtered_users else None

def create_account(agency, account_number, users):
    cpf = input("Enter your CPF (numbers only): ")
    user = filter_users(cpf, users)

    if user:
        print("\n=== Account successfully created! ===")
        return {"agency": agency, "account_number": account_number, "user": user}
    
    print("\n@@@ User not found, account creation flow over! @@@")

def list_accounts(accounts):
    for account in accounts:
        line = f"""\
            Agency:\t{account['agency']}
            C/C:\t{account['account_number']}
            Owner:\t{account['user']['name']}
        """
        print("=" * 100)
        print(textwrap.dedent(line))

def main():
    LIMIT_OF_WITHDRAWALS = 3
    AGENCY = "0001"

    balance = 0
    limit = 500
    statement = ""
    number_of_withdrawals = 0
    users = []
    accounts = []

    while True:

        option = menu()

        if option == "d":
            value = float(input("Enter the deposit amount: "))

            balance, statement = deposit(balance, value, statement)

        elif option == "w":
            value = float(input("Enter the withdrawal amount: "))

            balance, statement = withdrawal(
                balance=balance,
                value=value,
                statement=statement,
                limit=limit,
                number_of_withdrawals=number_of_withdrawals,
                limit_of_withdrawals=LIMIT_OF_WITHDRAWALS
            )

        elif option == "s":
            display_statement(balance, statement=statement)

        elif option == "ru":
            register_user(users)

        elif option == "ca":
            account_number = len(accounts) + 1
            account = create_account(AGENCY, account_number, users)

            if account:
                accounts.append(account)
            
        elif option == "la":
            list_accounts(accounts)

        elif option == "e":
            break

        else:
            print("Invalid operation, please select the desired operation again.")

main()