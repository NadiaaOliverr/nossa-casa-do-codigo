from src.authors.authors import Author
from prettytable import PrettyTable


def cria_authors():
    author_1 = Author('Albert Einstein', 'einstein@pandora.be', 'Autor do livro Como Vejo o Mundo')
    author_2 = Author('Roger S. Pressman', 'presman@engenharia.com', 'Autor do Livro de Engenharia de Software')
    author_3 = Author('Luciano Ramalho', 'lucianor@hotmail.com', 'Autor do livro Fluent Python')
    return author_1, author_2, author_3


def registration_author():
    author_1, author_2, author_3 = cria_authors()
    authors = {}

    author = [author_1.name, author_1.email, author_1.description, author_1.time_registration]
    authors[author_1.name] = author

    author = [author_2.name, author_2.email, author_2.description, author_2.time_registration]
    authors[author_2.name] = author

    author = [author_3.name, author_3.email, author_3.description, author_3.time_registration]
    authors[author_3.name] = author

    return authors


def print_all_authors(authors):
    table_authors = PrettyTable()
    table_authors.field_names = ["Name", "E-mail", "Description", "Time Registration"]

    for name, values in authors.items():
        email = values[0]
        description = values[1]
        time_registration = values[2]
        table_authors.add_row([name, email, description, time_registration])

    print('\n--- Authors registrated ---\n\n')
    print(table_authors)
    print()


if __name__ == '__main__':
    authors = registration_author()
    print_all_authors(authors)
