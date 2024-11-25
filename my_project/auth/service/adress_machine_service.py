# AddressMachineService.py
from typing import List
from my_project.auth.dao import adress_machine_dao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.AdressMachine import AddressMachine

class AdressMachineService(GeneralService):
    _dao = adress_machine_dao

    def create(self, address_machine: AddressMachine) -> None:
        self._dao.create(address_machine)

    def update(self, address_id: int, address_machine: AddressMachine) -> None:
        self._dao.update(address_id, address_machine)

    def get_all_address_machines(self) -> List[AddressMachine]:
        return self._dao.find_all()

    def get_address_machine_by_id(self, address_id: int) -> AddressMachine:
        return self._dao.find_by_id(address_id)

