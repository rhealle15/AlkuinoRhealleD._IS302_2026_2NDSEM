try:
     number_RDA = int(input("Enter a number: "))
     result_ = 100 / number_RDA
     print("Result:", result_)
 
except ZeroDivisionError:
     print("Cannot divide by zero")
except ValueError:
     print("Invalid input")