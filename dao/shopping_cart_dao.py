from dao import BookDatabase


class ShoppingCart:
    def __init__(self, book_database: BookDatabase) -> None:
        self.__books_on_cart = {}
        self.__book_database = book_database
        self.__quantity_initial = 1

    def add_cart(self, title_book: str) -> None:
        book = self.__book_database.find_by_title(title_book)
        if book in self.__books_on_cart:
            quantity = self.__books_on_cart[book]
            self.__books_on_cart[book] = quantity + 1
        else:
            self.__books_on_cart[book] = self.__quantity_initial

    def list_items_cart(self) -> None:
        total_prices = 0.0
        print('Seu carrinho'.upper())
        for item, quantity in self.__books_on_cart.items():
            total_prices += item.price * quantity
            total_item = item.price * quantity
            print(
                f'Item: {item.title} - Preço: R${item.price} - '
                f'Quantidade: {quantity} - Total: {total_item:.2f}'
            )

        print('Total do Carrinho: R$ {:.2f}'.format(total_prices))
