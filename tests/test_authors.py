from src.authors.authors import Author
from src.authors.excecoes import NameRequired, DescriptionRequired, DescriptionFull, EmailValid, TimeRegistrationNull

import pytest
from datetime import datetime

@pytest.fixture
def authors():
    return Author()

#test_nao_deve_permitir_adicionar_uma_descricao_maior_que_400_caracteres
def test_not_should_allow_add_an_description_bigger_what_400_characters(authors):
    name = 'Luciano Ramalho'
    email = 'lucianor@hotmail.com'
    description = 'Luciano Ramalho é programador Python desde 1998, Fellow da Python Software Foundation; é sócio do Python.pro.br ' \
                  '– uma empresa de treinamento – e cofundador do Garoa Hacker Clube, ' \
                  'o primeiro hackerspace do Brasil. Luciano Ramalho é programador Python desde 1998, Fellow da Python Software ' \
                  'Foundation; é sócio do Python.pro.br – uma empresa de treinamento – e cofundador do Garoa Hacker Clube, ' \
                  'o primeiro hackerspace do Brasil.'
    time_registration = datetime.now().strftime("%d/%m/%Y às %H:%M:%S.%f - BRT")

    with pytest.raises(DescriptionFull):
        authors.set_author(name, email, description, time_registration)

#test_nao_deve_permitir_adicionar_nome_em_branco porque o nome é obrigatório
def test_not_should_allow_add_name_in_blank(authors):
    name = ''
    email = 'lucianor@hotmail.com'
    description = 'Luciano Ramalho é programador Python desde 1998, Fellow da Python Software Foundation; é sócio do Python.pro.br ' \
                  '– uma empresa de treinamento – e cofundador do Garoa Hacker Clube, ' \
                  'o primeiro hackerspace do Brasil.'
    time_registration = datetime.now().strftime("%d/%m/%Y às %H:%M:%S.%f - BRT")

    with pytest.raises(NameRequired):
        authors.set_author(name, email, description, time_registration)

#test_nao_deve_permitir_adicionar_descricao_em_branco porque a descrição é obrigatória
def test_not_should_allow_add_description_in_blank(authors):
    name = 'Luciano Ramalho'
    email = 'lucianor@hotmail.com'
    description = ''
    time_registration = datetime.now().strftime("%d/%m/%Y às %H:%M:%S.%f - BRT")

    with pytest.raises(DescriptionRequired):
        authors.set_author(name, email, description, time_registration)

#test_nao_deve_permitir_adicionar_um_email_invalido
def test_not_should_allow_add_an_email_invalid(authors):
    name = 'Luciano Ramanho'
    email = 'lucianor'
    description = 'Luciano Ramalho é programador Python desde 1998, Fellow da Python Software Foundation; é sócio do Python.pro.br ' \
                  '– uma empresa de treinamento – e cofundador do Garoa Hacker Clube, ' \
                  'o primeiro hackerspace do Brasil.'
    time_registration = datetime.now().strftime("%d/%m/%Y às %H:%M:%S.%f - BRT")

    with pytest.raises(EmailValid):
        authors.set_author(name, email, description, time_registration)

#test_nao_deve_permitir_o_instante_ser_nulo
def test_not_should_allow_the_instant_be_null(authors):
    name = 'Luciano Ramanho'
    email = 'lucianor@hotmail.com'
    description = 'Luciano Ramalho é programador Python desde 1998, Fellow da Python Software Foundation; é sócio do Python.pro.br ' \
                  '– uma empresa de treinamento – e cofundador do Garoa Hacker Clube, ' \
                  'o primeiro hackerspace do Brasil.'
    time_registration = None

    with pytest.raises(TimeRegistrationNull):
        authors.set_author(name, email, description, time_registration)