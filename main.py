from model.author import Author
from model.category import Category
from dao.author_dao import AuthorDatabase
from dao.category_dao import CategoryDatabase

if __name__ == '__main__':

    # Livros
    authors = AuthorDatabase()

    author_1 = Author(
        'Eistein', 'eistein@gmail.com',
        'Autor do livro Como Vejo o Mundo'
    )
    authors.add(author_1)

    author_2 = Author(
        'Roger S. Pressman', 'presman@engenharia.com',
        'Autor do Livro de Engenharia de Software'
    )
    authors.add(author_2)

    author_3 = Author(
        'Luciano Ramalho', 'elucianor@gmail.com',
        'Autor do livro Fluent Python'
    )
    authors.add(author_3)

    for author in authors.list:
        print(author)

    # Categorias
    categories = CategoryDatabase()

    category_1 = Category('Romance')
    categories.add(category_1)

    category_2 = Category('Ficção Científica')
    categories.add(category_2)

    category_3 = Category('Aventura')
    categories.add(category_3)

    for category in categories.list:
        print(category)
