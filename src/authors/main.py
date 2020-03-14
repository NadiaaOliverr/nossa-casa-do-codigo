from src.authors.authors import Author
from prettytable import PrettyTable

if __name__ == '__main__':
    try:
        author_1 = Author('Eistein', 'einstein@pandora.be', 'Autor do livro Como Vejo o Mundo')
        author_2 = Author('Roger S. Pressman', 'presman@engenharia.com', 'Autor do Livro de Engenharia de Software')
        author_3 = Author('Luciano Ramalho', 'elucianor@gmail.com', 'Autor do livro Fluent Python')
        authors = [author_1, author_2, author_3]
    except:
        raise TypeError('Preencha todos os campos')

    table_authors = PrettyTable()
    table_authors.field_names = ["Name", "E-mail", "Description", "Time Registration"]

    for i in range(len(authors)):
        name = authors[i].name
        email = authors[i].email
        description = authors[i].description
        time_registration = authors[i].time_registration
        table_authors.add_row([name, email, description, time_registration])

    print(table_authors)