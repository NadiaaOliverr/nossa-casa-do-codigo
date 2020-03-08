from src.authors.excecoes import NameRequired, DescriptionRequired, DescriptionFull, EmailValid, TimeRegistrationNull

from validate_email import validate_email
from prettytable import PrettyTable
import os

class Author:

    _authors = {}

    def __init__(self):
        pass

    def set_author(self, name, email, description, time_registration):
        if (self._name_field_validation(name)):
            self._name = name
        if (self._email_field_validation(email)):
            self._email = email
        if (self._description_field_validation(description)):
            self._description = description
        if(self._time_registration_validation(time_registration)):
            self._time_registration = time_registration

        self._registration_author(self._name, self._email, self._description, self._time_registration)

    def _time_registration_validation(self, time_registration):
        time_registration_is_null = time_registration == None
        if(time_registration_is_null):
            raise TimeRegistrationNull('O instante de cadastro não pode ser nulo')
        else:
            return True

    def _name_field_validation(self, name):
        name_is_empty = len(name) == 0
        if(name_is_empty):
            raise NameRequired('O campo nome é obrigatório')
        else:
            return True

    def _description_field_validation(self, description):
        description_is_empty = len(description) == 0
        description_is_full = len(description) > 400
        if(description_is_empty):
            raise DescriptionRequired('O campo descrição é obrigatório')
        if (description_is_full):
            raise DescriptionFull('O campo descrição ultrapassa 400 caracteres')
        else:
            return True

    def _email_field_validation(self, email):
        email_is_valid = validate_email(email)
        if(not email_is_valid):
            raise EmailValid('O email digitado não é válido')
        else:
            return True

    def _registration_author(self, name, email, description, time_registration):
        author = []
        author.append(email)
        author.append(description)
        author.append(time_registration)
        self._authors[name] = author

    def _clear_display(self):
        os.system('clear')

    def print_table_all_authors(self):
        table_authors = PrettyTable()
        table_authors.field_names = ["Name", "E-mail", "Description", "Time Registration"]

        for name, values in self._authors.items():
            name = name
            email = values[0]
            description = values[1]
            time_registration = values[2]
            table_authors.add_row([name, email, description, time_registration])

        self._clear_display()
        print('\n--- Authors registrated ---\n\n')
        print(table_authors)
        print()
