from typing import List
from my_project import db
from my_project.auth.domain import Menu

class MenuDao:
    @staticmethod
    def create(menu: Menu) -> None:
        db.session.add(menu)
        db.session.commit()

    @staticmethod
    def update(menu_id: int, menu: Menu) -> None:
        db.session.query(Menu).filter_by(id=menu_id).update({
            "quantity": menu.quantity,
            "snacks_id": menu.snacks_id,
        })
        db.session.commit()

    @staticmethod
    def find_all() -> List[Menu]:
        return db.session.query(Menu).all()

    @staticmethod
    def find_by_id(menu_id: int) -> Menu:
        return db.session.query(Menu).filter_by(id=menu_id).first()
