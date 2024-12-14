
import saveUser
import saveAllBooksfrom 
from datetime import datetime


def borrowing(booksList, userDetails):
    search = input("Enter Book title: ")
    for book in booksList:
        if book['title'] == search:
            userName = input("Enter Your name: ")
            phoneNumber = input("Enter Your Phone Number: ")
            inputDate =input('Enter a date (DD-MM-YYYY): ')
            
            dateFormat ="%d-%m-%y"
            try:
                returnDate = datetime.strptime(inputDate, dateFormat).date()
            except:
                print("Invalid date format. use (DD-MM-YYYY)")
                
            
            user ={
                'title' : search,
                'userName': userName,
                'phoneNumber': phoneNumber,
                'returnDate': returnDate,
                
            }
            
            userDetails.append(user)
            saveUser.userDetails(userDetails)
            
            book['quantity'] = book['quantity'] - 1 
            saveAllBooksfrom.saveBooks(booksList)
            
    else:
        print("No enought books are available to lend")
            
    return userDetails             
            
            