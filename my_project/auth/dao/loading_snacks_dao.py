from typing import List
from my_project import db
from my_project.auth.domain.orders.LoadingSnacks import LoadingSnacks

class LoadingSnacksDao:
    @staticmethod
    def find_all() -> List[LoadingSnacks]:
        return db.session.query(LoadingSnacks).all()

    @staticmethod
    def find_by_ids(loading_machine_id: int, snack_id: int) -> LoadingSnacks:
        return db.session.query(LoadingSnacks).filter_by(
            loading_machine_id=loading_machine_id,
            snack_id=snack_id
        ).first()

    @staticmethod
    def create(loading_snack: LoadingSnacks) -> None:
        db.session.add(loading_snack)
        db.session.commit()

    @staticmethod
    def delete(loading_machine_id: int, snack_id: int) -> None:
        db.session.query(LoadingSnacks).filter_by(
            loading_machine_id=loading_machine_id,
            snack_id=snack_id
        ).delete()
        db.session.commit()
