# CurrencyDenominationsController.py
from typing import List
from my_project.auth.dao.currency_denomination_dao import CurrencyDenominationsDao
from my_project.auth.domain.orders.CurrecyDenomination import CurrencyDenominations

class CurrencyDenominationsController:
    _dao = CurrencyDenominationsDao()

    def find_all(self) -> List[CurrencyDenominations]:
        return self._dao.find_all()

    def create(self, currency: CurrencyDenominations) -> None:
        self._dao.create(currency)

    def find_by_id(self, currency_id: int) -> CurrencyDenominations:
        return self._dao.find_by_id(currency_id)

    def update(self, currency_id: int, currency: CurrencyDenominations) -> None:
        self._dao.update(currency_id, currency)

    def delete(self, currency_id: int) -> None:
        self._dao.delete(currency_id)
