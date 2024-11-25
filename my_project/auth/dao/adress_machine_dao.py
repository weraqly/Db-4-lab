from typing import List
from my_project import db
from my_project.auth.domain.orders.AdressMachine import AddressMachine

class AddressMachineDao:
    @staticmethod
    def find_all() -> List[AddressMachine]:
        return db.session.query(AddressMachine).all()

    @staticmethod
    def find_by_id(address_id: int) -> AddressMachine:
        return db.session.query(AddressMachine).filter_by(id=address_id).first()

    @staticmethod
    def create(address_machine: AddressMachine) -> None:
        db.session.add(address_machine)
        db.session.commit()

    @staticmethod
    def update(address_id: int, address_machine: AddressMachine) -> None:
        db.session.query(AddressMachine).filter_by(id=address_id).update({
            "city": address_machine.city,
            "street": address_machine.street,
            "street_number": address_machine.street_number,
            "district": address_machine.district,
            "city_index": address_machine.city_index,
            "country": address_machine.country,
        })
        db.session.commit()

    @staticmethod
    def delete(address_id: int) -> None:
        db.session.query(AddressMachine).filter_by(id=address_id).delete()
        db.session.commit()
