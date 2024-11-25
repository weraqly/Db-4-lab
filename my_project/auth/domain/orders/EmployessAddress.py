from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class EmployessAddress(db.Model, IDto):
    __tablename__ = "employess_address"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city = db.Column(db.String(255))
    street = db.Column(db.String(255))
    street_number = db.Column(db.String(255))
    district = db.Column(db.String(255))
    city_index = db.Column(db.Integer)
    country = db.Column(db.String(255))

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "city": self.city,
            "street": self.street,
            "street_number": self.street_number,
            "district": self.district,
            "city_index": self.city_index,
            "country": self.country,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> EmployessAddress:
        return EmployessAddress(**dto_dict)