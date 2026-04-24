product_rda = input("Enter product name: ")
price_rda = input("Enter price: ")

with open("inventory.txt", "a") as file:
    file.write(product_rda + "," + price_rda + "\n")

print("Product saved successfully")