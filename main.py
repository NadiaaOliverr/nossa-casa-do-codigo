from dao.book_dao import BookDatabase
from model.book import Book

if __name__ == '__main__':

    books = BookDatabase()
    book_1 = Book('Test-Driven Development',
                  'Por que não testamos software? Porque é caro? Porque é demorado? Porque é chato? '
                  'Testes automatizados são a solução para todos esses problemas. Aprenda a escrever '
                  'um programa que teste seu programa de forma rápida, barata e produtiva, '
                  'e aumente a qualidade do seu produto final.',
                  '# Introdução ## 1.1 Era uma vez um projeto sem testes... '
                  '## 1.2 Por que devemos testar?'
                  '## 1.3 Por que não testamos?', 29.90, 194, '9788566250046',
                  (2020, 4, 20), 'Programação')
    books.add(book_1)

    for book in books.list:
        print(book)