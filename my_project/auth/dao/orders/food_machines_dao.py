from typing import List
from sqlalchemy.orm import joinedload
from my_project import db
from my_project.auth.domain import FoodMachine

class FoodMachineDao:
    @staticmethod
    def find_all() -> List[FoodMachine]:
        return db.session.query(FoodMachine).options(joinedload(FoodMachine.address_machine)).all()

    @staticmethod
    def find_by_id(machine_id: int) -> FoodMachine:
        return db.session.query(FoodMachine).options(joinedload(FoodMachine.address_machine)).filter_by(id=machine_id).first()

    @staticmethod
    def create(food_machine: FoodMachine) -> None:
        db.session.add(food_machine)
        db.session.commit()

    @staticmethod
    def update(machine_id: int, food_machine: FoodMachine) -> None:
        db.session.query(FoodMachine).filter_by(id=machine_id).update({
            "name": food_machine.name,
            "gps_coordinates": food_machine.gps_coordinates,
            "address_machine_id": food_machine.address_machine_id,
        })
        db.session.commit()

    @staticmethod
    def delete(machine_id: int) -> None:
        db.session.query(FoodMachine).filter_by(id=machine_id).delete()
        db.session.commit()
