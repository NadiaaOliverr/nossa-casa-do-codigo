from model import Book

from typing import List


class BookDatabase:

    def __init__(self) -> None:
        self.__list = []

    '''
        O método __iter__ é para que possa iterar diretamente sobre o objeto criado.
        Evitando assim acessar por exemplo: for book in books.list
        Faça então: for book in books
    '''

    def __iter__(self):
        return self.list.__iter__()

    def add(self, book: Book) -> None:
        if book in self.__list:
            raise Exception('Título ou ISBN duplicado. Isto não é permitido')
        self.__list.append(book)

    def find_by_title(self, title: str) -> Book:
        for book in self.__list:
            if title == book.title:
                return book
        raise Exception('Título procurado não encontrado')

    @property
    def list(self) -> List[Book]:
        return self.__list.copy()
