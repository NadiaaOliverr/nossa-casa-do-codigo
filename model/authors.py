from validate_email import validate_email
from datetime import datetime


class Author:

    def __init__(self, name, email, description):
        self.__set_name(name)
        self.__set_email(email)
        self.__set_description(description)
        self.__time_recorded = datetime.now()

    def __str__(self):
        return f'Nome: {self.name}\nEmail: {self.email}\nDescrição: {self.description}\nRegistrado às: {self.time_registration}\n'

    def __eq__(self, other_author):
        return self.email == other_author.email

    def __ne__(self, other_author):
        return not self.__eq__(other_author)

    def __set_name(self, name):
        name_is_empty = len(name) == 0
        if name_is_empty:
            raise Exception('Nome não pode ser vazio')
        self.__name = name

    def __set_email(self, email):
        email_is_valid = validate_email(email)
        if not email_is_valid:
            raise Exception('O email digitado não é válido')
        self.__email = email

    def __set_description(self, description):
        description_is_empty = len(description) == 0
        description_is_full = len(description) > 400
        if description_is_empty:
            raise Exception('Descrição não pode ser vazia')
        if description_is_full:
            raise Exception('Descrição não pode conter mais que 400 caracteres')
        self.__description = description

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @property
    def description(self):
        return self.__description

    @property
    def time_registration(self):
        return self.__time_recorded


class AuthorDatabase:

    def __init__(self):
        self.__list_authors = []

    def add_author(self, author):
        if author in self.__list_authors:
            raise Exception('Já existe um e-mail como este')
        self.__list_authors.append(author)

    @property
    def list_authors(self):
        return self.__list_authors
