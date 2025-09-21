from typing import List
from my_project.auth.dao import LoadingMachineDao
from my_project.auth.domain import LoadingMachine


class LoadingMachineController:
    _dao = LoadingMachineDao()

    def find_all(self) -> List[LoadingMachine]:
        return self._dao.find_all()

    def find_by_id(self, machine_id: int) -> LoadingMachine:
        return self._dao.find_by_id(machine_id)

    def create(self, loading_machine: LoadingMachine) -> None:
        self._dao.create(loading_machine)

    def update(self, machine_id: int, loading_machine: LoadingMachine) -> None:
        self._dao.update(machine_id, loading_machine)

    def delete(self, machine_id: int) -> None:
        self._dao.delete(machine_id)
