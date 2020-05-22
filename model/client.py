from validate_email import validate_email
from validate_docbr import CPF

from model import Address


class Client:

    __attributes = ('_name', '_email', '_cpf', '_address')

    def __init__(self, name: str, email: str,
                 cpf: str, address: 'Address') -> None:
        self.__set_name(name)
        self.__set_email(email)
        self.__set_cpf(cpf)
        self._address = address

    def __setattr__(self, key, value):
        if key not in self.__attributes:
            raise AttributeError(f'Não foi possível adicionar o atributo {key}')
        object.__setattr__(self, key, value)
    
    def __str__(self):
        return (
            f'Nome: {self._name}\n'
            f'Email: {self._email}\n'
            f'CPF: {self._cpf}\n'
            f'Endereço: {self._address.city} - {self._address.state} - {self._address.cep}'
        ) 

    def __set_name(self, name: str) -> None:
        name_is_empty = len(name) == 0 or len(name.split()) == 0
        if name_is_empty:
            raise Exception('Nome não pode ser vazio')
        self._name = name

    def __set_email(self, email: str) -> None:
        email_is_valid = validate_email(email)
        if not email_is_valid:
            raise Exception('O email digitado não é válido')
        self._email = email

    def __set_cpf(self, cpf: str) -> None:
        cpf_is_valid = CPF()
        cpf_is_valid = cpf_is_valid.validate(cpf)
        if not cpf_is_valid:
            raise Exception('O CPF digitado não é válido')
        self._cpf = cpf
