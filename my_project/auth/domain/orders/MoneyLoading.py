from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class MoneyLoading(db.Model, IDto):
    __tablename__ = "money_loading"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    loading_date = db.Column(db.DateTime)
    loaded_amount = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    denomination_id = db.Column(db.Integer, db.ForeignKey("currency_denominations.id"))
    food_machines_id = db.Column(db.Integer, db.ForeignKey("food_machines.id"))

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "loading_date": str(self.loading_date),
            "loaded_amount": self.loaded_amount,
            "quantity": self.quantity,
            "denomination_id": self.denomination_id,
            "food_machines_id": self.food_machines_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> MoneyLoading:
        return MoneyLoading(**dto_dict)