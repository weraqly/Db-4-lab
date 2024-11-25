from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class Menu(db.Model, IDto):
    __tablename__ = "menu"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    quantity = db.Column(db.Integer)
    snacks_id = db.Column(db.Integer, db.ForeignKey("snacks.id"))

    def put_into_dto(self) -> Dict[str, Any]:
        return {"id": self.id, "quantity": self.quantity, "snacks_id": self.snacks_id}

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Menu:
        return Menu(**dto_dict)