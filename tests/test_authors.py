from model import Author
from dao import AuthorDatabase

import pytest


@pytest.fixture()
def author():
    def _create_author(name, email, description):
        return Author(name, email, description)

    return _create_author


def test_not_should_allow_add_fields_in_blank(author):
    name = ''
    email = 'lucianor@hotmail.com'
    description = 'Luciano Ramalho é programador Python desde 1998, Fellow da Python Software Foundation; é sócio do Python.pro.br ' \
                  '– uma empresa de treinamento – e cofundador do Garoa Hacker Clube, ' \
                  'o primeiro hackerspace do Brasil.'

    with pytest.raises(Exception):
        author(name, email, description)


def test_not_should_allow_add_an_email_invalid(author):
    name = 'Luciano Ramanho'
    email = 'lucianor'
    description = 'Luciano Ramalho é programador Python desde 1998, Fellow da Python Software Foundation; é sócio do Python.pro.br ' \
                  '– uma empresa de treinamento – e cofundador do Garoa Hacker Clube, ' \
                  'o primeiro hackerspace do Brasil.'

    with pytest.raises(Exception):
        author(name, email, description)


def test_not_should_allow_add_an_description_greater_than_400_characters(author):
    name = 'Luciano Ramalho'
    email = 'lucianor@hotmail.com'
    description = 'Luciano Ramalho é programador Python desde 1998, Fellow da Python Software Foundation; é sócio do Python.pro.br ' \
                  '– uma empresa de treinamento – e cofundador do Garoa Hacker Clube, ' \
                  'o primeiro hackerspace do Brasil. Luciano Ramalho é programador Python desde 1998, Fellow da Python Software ' \
                  'Foundation; é sócio do Python.pro.br – uma empresa de treinamento – e cofundador do Garoa Hacker Clube, ' \
                  'o primeiro hackerspace do Brasil.o primeiro hackerspace do Brasil. Luciano Ramalho é programador Python desde 1998, Fellow da Python Software ' \
                  'Foundation; é sócio do Python.pro.br – uma empresa de treinamento – e cofundador do Garoa Hacker Clube, ' \
                  'o primeiro hackerspace do Brasil.'

    with pytest.raises(Exception):
        author(name, email, description)


def test_not_should_allow_add_author_with_the_same_email(author):
    name_1 = 'Luciano'
    email_1 = 'lucianor@hotmail.com'
    description_1 = 'Luciano Ramalho é programador Python desde 1998'

    name_2 = 'Luciano Ramalho'
    email_2 = 'lucianor@hotmail.com'
    description_2 = 'Luciano Ramalho é programador Python desde 1998, Fellow da Python Software Foundation; é sócio do Python.pro.br '

    author_1 = author(name_1, email_1, description_1)
    author_2 = author(name_2, email_2, description_2)

    authors = AuthorDatabase()

    with pytest.raises(Exception):
        authors.add(author_1)
        authors.add(author_2)
