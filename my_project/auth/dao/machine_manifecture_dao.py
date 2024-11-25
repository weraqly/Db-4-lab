from typing import List
from my_project import db
from my_project.auth.domain.orders.MachineManifecture import MachineManifecture

class MachineManifectureDao:
    @staticmethod
    def create(machine_manifecture: MachineManifecture) -> None:
        db.session.add(machine_manifecture)
        db.session.commit()

    @staticmethod
    def update(manifecture_id: int, machine_manifecture: MachineManifecture) -> None:
        db.session.query(MachineManifecture).filter_by(id=manifecture_id).update({
            "name": machine_manifecture.name
        })
        db.session.commit()

    @staticmethod
    def find_all() -> List[MachineManifecture]:
        return db.session.query(MachineManifecture).all()

    @staticmethod
    def find_by_id(manifecture_id: int) -> MachineManifecture:
        return db.session.query(MachineManifecture).filter_by(id=manifecture_id).first()
