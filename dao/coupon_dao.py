from model import Coupon

from typing import List
from datetime import datetime


class CouponDatabase:

    def __init__(self):
        self.__coupons = []

    def add(self, coupon: Coupon) -> None:
        if coupon in self.__coupons:
            raise Exception('Cupom duplicado. Isto não é permitido')
        self.__coupons.append(coupon)

    def find_by_code(self, code: str) -> Coupon:
        for coupon in self.__coupons:
            if code == coupon.code:
                self.__check_coupon_expiration_date(coupon)
                return coupon
        raise Exception('Cupom Inválido')

    def __check_coupon_expiration_date(self, coupon: Coupon) -> bool:
        if datetime.now() > coupon.expiration_date:
            raise Exception('O Cupom está expirado')
        return False

    @property
    def coupons(self) -> List[Coupon]:
        return self.__coupons.copy()
       
