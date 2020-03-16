from src.model.authors import Author

if __name__ == '__main__':
    authors = []

    author_1 = Author('Eistein', 'elucianor@gmail.com', 'Autor do livro Como Vejo o Mundo')
    authors.append(author_1)

    author_2 = Author('Roger S. Pressman', 'presman@engenharia.com', 'Autor do Livro de Engenharia de Software')
    if author_2 in authors:
        raise Exception('Autor duplicado')
    authors.append(author_2)

    author_3 = Author('Luciano Ramalho', 'elucianor@gmail.com', 'Autor do livro Fluent Python')
    if author_3 in authors:
        raise Exception('Autor duplicado')
    authors.append(author_3)

    for author in authors:
        print(author)
