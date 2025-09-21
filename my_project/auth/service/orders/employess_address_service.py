# EmployessAddressService.py
from typing import List
from my_project.auth.dao.orders import employess_address_dao
from my_project.auth.service.orders.general_service import GeneralService
from my_project.auth.domain import EmployessAddress

class EmployessAddressService(GeneralService):
    _dao = employess_address_dao

    def create(self, employess_address: EmployessAddress) -> None:
        self._dao.create(employess_address)

    def update(self, address_id: int, employess_address: EmployessAddress) -> None:
        self._dao.update(address_id, employess_address)

    def get_all_employess_addresses(self) -> List[EmployessAddress]:
        return self._dao.find_all()

    def get_employess_address_by_id(self, address_id: int) -> EmployessAddress:
        return self._dao.find_by_id(address_id)