import saveAllBooks

def bookDelete(bookList):
    serchBook = input("Enter Book title to delete: ")
    for book in bookList:
        if book['title'] == serchBook:
            bookList.remove(book)
            saveAllBooks.saveBooks(bookList)
            print("Book Delete Sucessfully")
            print("-----------------------------")
            
            return bookList 
    else:
        print("Book Not Found!")
    print("------------------------------")
        
            