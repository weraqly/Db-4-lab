from __future__ import annotations
from typing import Dict, Any
from sqlalchemy.orm import relationship
from my_project import db
from my_project.auth.domain.i_dto import IDto


class Snacks(db.Model, IDto):
    __tablename__ = "snacks"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)

    # Зв’язок Many-to-Many із LoadingMachine через LoadingSnacks
    loading_snacks = relationship("LoadingSnacks", back_populates="snack")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Snacks:
        return Snacks(**dto_dict)
