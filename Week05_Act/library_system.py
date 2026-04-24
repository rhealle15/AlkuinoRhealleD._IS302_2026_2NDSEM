class Book_rda:
    def __init__(self_rda, title_rda, author_rda, year_rda):
        self_rda.title_rda = title_rda
        self_rda.author_rda = author_rda
        self_rda.year_rda = year_rda
    
    def display_book_rda(self_rda):
        print("Title:", self_rda.title_rda)
        print("Author:", self_rda.author_rda)
        print("Year:", self_rda.year_rda)
        print()

print("----- LIBRARY MANAGEMENT SYSTEM -----\n")

# Create three book objects
book1_rda = Book_rda("Python Programming", "John Smith", 2022)
book2_rda = Book_rda("Data Science Basics", "Sarah Johnson", 2021)
book3_rda = Book_rda("Web Development Guide", "Mike Davis", 2023)

# Display book information
print("Book 1:")
book1_rda.display_book_rda()

print("Book 2:")
book2_rda.display_book_rda()

print("Book 3:")
book3_rda.display_book_rda()
