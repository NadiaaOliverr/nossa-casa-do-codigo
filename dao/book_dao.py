from model import Book

from typing import List


class BookDatabase:

    def __init__(self) -> None:
        self.__list = []

    def add(self, book: Book) -> None:
        if book in self.__list:
            raise Exception('Título ou ISBN duplicado. Isto não é permitido')
        self.__list.append(book)

    def find_by_title(self, title: str) -> Book:
        if self.__validate_title_wanted_book(title):
            for book in self.__list:
                if title == book.title:
                    return book.to_view()
            raise Exception('Título procurado não encontrado')
        raise Exception('Título em formato inválido')

    def __validate_title_wanted_book(self, title: str) -> bool:
        if not title:
            return False
        return True

    @property
    def list(self) -> List[Book]:
        return self.__list.copy()
