class Account:
    def __init__(self):
        self.number = None
        self.__pin = None
        self.__balance = 0
        self.__owner_details = None
        self.__overdraft_limit = 0
        self.__transactions = []
        self.__is_frozen = False
        self.__minimum_balance = 0

    def create_account(self, number, pin, owner_details, initial_balance=0):
        self.number = number
        self.__pin = pin
        self.__balance = initial_balance
        self.__owner_details = owner_details
        return "Account created successfully."

    def show_balance(self, pin):
        if pin == self.__pin:
            return self.__balance
        else:
            return "Wrong pin"

    def view_account_details(self, pin):
        if pin == self.__pin:
            return f"Account Number: {self.number} ,Account Owner: {self.__owner_details},Current Balance: {self.__balance}"
        else:
            return "Wrong pin"

    def change_account_owner(self, pin, new_owner_details):
        if pin == self.__pin:
            self.__owner_details = new_owner_details
            return "Account owner updated successfully."
        else:
            return "Wrong pin"

    def generate_account_statement(self, pin):
        if pin == self.__pin:
            statement = "Account Statement:"
            for transaction in self.__transactions:
                statement += f"{transaction}"
            return statement
        else:
            return "Wrong pin"

    def set_overdraft_limit(self, pin, limit):
        if pin == self.__pin:
            self.__overdraft_limit = limit
            return f"Overdraft limit set to {limit}."
        else:
            return "Wrong pin"

    def calculate_interest(self, pin, interest_rate):
        if pin == self.__pin:
            interest_amount = self.__balance * interest_rate
            self.__balance += interest_amount
            self.__transactions.append(f"Interest of {interest_amount} applied.")
            return f"Interest of {interest_amount} has been applied to your account."
        else:
            return "Wrong pin"

    def freeze_account(self, pin):
        if pin == self.__pin:
            self.__is_frozen = True
            return "Account has been frozen."
        else:
            return "Wrong pin"

    def unfreeze_account(self, pin):
        if pin == self.__pin:
            self.__is_frozen = False
            return "Account has been unfrozen."
        else:
            return "Wrong pin"

    def get_transaction_history(self, pin):
        if pin == self.__pin:
            return self.__transactions
        else:
            return "Wrong pin"

    def set_minimum_balance(self, pin, minimum_balance):
        if pin == self.__pin:
            self.__minimum_balance = minimum_balance
            return f"Minimum balance set to {minimum_balance}."
        else:
            return "Wrong pin"

    def transfer_funds(self, pin, recipient_account, amount):
        if pin == self.__pin and self.__balance >= amount + self.__minimum_balance:
            self.__balance -= amount
            recipient_account.__balance += amount
            self.__transactions.append(f"Transferred {amount} to account {recipient_account.number}")
            recipient_account.__transactions.append(f"Received {amount} from account {self.number}")
            return f"Transfer of {amount} completed successfully."
        else:
            return "Transfer failed. Insufficient funds or wrong pin."

    def close_account(self, pin):
        if pin == self.__pin:
            self.__balance = 0
            self.__owner_details = None
            self.__overdraft_limit = 0
            self.__transactions = []
            self.__is_frozen = False
            self.__minimum_balance = 0
            return "Account closed successfully."
        else:
            return "Wrong pin"

account = Account()
result = account.create_account("123456789", 1234, "Agnes Auma", 1000)
balance = account.show_balance(1234)
print(f"Current balance: {balance}") 

details = account.view_account_details(1234)
print(details)

result = account.change_account_owner(1234, "Reign Kaiden")
print(result)

result = account.set_overdraft_limit(1234, 500)
print(result)

result = account.calculate_interest(1234, 0.05)
print(result) 

result = account.freeze_account(1234)
print(result)  

result = account.unfreeze_account(1234)
print(result) 

result = account.close_account(1234)
print(result)

result = account.set_minimum_balance(1234, 100)
print(result)

sender_account = Account()
sender_account.create_account("123456789", 1234, "Agnes Auma", 1000)
recipient_account = Account()
recipient_account.create_account("987654321", 4321, "Vincent Omondi", 500)
result = sender_account.transfer_funds(1234, recipient_account, 200)
print(result)
