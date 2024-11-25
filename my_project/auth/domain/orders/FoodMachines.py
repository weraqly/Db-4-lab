from __future__ import annotations
from typing import Dict, Any
from sqlalchemy.orm import relationship
from my_project import db
from my_project.auth.domain.i_dto import IDto

class FoodMachine(db.Model, IDto):
    __tablename__ = "food_machine"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    gps_coordinates = db.Column(db.String(255), nullable=True)
    address_machine_id = db.Column(db.Integer, db.ForeignKey("address_machine.id"), nullable=False)

    # Зв'язок до AddressMachine
    address_machine = relationship("AddressMachine", back_populates="food_machines")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "gps_coordinates": self.gps_coordinates,
            "address_machine": self.address_machine.put_into_dto() if self.address_machine else None,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> FoodMachine:
        return FoodMachine(**dto_dict)
