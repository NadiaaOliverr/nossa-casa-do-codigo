from src.authors.authors import Author

if __name__ == '__main__':
    try:
        author_1 = Author('Eistein', 'einstein@pandora.be', 'Autor do livro Como Vejo o Mundo')
        author_2 = Author('Roger S. Pressman', 'presman@engenharia.com', 'Autor do Livro de Engenharia de Software')
        author_3 = Author('Luciano Ramalho', 'elucianor@gmail.com', 'Autor do livro Fluent Python')
        authors = [author_1, author_2, author_3]
    except:
        raise TypeError('Preencha todos os campos')

    for author in authors:
        print(f'Name: {author.name}\nEmail: {author.email}\nDescription: {author.description}\nRegistered at: {author.time_registration}\n')