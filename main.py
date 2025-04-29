from Library import Library
from Book import Book

# create book object for a library
book_obj  = Book(100,"The Hidden Power", 'Shathyajit',True)
book_obj1 = Book(102,"Positive Thinker", 'Radhanath',True)
book_obj2 = Book(103,"Positive philosophy", 'Radhanath',True)
book_obj3 = Book(104,"Rich dad poor dad", 'Roburt Toru',True)
book_obj4 = Book(105,"Sheser Kobitha", 'Robindronath Takur',True)

# Insert book obj to the library class using entry_book
Library.entry_book(book_obj)
Library.entry_book(book_obj1)
Library.entry_book(book_obj2)
Library.entry_book(book_obj3)
Library.entry_book(book_obj4)


# Q-7
# Creating Manu System
option = None
while option != 4:
    print("")
    print("------ Welcome to the Library ------")
    print("1.View All Book")
    print("2.Borrow Book")
    print("3.Return Book")
    print("4.Exit")
    option = int (input("Enter Your Choise: "))
    
    if option == 1:
        book_obj.view_book_info()
    elif option == 2:
        Book.borrow_book()
    elif option == 3:
        Book.return_book()