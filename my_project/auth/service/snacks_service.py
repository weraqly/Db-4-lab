# SnacksService.py
from typing import List
from my_project.auth.dao import snacks_dao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.Snacks import Snacks

class SnacksService(GeneralService):
    _dao = snacks_dao

    def create(self, snacks: Snacks) -> None:
        self._dao.create(snacks)

    def update(self, snacks_id: int, snacks: Snacks) -> None:
        self._dao.update(snacks_id, snacks)

    def get_all_snacks(self) -> List[Snacks]:
        return self._dao.find_all()

    def get_snacks_by_id(self, snacks_id: int) -> Snacks:
        return self._dao.find_by_id(snacks_id)
