from model import Coupon

from typing import List


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
                return coupon
        raise Exception('Cupom Inválido')

    @property
    def coupons(self) -> List[Coupon]:
        return self.__coupons.copy()
       
