from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class MoneyTransfer(db.Model, IDto):
    __tablename__ = "money_transfer"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    transfer_date = db.Column(db.DateTime)
    sum = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    denomination_id = db.Column(db.Integer, db.ForeignKey("currency_denominations.id"))
    food_machines_id = db.Column(db.Integer, db.ForeignKey("food_machines.id"))

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "transfer_date": str(self.transfer_date),
            "sum": self.sum,
            "quantity": self.quantity,
            "denomination_id": self.denomination_id,
            "food_machines_id": self.food_machines_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> MoneyTransfer:
        return MoneyTransfer(**dto_dict)