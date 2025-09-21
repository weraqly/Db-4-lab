from typing import List
from my_project import db
from my_project.auth.domain import SaledSnacks

class SaledSnacksDao:
    @staticmethod
    def create(saled_snacks: SaledSnacks) -> None:
        db.session.add(saled_snacks)
        db.session.commit()

    @staticmethod
    def update(saled_id: int, saled_snacks: SaledSnacks) -> None:
        db.session.query(SaledSnacks).filter_by(id=saled_id).update({
            "sale_date": saled_snacks.sale_date,
            "quantity_sold": saled_snacks.quantity_sold,
            "food_machines_id": saled_snacks.food_machines_id,
            "snacks_id": saled_snacks.snacks_id,
        })
        db.session.commit()

    @staticmethod
    def find_all() -> List[SaledSnacks]:
        return db.session.query(SaledSnacks).all()

    @staticmethod
    def find_by_id(saled_id: int) -> SaledSnacks:
        return db.session.query(SaledSnacks).filter_by(id=saled_id).first()
