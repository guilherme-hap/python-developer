class Account:
    def __init__(self, nbr_agency, balance=0):
        self._balance = balance
        self.nbr_agency = nbr_agency

    def deposit(self, value):
        # ...
        self._balance += value

    def withdraw(self, value):
        # ...
        self._balance -= value

    def display_balance(self):
        # ...
        return self._balance


account = Account("0001", 100)
account.deposit(100)
print(account.nbr_agency)
print(account.display_balance())