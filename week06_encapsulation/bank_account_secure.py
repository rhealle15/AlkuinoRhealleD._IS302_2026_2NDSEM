class BankAccount_rda:
    def __init__(self_rda, balance_rda):
        self_rda.__balance = balance_rda

    def deposit_rda(self_rda, amount_rda):
        self_rda.__balance += amount_rda

    def withdraw_rda(self_rda, amount_rda):
        if amount_rda <= self_rda.__balance:
            self_rda.__balance -= amount_rda
        else:
            print("Insufficient funds")

    def get_balance_rda(self_rda):
        return self_rda.__balance

account_rda = BankAccount_rda(5000)
account_rda.deposit_rda(1000)
account_rda.withdraw_rda(2000)
print("Balance_rda:", account_rda.get_balance_rda())