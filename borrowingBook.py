import datetime 
import saveUser
import saveAllBooks



def borrowing(booksList, userDetails):
    search = input("Enter Book title: ")
    for book in booksList:
        if book['title'] == search:
            userName = input("Enter Your name: ")
            phoneNumber = input("Enter Your Phone Number: ")
            returnDate = int(input("Entr return Date: "))
            
            currentTime = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
            
            user ={
                'title' : search,
                'userName': userName,
                'phoneNumber': phoneNumber,
                'returnDate': returnDate,
                
            }
            userDetails.append(user)
            saveUser.userDetails(userDetails)
            
            book['quantity'] = book['quantity'] - 1 
            saveAllBooks.saveBooks(booksList)
            
    else:
        print("No enought books are available to lend")
            
    return userDetails             
            
            