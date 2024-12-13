import random 
import datetime 
import saveAllBooks 



def add_books(booksList):
    title = input('Enter Book title: ')
    author = input('Enter Author name: ')
    
    while True:
        try:
            year = int(input('Enter Publishing Year: '))
            break
        except ValueError:
            print("Ente  Valied Year!")
    
    while True:
        try:
            price = int(input('Enter Book Price: '))
            break
        except ValueError:
            print("Enter Valid Price!")
            
    while True:
        try:
            quantity = int(input('Enter Quantity of Books: '))
            break
        except ValueError:
            print('Enter Valid Quantity!')
    
    isbn = random.randint(100000, 999999)
    bookAddDate = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
    
    book = {
        'title': title,
        'author': author,
        'year': year,
        'price': price,
        'quantity': quantity,
        'isbn': isbn,
        'bookAddDate': bookAddDate,
        'updateBook' : bookAddDate,
         
    }
    
    booksList.append(book)
    saveAllBooks.saveBooks(booksList)
    
    print('Book Added Successfully')
    print("-------------------------------")
    
    return booksList 
    
    