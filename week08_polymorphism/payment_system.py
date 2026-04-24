class Payment_rda:
    def pay_rda(self_rda):
        print("Processing payment")

class CashPayment_rda(Payment_rda):
    def pay_rda(self_rda):
        print("Payment made using cash")

class CardPayment_rda(Payment_rda):
    def pay_rda(self_rda):
        print("Payment made using credit card")

payments_rda = [CashPayment_rda(), CardPayment_rda()]
for p_rda in payments_rda:
    p_rda.pay_rda()