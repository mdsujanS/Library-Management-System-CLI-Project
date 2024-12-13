import json 

def saveBooks(bookList):
    with open('AllBooks.json', 'w') as book:
        json.dump(bookList, book, indent=4)
        