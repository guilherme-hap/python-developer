import textwrap
from abc import ABC
from datetime import datetime

class Client:
    def __init__(self, address):
        self.address = address
        self.accounts = []

    def make_transaction(self, account, transaction):
        transaction.register(account)

    def add_account(self, account):
        self.accounts.append(account)


class Individual(Client):
    def __init__(self, name, birth_date, cpf, address):
        super().__init__(address)
        self.name = name
        self.birth_date = birth_date
        self.cpf = cpf


class Account:
    def __init__(self, account_number, client):
        self._balance = 0
        self._account_number = account_number
        self._agency = "0001"
        self._client = client
        self._history = History()
    
    @classmethod
    def create_account(cls, client, account_number):
        return cls(client, account_number)
    
    @property
    def balance(self):
        return self._balance

    @property
    def account_number(self):
        return self._account_number

    @property
    def agency(self):
        return self._agency

    @property
    def client(self):
        return self._client

    @property
    def history(self):
        return self._history
    
    def withdrawal(self, value):
        balance = self.balance
        exceeded_balance = value > balance

        if exceeded_balance:
            print("\n@@@ Operation failed! You don't have enough balance. @@@")

        elif value > 0:
            self._balance -= value
            print("\n=== Withdrawal successfull! ===")
            return True

        else:
            print("\n@@@ Operation failed! The value entered is invalid. @@@")
        
        return False
    
    def deposit(self, value):
        if value > 0:
            self._balance += value
            print("\n=== Deposit successfully made! ===")
        else:
            print("\n@@@ Operation failed! The value entered is invalid. @@@")
            return False
        
        return True


class Checking_account(Account):
    def __init__(self, account_number, client, limit=500, withdrawals_limit=3):
        super().__init__(account_number, client)
        self._limit = limit
        self._withdrawals_limit = withdrawals_limit

    def withdrawal(self, value):
        withdrawal_count = len([transaction for transaction in self.history.transactions if transaction["type"] == Withdrawal.__name__])

        exceeded_limit = value > self._limit
        exceeded_withdrawals = withdrawal_count >= self._withdrawals_limit

        if exceeded_limit:
            print("\n@@@ Operation failed! The withdrawal amount exceeds the limit. @@@")

        elif exceeded_withdrawals:
            print("\n@@@ Operation failed! Maximum number of withdrawals exceeded. @@@")

        else:
            return super().withdrawal(value)

        return False

    def __str__(self):
        return f"""\
            Agency:\t{self.agency}
            C/C:\t\t{Account.account_number}
            Owner:\t{self.client}
        """


class History(Account): 
    def __init__(self):
        self._transactions = []

    @property
    def transactions(self):
        return self._transactions

    def add_transaction(self, transaction):
        self._transactions.append(
            {
                "type": transaction.__class__.__name__,
                "value": transaction.value,
                "date": datetime.now().strftime("%d-%m-%Y"),
            }
        )


class Transaction(ABC):
    @property
    def value(self):
        pass

    def register(self):
        pass


class Withdrawal(Transaction):
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value
    
    def register(self, account):
        transaction_successful = account.withdrawal(self.value)

        if transaction_successful:
            account.history.add_transaction(self)


class Deposit(Transaction):
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value
    
    def register(self, account):
        transaction_successful = account.deposit(self.value)

        if transaction_successful:
            account.history.add_transaction(self)


def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDeposit
    [w]\tWithdraw
    [s]\tDisplay statement
    [ca]\tCreate account
    [la]\tList accounts
    [cc]\tCreate client
    [e]\tExit
    => """
    return input(textwrap.dedent(menu))


def filter_clients(cpf, clients):
    filtered_clients = [client for client in clients if client.cpf == cpf]
    return filtered_clients[0] if filtered_clients else None


def recover_client_account(client):
    if not client.accounts:
        print("\n@@@ Client doesn't own an account! @@@")
        return

    return client.accounts[0]


def deposit(clients):
    cpf = input("Enter your CPF (numbers only): ")
    client = filter_clients(cpf, clients)

    if not client:
        print("\n@@@ Client not found! @@@")
        return

    value = float(input("Enter the deposit amount: "))
    transaction = Deposit(value)

    account = recover_client_account(client)
    if not account:
        return

    client.make_transaction(account, transaction)


def withdraw(clients):
    cpf = input("Enter your CPF (numbers only): ")
    client = filter_clients(cpf, clients)

    if not client:
        print("\n@@@ Client not found! @@@")
        return

    value = float(input("Enter the withdrawal amount: "))
    transaction = Withdrawal(value)

    account = recover_client_account(client)
    if not account:
        return

    client.make_transaction(account, transaction)


def display_statement(clients):
    cpf = input("Enter your CPF (numbers only): ")
    client = filter_clients(cpf, clients)

    if not client:
        print("\n@@@ Client not found! @@@")
        return

    account = recover_client_account(client)
    if not account:
        return

    print("\n================ STATEMENT ================")
    transactions = account.history.transactions

    statement = ""
    if not transactions:
        statement = "No movements were made."

    else:
        for transaction in transactions:
            statement += f"\n{transaction['type']}:\n\tR$ {transaction['value']:.2f}"

    print(statement)
    print(f"\nBalance:\tR$ {account.balance:.2f}")
    print("==========================================")


def create_client(clients):
    cpf = input("Enter your CPF (numbers only): ")
    client = filter_clients(cpf, clients)

    if client:
        print("\n@@@ There is already a user with this CPF! @@@")
        return
    
    name = input("Enter your full name: ")
    birth_date = input("Enter your birth date (dd-mm-yyyy): ")
    address = input("Enter your address (street, number - neighborhood - city/state abbreviation): ")

    client = Individual(name=name, birth_date=birth_date, cpf=cpf, address=address)

    clients.append(client)

    print("=== Client registered successfully! ===")


def create_account(account_number, clients, accounts):
    cpf = input("Enter your CPF (numbers only): ")
    client = filter_clients(cpf, clients)

    if not client:
        print("\n@@@ Client not found, account creation flow over! @@@")
        return

    account = Checking_account.create_account(client=client, account_number=account_number)
    accounts.append(account)
    client.accounts.append(account)

    print("\n=== Account created successfully! ===")


def list_accounts(accounts):
    for account in accounts:
        print("=" * 100)
        print(textwrap.dedent(str(account)))


def main():
    clients = []
    accounts = []

    while True:
        option = menu()

        if option == "d":
            deposit(clients)

        elif option == "w":
            withdraw(clients)

        elif option == "s":
            display_statement(clients)

        elif option == "cc":
            create_client(clients)

        elif option == "ca":
            account_number = len(accounts) + 1
            create_account(account_number, clients, accounts)

        elif option == "la":
            list_accounts(accounts)

        elif option == "e":
            break

        else:
            print("\n@@@ Invalid operation, please select the desired operation again. @@@")


main()