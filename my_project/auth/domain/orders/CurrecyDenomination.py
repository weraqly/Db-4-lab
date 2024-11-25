from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class CurrencyDenominations(db.Model, IDto):
    """
    Model declaration for Currency Denominations.
    """
    __tablename__ = "currency_denominations"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    denomination_type = db.Column(db.String(50))
    denomination_value = db.Column(db.Float)
    currency_name = db.Column(db.String(255))

    def __repr__(self) -> str:
        return f"CurrencyDenominations({self.id}, '{self.denomination_type}', '{self.denomination_value}', '{self.currency_name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Converts domain object to DTO without relationships.
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "denomination_type": self.denomination_type,
            "denomination_value": self.denomination_value,
            "currency_name": self.currency_name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> CurrencyDenominations:
        """
        Creates domain object from DTO.
        :param dto_dict: DTO object
        :return: Domain object
        """
        return CurrencyDenominations(**dto_dict)
