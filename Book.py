from Library import Library

class Book:
    def __init__(self,book_id, title, author, available):
        self.__book_id = book_id
        self._title = title
        self.__author = author
        self._available = available
        
    # Booking a book of the library 
    @classmethod
    def borrow_book(self):
        ID = int(input("Enter book id to borrow: "))
        for i in Library.book_list:
            if i.__book_id == ID: 
                if i._available is True:
                    i._available = False
                    print(f'Successfully Borrow {i._title}')
                    return
                else:
                    print("Allready Borrowed This Book")
                    return
        print("Can't not match book ID")

                
    # Back to book of the library 
    @classmethod
    def return_book(self):
        ID = int(input("Enter book id to Return: "))
        for i in Library.book_list:
            if i.__book_id == ID:
                if i._available is False:
                    i._available = True                    
                    print(f'Successfully Return {i._title}')
                    return
                else:
                    print("Allready Return This Book")
                    return
        print("Can't match book ID")
           
        
    # View library strock book 
    def view_book_info (self):
        print("")
        print("Library Book")
        for i in Library.book_list:
            print(f'ID: {i.__book_id},   Title: {i._title}, Author: {i.__author}, Status: {i._available}')
