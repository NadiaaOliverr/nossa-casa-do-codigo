from src.authors.authors import Author

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

    with pytest.raises(TypeError):
        author(name, email, description)


def test_not_should_allow_add_an_email_invalid(author):
    name = 'Luciano Ramanho'
    email = 'lucianor'
    description = 'Luciano Ramalho é programador Python desde 1998, Fellow da Python Software Foundation; é sócio do Python.pro.br ' \
                  '– uma empresa de treinamento – e cofundador do Garoa Hacker Clube, ' \
                  'o primeiro hackerspace do Brasil.'

    with pytest.raises(Exception):
        author(name, email, description)


def test_not_should_allow_add_an_description_bigger_what_400_characters(author):
    name = 'Luciano Ramalho'
    email = 'lucianor@hotmail.com'
    description = 'Luciano Ramalho é programador Python desde 1998, Fellow da Python Software Foundation; é sócio do Python.pro.br ' \
                  '– uma empresa de treinamento – e cofundador do Garoa Hacker Clube, ' \
                  'o primeiro hackerspace do Brasil. Luciano Ramalho é programador Python desde 1998, Fellow da Python Software ' \
                  'Foundation; é sócio do Python.pro.br – uma empresa de treinamento – e cofundador do Garoa Hacker Clube, ' \
                  'o primeiro hackerspace do Brasil.'

    with pytest.raises(Exception):
        author(name, email, description)
