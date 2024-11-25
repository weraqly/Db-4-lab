from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class Services(db.Model, IDto):
    __tablename__ = "services"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    service_type = db.Column(db.String(255))
    service_date = db.Column(db.DateTime)
    food_machine_id = db.Column(db.Integer, db.ForeignKey("food_machines.id"))
    employees_id = db.Column(db.Integer, db.ForeignKey("employees.id"))

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "service_type": self.service_type,
            "service_date": str(self.service_date),
            "food_machine_id": self.food_machine_id,
            "employees_id": self.employees_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Services:
        return Services(**dto_dict)