from datetime import datetime
from typing import Tuple

from model import Category


class Book:

    def __init__(
            self, title: str, resume: str, summary: str,
            price: float, number_pages: int, isbn: str,
            publication_date: Tuple[int, int, int], category: Category
    ) -> None:
        self.__set_title(title)
        self.__set_resume(resume)
        self.__set_summary(summary)
        self.__set_price(price)
        self.__set_number_pages(number_pages)
        self.__set_isbn(isbn)
        self.__set_publication_date(publication_date)
        self.__set_category(category)

    def __set_title(self, title: str) -> None:
        title_is_empty = len(title) == 0
        if title_is_empty:
            raise Exception('Título não pode ser vazio')
        self.__title = title

    def __eq__(self, other: 'Book') -> bool:
        return self.title == other.title or self.isbn == other.isbn

    def __ne__(self, other: 'Book'):
        return not self.__eq__(other)

    def __str__(self) -> str:
        return (
            f'Título: {self.title}\n'
            f'Resumo: {self.resume}\n'
            f'Sumário: {self.summary}\n'
            f'Preço: R$ {self.price}\n'
            f'Número de Páginas: {self.number_pages}\n'
            f'ISBN: {self.isbn}\n'
            f'Data de Publicação: {self.publication_date}\n'
            f'Categoria: {self.categoria}\n'
        )

    def __set_resume(self, resume: str) -> None:
        resume_is_empty = len(resume) == 0
        resume_is_full = len(resume) > 500
        if resume_is_empty:
            raise Exception('Resumo não pode ser vazio')
        if resume_is_full:
            raise Exception('Resumo não pode conter mais que 500 caracteres')
        self.__resume = resume

    def __set_summary(self, summary: str) -> None:
        summary_is_empty = len(summary) == 0
        if summary_is_empty:
            raise Exception('Sumário não pode ser vazio')
        self.__summary = summary

    def __set_price(self, price: float) -> None:
        if price < 20.0:
            raise Exception('Preço tem que ser maior do que R$ 20,00 reais')
        self.__price = price

    def __set_number_pages(self, number_pages: int) -> None:
        if number_pages < 100:
            raise Exception('Número de páginas não pode ser menor que 100')
        self.__number_pages = number_pages

    def __set_isbn(self, isbn: str) -> None:
        isbn_is_empty = len(isbn) == 0
        if isbn_is_empty:
            raise Exception('ISBN não pode ser vazio')
        self.__isbn = isbn

    def __set_publication_date(
            self, publication_date: Tuple[int, int, int]
    ) -> None:
        year = publication_date[0]
        month = publication_date[1]
        day = publication_date[2]
        publication_date_formated = datetime(year, month, day)
        publication_date = publication_date_formated
        current_date = datetime.now()
        if current_date > publication_date_formated:
            raise Exception(
                'A data de publicação tem que ser maior que a data atual'
            )
        self.__publication_date = publication_date

    def __set_category(self, category: Category) -> None:
        self.__category = category

    @property
    def title(self) -> str:
        return self.__title

    @property
    def resume(self) -> str:
        return self.__resume

    @property
    def summary(self) -> str:
        return self.__summary

    @property
    def price(self) -> float:
        return self.__price

    @property
    def isbn(self) -> str:
        return self.__isbn

    @property
    def number_pages(self) -> int:
        return self.__number_pages

    @property
    def publication_date(self) -> str:
        return self.__publication_date.strftime("%d/%m/%Y")

    @property
    def categoria(self) -> Category:
        return self.__category
