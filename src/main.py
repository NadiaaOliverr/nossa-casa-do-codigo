from datetime import datetime
from validate_email import validate_email
from prettytable import PrettyTable
import os

def name_field_validation(name):
    name_is_empty = len(name) == 0
    return not name_is_empty

def description_field_validation(description):
    description_is_empty = len(description) == 0
    description_is_full = len(description) > 400
    if(description_is_empty or description_is_full):
        return False
    else:
        return True

def email_field_validation(email):
    email_is_valid = validate_email(email) 
    return email_is_valid

def insert_name():
    name = input('Name: ')
    while (not name_field_validation(name)):
        print('O campo nome é obrigatório.')
        name = input('Name: ')
    return name

def insert_email():
    email = input('E-mail: ')
    while (not email_field_validation(email)):
        print('Digite um e-mail válido.')
        email = input('E-mail: ')
    return email

def insert_description():
    description = input('Description: ')
    while (not description_field_validation(description)):
        print('O campo descrição é obrigatório e não pode ultrapassar 400 caracteres')
        description = input('Description: ')
    return description

def inputs():
    print('\n--- Registration new author ---')
    name = insert_name()
    email = insert_email()
    description = insert_description()
    time_registration = datetime.now().strftime("%d/%m/%Y às %H:%M:%S de BRT")
    return name, email, description, time_registration

def registration_author():
    author = []
    name, email, description, time_registration = inputs()
    author.append(email)
    author.append(description)
    author.append(time_registration)
    return name, author

def clear_display():
    os.system('clear')

def print_table_authors(authors):
    table_authors = PrettyTable()
    table_authors.field_names = ["Name", "E-mail", "Description", "Time Registration"]

    for name, values in authors.items():
        name = name
        email = values[0]
        description = values[1]
        time_registration = values[2]
        table_authors.add_row([name, email, description, time_registration])

    clear_display()
    print('\n--- Authors registrated ---\n\n')
    print(table_authors)
    print()

if __name__ == '__main__':

    authors = {}
    quantity = int(input('Number of authors: '))
    for i in range(quantity):
        name, authors[name] = registration_author()

    print_table_authors(authors)