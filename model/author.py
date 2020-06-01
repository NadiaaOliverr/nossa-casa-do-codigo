from validate_email import validate_email
from datetime import datetime


class Author:
    __attributes = ('_name', '_email', '_description', '_time_recorded')

    def __init__(self, name: str, email: str, description: str) -> None:
        self.__set_name(name)
        self.__set_email(email)
        self.__set_description(description)
        self._time_recorded: datetime = datetime.now()

    '''
         __setattr__ é para evitar a criação de atributos fora da classe.

        Exemplo:
        author = Author('nadia','nadia.silva@gmail.com','estudante')
        author.faculdade = 'ufv'
        print(author.faculdade)

        Resultado do Console: Não foi possível adicionar o atributo faculdade
    '''

    def __setattr__(self, key, value):
        if key not in self.__attributes:
            raise AttributeError(f'Não foi possível adicionar o atributo {key}')
        object.__setattr__(self, key, value)

    def __str__(self) -> str:
        return (
            f'Nome: {self.name}\nEmail: {self.email}\nDescrição: '
            f'{self.description}\nRegistrado às: '
            f'{self.time_registration}\n'
        )

    def __eq__(self, other_author: 'Author') -> bool:
        return self.email == other_author.email

    def __ne__(self, other_author: 'Author') -> bool:
        return not self.__eq__(other_author)

    def __set_name(self, name: str) -> None:
        name_is_empty = len(name) == 0
        if name_is_empty:
            raise Exception('Nome não pode ser vazio')
        self._name = name

    def __set_email(self, email: str) -> None:
        email_is_valid = validate_email(email)
        if not email_is_valid:
            raise Exception('O email digitado não é válido')
        self._email = email

    def __set_description(self, description: str) -> None:
        description_is_empty = len(description) == 0
        description_is_full = len(description) > 400
        if description_is_empty:
            raise Exception('Descrição não pode ser vazia')
        if description_is_full:
            raise Exception(
                'Descrição não pode conter mais que 400 caracteres'
            )
        self._description = description

    @property
    def name(self) -> str:
        return self._name

    @property
    def email(self) -> str:
        return self._email

    @property
    def description(self) -> str:
        return self._description

    @property
    def time_registration(self) -> datetime:
        return self._time_recorded
