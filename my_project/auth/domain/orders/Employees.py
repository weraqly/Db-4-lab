from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class Employees(db.Model, IDto):
    __tablename__ = "employees"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    phone_number = db.Column(db.String(255))
    experience = db.Column(db.Integer)
    email = db.Column(db.String(255))
    employess_address_id = db.Column(db.Integer, db.ForeignKey("employess_address.id"))

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone_number": self.phone_number,
            "experience": self.experience,
            "email": self.email,
            "employess_address_id": self.employess_address_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Employees:
        return Employees(**dto_dict)