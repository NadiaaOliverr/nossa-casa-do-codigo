from datetime import datetime
from typing import Tuple


class CouponDatabase:

    def __init__(self):
        self.__coupons = []

    def add_coupon(self, code: str, expiration_date: Tuple[int, int, int],
                   percent_discount: int):
        self.__set_code(code)
        self.__set_expiration_date(expiration_date)
        self.__set_percent_discount(percent_discount)

        self.__coupons.append(
            (self.__code, self.__expiration_date, self.__percent_discount)
        )

    def __set_code(self, code: str) -> None:
        code_is_empty = len(code) == 0 or len(code.split()) == 0
        if code_is_empty:
            raise Exception('Código não pode ficar em branco')
        self.__code = code

    def __set_expiration_date(self, expiration_date: Tuple[int, int, int]) -> None:
        year = expiration_date[0]
        month = expiration_date[1]
        day = expiration_date[2]
        expiration_date = datetime(year, month, day)
        current_date = datetime.now()
        if current_date > expiration_date:
            raise Exception(
                'A data de expiração tem que ser maior que a data atual'
            )
        self.__expiration_date = expiration_date

    def __set_percent_discount(self, percent_discount: int) -> None:
        if percent_discount <= 0 or percent_discount > 100:
            raise Exception(
                'O percentual de desconto tem que estar entre 1 e 100'
            )
        self.__percent_discount = percent_discount

    def get_percent_if_coupon_is_valid(self, code: str) -> None:
        for coupoun in self.__coupons:
            name, data, desconto = coupoun
            if name == code:
                return desconto
        raise Exception('Cupom Inválido')
