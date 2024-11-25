from __future__ import annotations
from typing import Dict, Any
from sqlalchemy.orm import relationship
from my_project import db
from my_project.auth.domain.i_dto import IDto


class LoadingMachine(db.Model, IDto):
    __tablename__ = "loading_machine"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    loading_time = db.Column(db.DateTime, nullable=False)

    # Зв’язок Many-to-Many із Snacks через LoadingSnacks
    loading_snacks = relationship("LoadingSnacks", back_populates="loading_machine")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "loading_time": str(self.loading_time),
            "loading_snacks": [
                {
                    "snack": ls.snack.put_into_dto(),  # Тягнемо повні дані про снек
                    "quantity_snacks": ls.quantity_snacks,  # Додаткові дані з проміжної таблиці
                }
                for ls in self.loading_snacks
            ],
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> LoadingMachine:
        return LoadingMachine(**dto_dict)
