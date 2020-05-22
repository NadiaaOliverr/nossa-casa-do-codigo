from dao import CategoryDatabase, BookDatabase, ShoppingCart, CouponDatabase
from model import Book, Category, Client, Address

if __name__ == '__main__':
    # Banco de Dados
    books = BookDatabase()
    categories = CategoryDatabase()
    coupons = CouponDatabase()

    # Categorias
    category_1 = Category('Programação')
    category_2 = Category('Arquitetura de Software')

    # Livros
    book_1 = Book('Test-Driven Development',
                  'Por que não testamos software?Porque é caro? ',
                  '# Introdução ## 1.1 Era uma vez um projeto sem testes... '
                  '## 1.3 Por que não testamos?', 29.90, 194, '9788566250046',
                  (2020, 6, 20), category_1)

    books.add(book_1)
    categories.add(category_1)

    book_2 = Book('Clean Code',
                  'Por que não testamos software? Porque é caro? '
                  'Porque é demorado? Porque é chato? ',
                  '## 1.2 Por que devemos testar?'
                  '## 1.3 Por que não testamos?', 59.90, 194, '9788566250048',
                  (2020, 6, 20), category_1)

    books.add(book_2)
    categories.add(category_2)

    coupon_1 = coupons.add_coupon('ALURA10', (2020, 10, 10), 10)
    coupon_2 = coupons.add_coupon('CDC40', (2020, 6, 10), 40)

    # Carrinho de Compras
    cart = ShoppingCart(books, coupons)
    client_1 = Client('Nádia', 'nadia@nadia.com.br',
                      '012.345.678-90', Address('São Gonçalo', 'MG', '38900456'))

    cart.add_cart('Clean Code')
    cart.add_cart('Test-Driven Development')
    cart.add_cart('Test-Driven Development')
    cart.checkout(client_1, 'ALURA10')
