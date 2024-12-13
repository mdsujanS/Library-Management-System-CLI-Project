
# def viewBooks(bookList):
#     if bookList != []:
#          for book in bookList:
#              print(f" Title: {book['title']} | Author: {book['author']} | Year: {book['year']} | Price: {book['price']} | ISBN :{book['isbn']} | Book Added: {book['bookAddDate']}")
#     else:
#         print("*** Book Not Found! ***")
    
#     print("--------------------------------------")
        
import json 
def viewBooks(bookList):
    with open('AllBooks.json', 'r') as book:
        bookList = json.load(book)
        if bookList != []:
            for book in bookList:
                print(f" Title: {book['title']} | Author: {book['author']} | Year: {book['year']} | Price: {book['price']} | Quantity:{book['quantity']} | ISBN :{book['isbn']} | Book Edite: {book['updateBook']}")
        else:
            print("*** Book Not Found! ***")
    
        print("--------------------------------------")
        