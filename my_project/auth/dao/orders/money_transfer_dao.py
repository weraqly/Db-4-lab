from typing import List
from my_project import db
from my_project.auth.domain import MoneyTransfer

class MoneyTransferDao:
    @staticmethod
    def create(transfer: MoneyTransfer) -> None:
        db.session.add(transfer)
        db.session.commit()

    @staticmethod
    def update(transfer_id: int, transfer: MoneyTransfer) -> None:
        db.session.query(MoneyTransfer).filter_by(id=transfer_id).update({
            "transfer_date": transfer.transfer_date,
            "sum": transfer.sum,
            "quantity": transfer.quantity,
            "denomination_id": transfer.denomination_id,
            "food_machines_id": transfer.food_machines_id,
        })
        db.session.commit()

    @staticmethod
    def find_all() -> List[MoneyTransfer]:
        return db.session.query(MoneyTransfer).all()

    @staticmethod
    def find_by_id(transfer_id: int) -> MoneyTransfer:
        return db.session.query(MoneyTransfer).filter_by(id=transfer_id).first()
