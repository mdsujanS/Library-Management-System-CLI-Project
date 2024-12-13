import saveAllBooks
import datetime 

def booksUpdate(bookList):
    searchBook = input("Enter Book Title to update: ")
    for book in bookList:
        if book['title'] == searchBook:
            
            book['title'] = input("Enter Book title: ")
            book['author'] = input("Entr Author name: ")
            book['year'] = int(input("Entr Publishing Year: "))
            book['price'] = int(input("Entr book price: "))
            book['quantity'] = int(input("Entr book Quantity: "))
            book['updateBook'] = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
            
            saveAllBooks.saveBooks(bookList)
            
            print("Books Update SuccessFully")
            print("----------------------------------")
            
            return bookList
        
    else:
        print("*** Book  Not Found ***")
        
            