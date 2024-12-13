import json 

def RestoreBooks():
    with open('allBooks.json', 'r') as fp:
        books = json.load(fp)
    return books
    # pass 