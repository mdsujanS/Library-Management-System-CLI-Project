import json 
def userDetails(allUser):
    with open('landBook.json', 'w') as land:
        json.dump(allUser, land, indent= 4)
    