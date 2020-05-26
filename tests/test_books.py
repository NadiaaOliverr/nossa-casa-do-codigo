from model import Book, Category
from dao import BookDatabase

import pytest
from datetime import datetime


@pytest.fixture()
def book():
    def _create_book(title, resume, summary, price, number_pages, isbn, publication_date, category):
        return Book(title, resume, summary, price, number_pages, isbn, publication_date, category)

    return _create_book


@pytest.fixture()
def category():
    def _create_category(name):
        return Category(name)

    return _create_category


def test_not_should_allow_add_title_in_blank(book, category):
    title = ''
    resume = 'Por que não testamos software? Porque é caro? Porque é demorado? Porque é chato?'
    summary = '# Introdução ## 1.1 Era uma vez um projeto sem testes...'
    price = 29.90
    number_pages = 120
    isbn = '9788566250048'
    publication_date = datetime(2020, 4, 20)
    category = category('Programação')

    with pytest.raises(Exception):
        book(title, resume, summary, price, number_pages, isbn, publication_date, category)


def test_not_should_allow_add_title_with_the_same_name(book, category):
    title_1 = 'Clean Code'
    resume_1 = 'Por que não testamos software? Porque é caro? Porque é demorado? Porque é chato?'
    summary_1 = '# Introdução ## 1.1 Era uma vez um projeto sem testes...'
    price_1 = 29.90
    number_pages_1 = 120
    isbn_1 = '9788566250048'
    publication_date_1 = datetime(2020, 10, 20)
    category_1 = category('Programação')

    title_2 = 'Clean Code'
    resume_2 = 'Por que não testamos software? Porque é caro?'
    summary_2 = '# Introdução'
    price_2 = 29.90
    number_pages_2 = 120
    isbn_2 = '9788566250060'
    publication_date_2 = datetime(2020, 10, 26)
    category_2 = category('Engenharia')

    books = BookDatabase()
    book_1 = book(title_1, resume_1, summary_1, price_1, number_pages_1, isbn_1, publication_date_1, category_1)
    book_2 = book(title_2, resume_2, summary_2, price_2, number_pages_2, isbn_2, publication_date_2, category_2)

    with pytest.raises(Exception):
        books.add(book_1)
        books.add(book_2)


def test_not_should_allow_add_resume_in_blank(book, category):
    title = 'Clean Code'
    resume = ''
    summary = '# Introdução ## 1.1 Era uma vez um projeto sem testes...'
    price = 29.90
    number_pages = 120
    isbn = '9788566250048'
    publication_date = datetime(2020, 10, 20)
    category = category('Programação')

    with pytest.raises(Exception):
        book(title, resume, summary, price, number_pages, isbn, publication_date, category)


def test_not_should_allow_add_resume_greater_than_500_characters(book, category):
    title = 'Clean Code'
    resume = (
        'Por que não testamos software? Porque é caro? Porque é demorado? Porque é chato?'
        'Por que não testamos software? Porque é caro? Porque é demorado? Porque é chato?'
        'Por que não testamos software? Porque é caro? Porque é demorado? Porque é chato?'
        'Por que não testamos software? Porque é caro? Porque é demorado? Porque é chato?'
        'Por que não testamos software? Porque é caro? Porque é demorado? Porque é chato?'
        'Por que não testamos software? Porque é caro? Porque é demorado? Porque é chato?'
        'Por que não testamos software? Porque é caro? Porque é demorado? Porque é chato?'
    )
    summary = '# Introdução ## 1.1 Era uma vez um projeto sem testes...'
    price = 29.90
    number_pages = 120
    isbn = '9788566250048'
    publication_date = datetime(2020, 4, 20)
    category = category('Programação')

    with pytest.raises(Exception):
        book(title, resume, summary, price, number_pages, isbn, publication_date, category)


def test_not_should_allow_add_summary_in_blank(book, category):
    title = 'Clean Code'
    resume = 'Por que não testamos software? Porque é caro? Porque é demorado? Porque é chato?'
    summary = ''
    price = 29.90
    number_pages = 120
    isbn = '9788566250048'
    publication_date = datetime(2020, 4, 20)
    category = category('Programação')

    with pytest.raises(Exception):
        book(title, resume, summary, price, number_pages, isbn, publication_date, category)


