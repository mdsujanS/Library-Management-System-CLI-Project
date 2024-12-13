import json
def restore():
    with open('landBook.json', 'r') as file:
        user = json.load(file)
    return user
    # pass
