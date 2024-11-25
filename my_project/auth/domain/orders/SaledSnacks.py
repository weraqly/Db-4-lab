from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class SaledSnacks(db.Model, IDto):
    __tablename__ = "saled_snacks"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sale_date = db.Column(db.DateTime)
    quantity_sold = db.Column(db.Integer)
    food_machines_id = db.Column(db.Integer, db.ForeignKey("food_machines.id"))
    snacks_id = db.Column(db.Integer, db.ForeignKey("snacks.id"))

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "sale_date": str(self.sale_date),
            "quantity_sold": self.quantity_sold,
            "food_machines_id": self.food_machines_id,
            "snacks_id": self.snacks_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> SaledSnacks:
        return SaledSnacks(**dto_dict)