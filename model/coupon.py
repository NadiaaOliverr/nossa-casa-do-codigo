from datetime import datetime


class Coupon:

    __attributes = ('_code', '_expiration_date', '_percent_discount')

    def __init__(self, code: str, expiration_date: datetime, percent_discount: int) -> None:
        self.__set_code(code)
        self.__set_expiration_date(expiration_date)
        self.__set_percent_discount(percent_discount)

    def __eq__(self, other: 'Coupon') -> bool:
        return self.code == other.code

    def __ne__(self, other: 'Coupon') -> bool:
        return not self.__eq__(other)

    def __setattr__(self, key, value):
        if key not in self.__attributes:
            raise AttributeError(
                f'Não foi possível adicionar o atributo {key}')
        object.__setattr__(self, key, value)

    def __str__(self):
        return (
            f'Código: {self._code}\n'
            f'Data de expiração: {self._expiration_date}\n'
            f'Desconto: {self._percent_discount}'
        )

    def __set_code(self, code: str) -> None:
        if not code or len(code.split()) == 0:
            raise Exception('Código não pode ficar em branco ou ser nulo')
        self._code = code

    def __set_expiration_date(self, expiration_date: datetime) -> None:
        current_date = datetime.now()
        if current_date > expiration_date:
            raise Exception(
                'A data de expiração tem que ser maior que a data atual'
            )
        self._expiration_date = expiration_date

    def __set_percent_discount(self, percent_discount: int) -> None:
        if percent_discount <= 0 or percent_discount > 100:
            raise Exception(
                'O percentual de desconto tem que estar entre 1 e 100'
            )
        self._percent_discount = percent_discount

    @property
    def code(self):
        return self._code

    @property
    def expiration_date(self):
        return self._expiration_date

    @property
    def percent_discount(self):
        return self._percent_discount

    @property
    def is_valid(self):
        return self.expiration_date > datetime.now() 
