# LoadingMachineService.py
from typing import List
from my_project.auth.dao import loading_machine_dao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.LoadingMachine import LoadingMachine

class LoadingMachineService(GeneralService):
    _dao = loading_machine_dao

    def create(self, loading_machine: LoadingMachine) -> None:
        self._dao.create(loading_machine)

    def update(self, machine_id: int, loading_machine: LoadingMachine) -> None:
        self._dao.update(machine_id, loading_machine)

    def get_all_loading_machines(self) -> List[LoadingMachine]:
        return self._dao.find_all()

    def get_loading_machine_by_id(self, machine_id: int) -> LoadingMachine:
        return self._dao.find_by_id(machine_id)

