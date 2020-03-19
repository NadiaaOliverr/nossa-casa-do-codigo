from model.author import Author
from dao.author_dao import AuthorDatabase

if __name__ == '__main__':
    authors = AuthorDatabase()

    author_1 = Author('Eistein', 'eistein@gmail.com', 'Autor do livro Como Vejo o Mundo')
    authors.add(author_1)

    author_2 = Author('Roger S. Pressman', 'presman@engenharia.com', 'Autor do Livro de Engenharia de Software')
    authors.add(author_2)

    author_3 = Author('Luciano Ramalho', 'elucianor@gmail.com', 'Autor do livro Fluent Python')
    authors.add(author_3)

    for author in authors.list:
        print(author)
