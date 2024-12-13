import json
import saveUser
import saveAllBooks


def bookReturn(allBooks):
    User = []
    with open('landBook.json', 'r') as land:
        User = json.load(land)
    
    title = input('Enter title: ')
    
    for i in User:
        if i['title'] == title:
            for book in allBooks:
                if book['title'] == title:
                    book['quantity'] += 1
                    saveAllBooks.saveBooks(allBooks)
                    break
            
            User.remove(i)
            saveUser.userDetails(User)
            
            return User
    else:
        print("Book title Not Found!")
            