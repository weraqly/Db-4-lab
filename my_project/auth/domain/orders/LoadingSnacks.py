from __future__ import annotations
from typing import Dict, Any
from sqlalchemy.orm import relationship
from my_project import db
from my_project.auth.domain.i_dto import IDto


class LoadingSnacks(db.Model, IDto):
    __tablename__ = "loading_snacks"

    loading_machine_id = db.Column(db.Integer, db.ForeignKey("loading_machine.id"), primary_key=True)
    snack_id = db.Column(db.Integer, db.ForeignKey("snacks.id"), primary_key=True)
    quantity_snacks = db.Column(db.Integer, nullable=False, default=0)

    # Відносини Many-to-Many із таблицями LoadingMachine і Snacks
    loading_machine = relationship("LoadingMachine", back_populates="loading_snacks")
    snack = relationship("Snacks", back_populates="loading_snacks")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "loading_machine_id": self.loading_machine_id,
            "snack_id": self.snack_id,
            "quantity_snacks": self.quantity_snacks,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> LoadingSnacks:
        return LoadingSnacks(**dto_dict)
