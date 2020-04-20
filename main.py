from dao import CategoryDatabase, BookDatabase
from model import Book, Category

if __name__ == '__main__':
    # Banco de Dados
    books = BookDatabase()
    categories = CategoryDatabase()

    # Categorias
    category_1 = Category('Programação')
    category_2 = Category('Arquitetura de Software')
    category_3 = Category('Aventura')

    # Livros
    book_1 = Book('Test-Driven Development',
                  'Por que não testamos software?Porque é caro? '
                  'Porque é demorado? Porque é chato? '
                  'Testes automatizados são a solução para '
                  'todos esses problemas. Aprenda a escrever '
                  'um programa que teste seu programa de forma '
                  'rápida, barata e produtiva, '
                  'e aumente a qualidade do seu produto final.',
                  '# Introdução ## 1.1 Era uma vez um projeto sem testes... '
                  '## 1.2 Por que devemos testar?'
                  '## 1.3 Por que não testamos?', 29.90, 194, '9788566250046',
                  (2020, 6, 20), category_1)

    books.add(book_1)
    categories.add(category_1)

    book_2 = Book('Clean Code',
                  'Por que não testamos software? Porque é caro? '
                  'Porque é demorado? Porque é chato? ',
                  '# Introdução ## 1.1 Era uma vez um projeto sem testes... '
                  '## 1.2 Por que devemos testar?'
                  '## 1.3 Por que não testamos?', 29.90, 194, '9788566250048',
                  (2020, 6, 20), category_1)

    books.add(book_2)
    categories.add(category_2)

    print(books.find_by_title('Clean Code'))

    # Imprimindo os livros
    # for book in books:
    #     print(book)
