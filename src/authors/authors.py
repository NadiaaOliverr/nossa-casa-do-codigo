from validate_email import validate_email
from datetime import datetime


class Author:

    def __init__(self, name='', email='', description=''):
        self._set_author(name, email, description)

    def _set_author(self, name, email, description):
        if self._fields_validation(name, email, description):
            self._name = name
            self._email = email
            self._description = description
        self._time_registration = datetime.now().strftime("%d/%m/%Y às %H:%M:%S.%f - BRT")

    def _fields_validation(self, name, email, description):
        self._fields_empty(name, email, description)
        self._description_is_full(description)
        self._email_field_validation(email)
        return True

    def _fields_empty(self, name, email, description):
        name_is_empty = len(name) == 0
        email_is_empty = len(email) == 0
        description_is_empty = len(description) == 0
        if name_is_empty or email_is_empty or description_is_empty:
            raise TypeError('Há campos vazios. Preencha todos os campos.')
        return False

    def _email_field_validation(self, email):
        email_is_valid = validate_email(email)
        if not email_is_valid:
            raise Exception('O email digitado não é válido')
        return True

    def _description_is_full(self, description):
        if len(description) > 400:
            raise Exception('A descrição possui mais do que 400 caracteres')
        return False

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def description(self):
        return self._description

    @property
    def time_registration(self):
        return self._time_registration
