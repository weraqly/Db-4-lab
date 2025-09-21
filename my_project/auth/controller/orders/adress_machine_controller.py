# AddressMachineController.py
from typing import List
from my_project.auth.dao import AddressMachineDao
from my_project.auth.domain import AddressMachine
from sqlalchemy.orm import joinedload
from my_project import db

class AddressMachineController:
    _dao = AddressMachineDao()

    def find_all(self) -> List[AddressMachine]:
        return self._dao.find_all()

    def find_all_with_related_data(self):
        return db.session.query(AddressMachine).options(
            joinedload(AddressMachine.related_table_name)
        ).all()

    def create(self, address_machine: AddressMachine) -> None:
        self._dao.create(address_machine)

    def find_by_id(self, address_id: int) -> AddressMachine:
        return self._dao.find_by_id(address_id)

    def update(self, address_id: int, address_machine: AddressMachine) -> None:
        self._dao.update(address_id, address_machine)

    def delete(self, address_id: int) -> None:
        self._dao.delete(address_id)
