# MachineManifectureController.py
from typing import List
from my_project.auth.dao import MachineManifectureDao
from my_project.auth.domain import MachineManifecture

class MachineManifectureController:
    _dao = MachineManifectureDao()

    def find_all(self) -> List[MachineManifecture]:
        return self._dao.find_all()

    def create(self, machine_manifecture: MachineManifecture) -> None:
        self._dao.create(machine_manifecture)

    def find_by_id(self, manifecture_id: int) -> MachineManifecture:
        return self._dao.find_by_id(manifecture_id)

    def update(self, manifecture_id: int, machine_manifecture: MachineManifecture) -> None:
        self._dao.update(manifecture_id, machine_manifecture)

    def delete(self, manifecture_id: int) -> None:
        self._dao.delete(manifecture_id)
