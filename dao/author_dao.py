from typing import List
from model import Author


class AuthorDatabase:

    def __init__(self) -> None:
        self.__list: List[Author] = []

    def add(self, author: Author) -> None:
        if author in self.__list:
            raise Exception('Já existe um e-mail como este')
        self.__list.append(author)

    @property
    def list(self) -> List[Author]:
        return self.__list.copy()
