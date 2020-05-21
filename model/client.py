from validate_email import validate_email
from validate_docbr import CPF

from model import Address

class Client:

    def __init__(self, name: str, email: str, cpf: str, address: 'Address') -> None:
        self.__set_name(name)
        self.__set_email(email)
        self.__set_cpf(cpf)
        self.__adress = address

    def __set_name(self, name: str) -> None:
        name_is_empty = len(name) == 0 or len(name.split()) == 0
        if name_is_empty:
            raise Exception('Nome não pode ser vazio')
        self.__name = name

    def __set_email(self, email: str) -> None:
        email_is_valid = validate_email(email)
        if not email_is_valid:
            raise Exception('O email digitado não é válido')
        self.__email = email

    def __set_cpf(self, cpf: str) -> None:
        cpf_is_valid = CPF()
        cpf_is_valid = cpf_is_valid.validate(cpf)
        if not cpf_is_valid:
            raise Exception('O CPF digitado não é válido')
        self.__cpf = cpf

user = User('Nádia', 'nadia@nadia.com.br', '012.345.678-90', Address('Itabira', 'MG', '38900456'))