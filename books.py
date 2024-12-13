
import viewAllBooks
import addBooks
import restoreBooks 
import updateBooks 
import deleteBooks 
import borrowingBook
import returnBook
import restoreUser

allBooks = []
userDetails =[]

while True:
 
    print('--------- Welcome to Library management System -----------')
    print("0. Exit")
    print("1. Add Books")
    print("2. View All Books")
    print("3. Update Books")
    print("4. Books Remove/Delete")
    print("5. Borrowing a Book: ")
    print('6. Return a Book: ')
    
    
    allBooks = restoreBooks.RestoreBooks()
    userDetails = restoreUser.restore()
    
    menu = input("Select an Option: ")
    
    if menu == '0':
        print("------ Thanks for using Library Management System --------")
        break
    elif menu == '1':
        all_books = addBooks.add_books(allBooks)
        
    elif menu == '2':
        viewAllBooks.viewBooks(allBooks)
        
    elif menu == '3':
        updateBooks.booksUpdate(allBooks)
        
    elif menu == '4':
        deleteBooks.bookDelete(allBooks)
    
    elif menu == '5':
        borrowingBook.borrowing(allBooks, userDetails) 
    elif menu == '6':
        returnBook.bookReturn(allBooks)
        
    else:
        print('Chose a Valid Operation')
        