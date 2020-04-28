from dao import BookDatabase
from typing import List, Dict


class ShoppingCart:

    def __init__(self, book_database: BookDatabase) -> None:
        self.__dict: Dict[str, List[float, int]] = {}
        self.__book_database = book_database
        self.__total_prices = []
        self.__quantity_initial = 1

    def add_cart(self, title: str) -> None:
        book = self.__book_database.find_by_title(title)
        if title in self.__dict:
            self.__dict[title][1] += 1  # Adicione mais uma quantidade a um item existente
        else:
            self.__dict[title] = [book.price, self.__quantity_initial]

        price = self.__dict[title][0]
        self.__total_prices.append(price)

    def list_items_cart(self) -> None:
        for title_book, informations_book in self.__dict.items():
            price, quantity = informations_book
            print(f'Título: {title_book}')
            print('Preço: R${}\nQuantidade: {}\n'.format(price, quantity))

        print('Total do Carrinho: R$ {:.2f}'.format(sum(self.__total_prices)))
