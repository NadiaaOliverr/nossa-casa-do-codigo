from typing import List
from model.category import Category


class CategoryDatabase:

    def __init__(self) -> None:
        self.__list: List[Category] = []

    def add(self, category: Category) -> None:
        if category in self.__list:
            raise Exception('Já existe uma categoria com este nome')
        self.__list.append(category)

    @property
    def list(self) -> List[Category]:
        return self.__list.copy()
