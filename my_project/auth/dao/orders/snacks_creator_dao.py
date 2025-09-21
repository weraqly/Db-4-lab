from typing import List
from my_project import db
from my_project.auth.domain import SnacksCreator

class SnacksCreatorDao:
    @staticmethod
    def create(snacks_creator: SnacksCreator) -> None:
        db.session.add(snacks_creator)
        db.session.commit()

    @staticmethod
    def update(creator_id: int, snacks_creator: SnacksCreator) -> None:
        db.session.query(SnacksCreator).filter_by(id=creator_id).update({
            "name": snacks_creator.name
        })
        db.session.commit()

    @staticmethod
    def find_all() -> List[SnacksCreator]:
        return db.session.query(SnacksCreator).all()

    @staticmethod
    def find_by_id(creator_id: int) -> SnacksCreator:
        return db.session.query(SnacksCreator).filter_by(id=creator_id).first()
