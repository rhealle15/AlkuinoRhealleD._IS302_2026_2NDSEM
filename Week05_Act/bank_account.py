class BankAccount_rda:
    def __init__(self_rda, account_name_rda, balance_rda):
        self_rda.account_name_rda = account_name_rda
        self_rda.balance_rda = balance_rda
    
    def deposit_rda(self_rda, amount_rda):
        self_rda.balance_rda += amount_rda
        print("Deposit successful")
    
    def withdraw_rda(self_rda, amount_rda):
        if amount_rda <= self_rda.balance_rda:
            self_rda.balance_rda -= amount_rda
            print("Withdrawal successful")
        else:
            print("Insufficient balance")
    
    def display_balance_rda(self_rda):
        print("Balance:", self_rda.balance_rda)

account_rda = BankAccount_rda("Juan", 5000)
account_rda.deposit_rda(1000)
account_rda.withdraw_rda(2000)
account_rda.display_balance_rda()
