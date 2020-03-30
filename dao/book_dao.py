from model.book import Book

from typing import List


class BookDatabase:

    def __init__(self) -> None:
        self.__list = []

    def add(self, book: Book) -> None:
        if book in self.__list:
            raise Exception('Título ou ISBN duplicado. Isto não é permitido')
        self.__list.append(book)

    @property
    def list(self) -> List[Book]:
        return self.__list.copy()
