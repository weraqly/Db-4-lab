from typing import List
from my_project import db
from my_project.auth.domain import Snacks

class SnacksDao:
    @staticmethod
    def find_all() -> List[Snacks]:
        """
        Отримати всі снеки.
        """
        return db.session.query(Snacks).all()

    @staticmethod
    def find_by_id(snack_id: int) -> Snacks:
        """
        Знайти снеки за їх ID.
        """
        return db.session.query(Snacks).filter_by(id=snack_id).first()

    @staticmethod
    def create(snack: Snacks) -> None:
        """
        Створити новий запис для снеків.
        """
        db.session.add(snack)
        db.session.commit()

    @staticmethod
    def update(snack_id: int, snack: Snacks) -> None:
        db.session.query(Snacks).filter_by(id=snack_id).update({
            "name": snack.name,
            "price": snack.price
        })
        db.session.commit()

    @staticmethod
    def delete(snack_id: int) -> None:
        """
        Видалити снеки за ID.
        """
        db.session.query(Snacks).filter_by(id=snack_id).delete()
        db.session.commit()
