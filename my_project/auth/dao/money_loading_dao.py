from typing import List
from my_project import db
from my_project.auth.domain.orders.MoneyLoading import MoneyLoading

class MoneyLoadingDao:
    @staticmethod
    def create(loading: MoneyLoading) -> None:
        db.session.add(loading)
        db.session.commit()

    @staticmethod
    def update(loading_id: int, loading: MoneyLoading) -> None:
        db.session.query(MoneyLoading).filter_by(id=loading_id).update({
            "loading_date": loading.loading_date,
            "loaded_amount": loading.loaded_amount,
            "quantity": loading.quantity,
            "denomination_id": loading.denomination_id,
            "food_machines_id": loading.food_machines_id,
        })
        db.session.commit()

    @staticmethod
    def find_all() -> List[MoneyLoading]:
        return db.session.query(MoneyLoading).all()

    @staticmethod
    def find_by_id(loading_id: int) -> MoneyLoading:
        return db.session.query(MoneyLoading).filter_by(id=loading_id).first()

