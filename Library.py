# Q-1
class Library:
    
    book_list = [] # Create book_list for entry book object 
    
    @classmethod # use classmethod for direct call entry_book using library class,not class object 
    def entry_book (self,obj): # this function using for insert book object in the book_list
        self.book_list.append(obj)