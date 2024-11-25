# SaledSnacksService.py
from typing import List
from my_project.auth.dao import saled_snacks_dao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.SaledSnacks import SaledSnacks

class SaledSnacksService(GeneralService):
    _dao = saled_snacks_dao

    def create(self, saled_snacks: SaledSnacks) -> None:
        self._dao.create(saled_snacks)

    def update(self, saled_id: int, saled_snacks: SaledSnacks) -> None:
        self._dao.update(saled_id, saled_snacks)

    def get_all_saled_snacks(self) -> List[SaledSnacks]:
        return self._dao.find_all()

    def get_saled_snacks_by_id(self, saled_id: int) -> SaledSnacks:
        return self._dao.find_by_id(saled_id)