# MachineManifectureService.py
from typing import List
from my_project.auth.dao import machine_manifecture_dao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.MachineManifecture import MachineManifecture

class MachineManifectureService(GeneralService):
    _dao = machine_manifecture_dao

    def create(self, machine_manifecture: MachineManifecture) -> None:
        self._dao.create(machine_manifecture)

    def update(self, manifecture_id: int, machine_manifecture: MachineManifecture) -> None:
        self._dao.update(manifecture_id, machine_manifecture)

    def get_all_machine_manifectures(self) -> List[MachineManifecture]:
        return self._dao.find_all()

    def get_machine_manifecture_by_id(self, manifecture_id: int) -> MachineManifecture:
        return self._dao.find_by_id(manifecture_id)

