from validate_email import validate_email
from datetime import datetime


class Author:

    def __init__(self, name, email, description):
        if not self._name_is_empty(name):
            self._name = name
        if self._email_is_valid(email):
            self._email = email
        if not self._description_is_empty(description) and not self._description_is_full(description):
            self._description = description
        self._time_registration = datetime.now().strftime("%d/%m/%Y às %H:%M:%S.%f - BRT")

    def _name_is_empty(self, name):
        name_is_empty = len(name) == 0
        if name_is_empty:
            raise Exception('A descrição possui mais do que 400 caracteres')
        return False

    def _email_is_valid(self, email):
        email_is_valid = validate_email(email)
        if not email_is_valid:
            raise Exception('O email digitado não é válido')
        return True

    def _description_is_empty(self, description):
        description_is_empty = len(description) == 0
        if description_is_empty:
            raise Exception('A descrição possui mais do que 400 caracteres')
        return False

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
