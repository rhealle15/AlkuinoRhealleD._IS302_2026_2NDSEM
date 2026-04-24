class Product_rda:
    def __init__(self_rda, name_rda, price_rda, quantity_rda):
        self_rda.__name = name_rda
        self_rda.__price = price_rda
        self_rda.__quantity = quantity_rda

    def get_product_info_rda(self_rda):
        print("Product:", self_rda.__name)
        print("Price:", self_rda.__price)
        print("Quantity:", self_rda.__quantity)

    def update_quantity_rda(self_rda, new_quantity_rda):
        if new_quantity_rda >= 0:
            self_rda.__quantity = new_quantity_rda

    def update_price_rda(self_rda, new_price_rda):
        if new_price_rda > 0:
            self_rda.__price = new_price_rda

# Example usage
product_rda = Product_rda("Laptop", 45000, 10)
product_rda.get_product_info_rda()