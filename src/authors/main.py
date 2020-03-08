from src.authors.authors import Author

from datetime import datetime

def time_author_registration():
    return datetime.now().strftime("%d/%m/%Y às %H:%M:%S.%f - BRT")

def registration_author(author):
    author.set_author('Susan Cain', 'scain@sweatmail.com', 'Autora do livro O Poder dos Quietos', time_author_registration())
    author.set_author('Albert Einstein', 'einstein@pandora.be', 'Autor do livro Como Vejo o Mundo', time_author_registration())
    author.set_author('Roger S. Pressman', 'presman@engenharia.com', 'Autor do Livro de Engenharia de Software', time_author_registration())
    author.set_author('Luciano Ramalho', 'lucianor@hotmail.com', 'Autor do livro Fluent Python', time_author_registration())
    author.set_author('Caio Incau', 'caioincau@yahoo.com.br', 'Autor do livro Vue.js-Construa aplicações incríveis', time_author_registration())
    author.set_author('Paulo Silveira', 'paulosilveira@hotmail.com', 'Autor do livro Lógica de Programação', time_author_registration())

def all_authors(author):
    author.print_table_all_authors()

if __name__ == '__main__':
    author = Author()
    registration_author(author)
    all_authors(author)

