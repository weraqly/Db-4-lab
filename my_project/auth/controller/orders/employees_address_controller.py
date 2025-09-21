# EmployessAddressController.py
from typing import List
from my_project.auth.dao import EmployessAddressDao
from my_project.auth.domain import EmployessAddress

class EmployessAddressController:
    _dao = EmployessAddressDao()

    def find_all(self) -> List[EmployessAddress]:
        return self._dao.find_all()

    def create(self, employess_address: EmployessAddress) -> None:
        self._dao.create(employess_address)

    def find_by_id(self, address_id: int) -> EmployessAddress:
        return self._dao.find_by_id(address_id)

    def update(self, address_id: int, employess_address: EmployessAddress) -> None:
        self._dao.update(address_id, employess_address)

    def delete(self, address_id: int) -> None:
        self._dao.delete(address_id)
