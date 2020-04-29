from dao import BookDatabase
from typing import Dict, Union

"""
    Estrutura do dicionário de listagem:
    {
        título_do_livro: {
                preco_do_livro: x
                quantidade_de_livro: y
            }
    }
    Ex: {'Clean Code': {'price': 59.9, 'quantity': 1}}
"""


class ShoppingCart:

    def __init__(self, book_database: BookDatabase) -> None:
        self.__dict: Dict[str, Dict[str, Union[float, int]]] = {}
        self.__book_database = book_database
        self.__quantity = 1

    def add_cart(self, title: str) -> None:
        book = self.__book_database.find_by_title(title)

        if title in self.__dict:
            self.__dict[book.title]['quantity'] += self.__quantity
        else:
            self.__dict[book.title] = {
                'price': book.price,
                'quantity': self.__quantity
            }

    def list_items_cart(self) -> None:
        total_prices = 0.0
        for title_book, informations_book in self.__dict.items():
            total_prices += informations_book['price'] * informations_book['quantity']
            print(f'Título: {title_book}')
            print(f'Preço: R${informations_book["price"]}\nQuantidade: {informations_book["quantity"]}\n')

        print('Total do Carrinho: R$ {:.2f}'.format(total_prices))
