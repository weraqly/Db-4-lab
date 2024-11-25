from typing import List
from my_project import db
from my_project.auth.domain.orders.EmployessAddress import EmployessAddress

class EmployessAddressDao:
    @staticmethod
    def create(employess_address: EmployessAddress) -> None:
        db.session.add(employess_address)
        db.session.commit()

    @staticmethod
    def update(address_id: int, employess_address: EmployessAddress) -> None:
        db.session.query(EmployessAddress).filter_by(id=address_id).update({
            "city": employess_address.city,
            "street": employess_address.street,
            "street_number": employess_address.street_number,
            "district": employess_address.district,
            "city_index": employess_address.city_index,
            "country": employess_address.country,
        })
        db.session.commit()

    @staticmethod
    def find_all() -> List[EmployessAddress]:
        return db.session.query(EmployessAddress).all()

    @staticmethod
    def find_by_id(address_id: int) -> EmployessAddress:
        return db.session.query(EmployessAddress).filter_by(id=address_id).first()
