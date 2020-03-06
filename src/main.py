from datetime import datetime

def registration_author():
    author = []
    print('\n--- Registration new author ---')
    name = input('Name: ')
    email = input('E-mail: ')
    description = input('Description: ')
    time_registration = datetime.now().strftime("%d/%m/%Y às %H:%M:%S de BRT")
    author.append(email)
    author.append(description)
    author.append(time_registration)
    return name, author

if __name__ == '__main__':

    authors = {}
    quantity = int(input('Number of authors: '))
    for i in range(quantity):
        name, authors[name] = registration_author()

    print(authors)