def test_not_should_allow_add_price_lass_than_20_real(book, category):
    title = 'Clean Code'
    resume = 'Por que não testamos software? Porque é caro? Porque é demorado? Porque é chato?'
    summary = '# Introdução ## 1.1 Era uma vez um projeto sem testes...'
    price = 10.0
    number_pages = 120
    isbn = '9788566250048'
    publication_date = datetime(2020, 4, 20)
    category = category('Programação')

    with pytest.raises(Exception):
        book(title, resume, summary, price, number_pages, isbn, publication_date, category)


def test_not_should_allow_add_isbn_in_blank(book, category):
    title = 'Clean Code'
    resume = 'Por que não testamos software? Porque é caro? Porque é demorado? Porque é chato?'
    summary = '# Introdução ## 1.1 Era uma vez um projeto sem testes...'
    price = 29.90
    number_pages = 120
    isbn = ''
    publication_date = datetime(2020, 4, 20)
    category = category('Programação')

    with pytest.raises(Exception):
        book(title, resume, summary, price, number_pages, isbn, publication_date, category)


def test_not_should_allow_add_isbn_with_same_identification(book, category):
    title_1 = 'Clean Code'
    resume_1 = 'Por que não testamos software? Porque é caro? Porque é demorado? Porque é chato?'
    summary_1 = '# Introdução ## 1.1 Era uma vez um projeto sem testes...'
    price_1 = 29.90
    number_pages_1 = 120
    isbn_1 = '9788566250048'
    publication_date_1 = datetime(2020, 10, 20)
    category_1 = category('Programação')

    title_2 = 'Clean'
    resume_2 = 'Por que não testamos software? Porque é caro?'
    summary_2 = '# Introdução'
    price_2 = 29.90
    number_pages_2 = 120
    isbn_2 = '9788566250048'
    publication_date_2 = datetime(2020, 10, 20)
    category_2 = category('Engenharia')

    books = BookDatabase()
    book_1 = book(title_1, resume_1, summary_1, price_1, number_pages_1, isbn_1, publication_date_1, category_1)
    book_2 = book(title_2, resume_2, summary_2, price_2, number_pages_2, isbn_2, publication_date_2, category_2)

    with pytest.raises(Exception):
        books.add(book_1)
        books.add(book_2)


def test_not_should_allow_add_date_in_past(book, category):
    title = 'Clean Code'
    resume = 'Por que não testamos software? Porque é caro? Porque é demorado? Porque é chato?'
    summary = '# Introdução ## 1.1 Era uma vez um projeto sem testes...'
    price = 29.90
    number_pages = 120
    isbn = '9788566250048'
    publication_date = datetime(2019, 4, 20)
    category = category('Programação')

    with pytest.raises(Exception):
        book(title, resume, summary, price, number_pages, isbn, publication_date, category)


def test_not_should_allow_add_month_invalid_in_date(book, category):
    title = 'Clean Code'
    resume = 'Por que não testamos software? Porque é caro? Porque é demorado? Porque é chato?'
    summary = '# Introdução ## 1.1 Era uma vez um projeto sem testes...'
    price = 29.90
    number_pages = 120
    isbn = '9788566250048'
    category = category('Programação')

    with pytest.raises(ValueError):
        publication_date = datetime(2020, 15, 20)
        book(title, resume, summary, price, number_pages, isbn, publication_date, category)


def test_not_should_allow_add_days_invalid_in_date(book, category):
    title = 'Clean Code'
    resume = 'Por que não testamos software? Porque é caro? Porque é demorado? Porque é chato?'
    summary = '# Introdução ## 1.1 Era uma vez um projeto sem testes...'
    price = 29.90
    number_pages = 120
    isbn = '9788566250048'
    category = category('Programação')

    with pytest.raises(ValueError):
        publication_date = datetime(2020, 12, 40)
        book(title, resume, summary, price, number_pages, isbn, publication_date, category)
