from typing import List
from sqlalchemy.orm import joinedload
from my_project import db
from my_project.auth.domain.orders.LoadingMachine import LoadingMachine


class LoadingMachineDao:
    @staticmethod
    def find_all() -> List[LoadingMachine]:
        return db.session.query(LoadingMachine).options(
            joinedload(LoadingMachine.loading_snacks).joinedload("snack")
        ).all()

    @staticmethod
    def find_by_id(machine_id: int) -> LoadingMachine:
        return db.session.query(LoadingMachine).options(
            joinedload(LoadingMachine.loading_snacks).joinedload("snack")
        ).filter_by(id=machine_id).first()

    @staticmethod
    def create(loading_machine: LoadingMachine) -> None:
        db.session.add(loading_machine)
        db.session.commit()

    @staticmethod
    def update(machine_id: int, loading_machine: LoadingMachine) -> None:
        db.session.query(LoadingMachine).filter_by(id=machine_id).update({
            "loading_time": loading_machine.loading_time,
        })
        db.session.commit()

    @staticmethod
    def delete(machine_id: int) -> None:
        db.session.query(LoadingMachine).filter_by(id=machine_id).delete()
        db.session.commit()
