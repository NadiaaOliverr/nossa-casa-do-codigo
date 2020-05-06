from dao import BookDatabase


class ShoppingCart:

    def __init__(self, book_database: BookDatabase) -> None:
        self.__dict_of_book_on_cart = {}
        self.__book_database = book_database
        self.__quantity = 1

    def add_cart(self, title: str) -> None:
        book = self.__book_database.find_by_title(title)

        if title in self.__dict_of_book_on_cart:
            self.__dict_of_book_on_cart[book.title]['quantity_cart'] += self.__quantity
        else:
            self.__dict_of_book_on_cart[book.title] = {
                'resume': book.resume,
                'summary': book.summary,
                'price': book.price,
                'number_pages': book.number_pages,
                'isbn': book.isbn,
                'publication_date': book.publication_date,
                'category': book.category,
                'quantity_cart': self.__quantity
            }

    def list_items_cart(self) -> None:
        total_prices = 0.0
        for title_book, informations_book in self.__dict_of_book_on_cart.items():
            total_prices += informations_book['price'] * informations_book['quantity_cart']
            print(f'Título: {title_book}')
            print(f'Preço: R${informations_book["price"]}\nQuantidade: {informations_book["quantity_cart"]}\n')

        print('Total do Carrinho: R$ {:.2f}'.format(total_prices))
