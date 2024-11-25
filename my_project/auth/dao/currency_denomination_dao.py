from typing import List
from my_project import db
from my_project.auth.domain.orders.CurrecyDenomination import CurrencyDenominations

class CurrencyDenominationsDao:
    @staticmethod
    def create(currency: CurrencyDenominations) -> None:
        db.session.add(currency)
        db.session.commit()

    @staticmethod
    def update(currency_id: int, currency: CurrencyDenominations) -> None:
        db.session.query(CurrencyDenominations).filter_by(id=currency_id).update({
            "denomination_type": currency.denomination_type,
            "denomination_value": currency.denomination_value,
            "currency_name": currency.currency_name,
        })
        db.session.commit()

    @staticmethod
    def find_all() -> List[CurrencyDenominations]:
        return db.session.query(CurrencyDenominations).all()

    @staticmethod
    def find_by_id(currency_id: int) -> CurrencyDenominations:
        return db.session.query(CurrencyDenominations).filter_by(id=currency_id).first()
