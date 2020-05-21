class ShoppingCart:
    def __init__(self, book_database: 'BookDatabase',
                 coupon_database: 'CouponDatabase') -> None:
        self.__books_on_cart = {}
        self.__book_database = book_database
        self.__quantity_initial = 1
        self.__coupon_database = coupon_database

    def add_cart(self, title_book: str) -> None:
        book = self.__book_database.find_by_title(title_book)
        if book in self.__books_on_cart:
            quantity = self.__books_on_cart[book]
            self.__books_on_cart[book] = quantity + 1
        else:
            self.__books_on_cart[book] = self.__quantity_initial

    def __list_items_cart(self, discount=None) -> None:
        self.__total_prices = 0.0
        print('Seu carrinho'.upper())
        for item, quantity in self.__books_on_cart.items():
            self.__total_prices += item.price * quantity
            total_item = item.price * quantity
            print(
                f'Item: {item.title} - Preço: R${item.price} - '
                f'Quantidade: {quantity} - Total: {total_item:.2f}'
            )
        if discount is None:
            print(f'Total do Carrinho: R$ {self.__total_prices:.2f}')
        else:
            value_discount = (self.__total_prices * discount) / 100
            self.__total_prices = self.__total_prices - value_discount
            print(f'Desconto de R$ {value_discount} aplicado a sua compra')
            print(f'Total do Carrinho: R$ {self.__total_prices:.2f}')

    def checkout(self, client: 'Client', coupon=None) -> None:
        if coupon not is None:
            percent_discount = self.__coupon_database
            .get_percent_if_coupon_is_valid(coupon)
            self.__list_items_cart(percent_discount)
        else:
            self.__list_items_cart()
        self.__books_on_cart = {}
