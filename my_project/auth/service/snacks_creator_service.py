# SnacksCreatorService.py
from typing import List
from my_project.auth.dao import snacks_creator_dao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.SnacksCreator import SnacksCreator

class SnacksCreatorService(GeneralService):
    _dao = snacks_creator_dao

    def create(self, snacks_creator: SnacksCreator) -> None:
        self._dao.create(snacks_creator)

    def update(self, creator_id: int, snacks_creator: SnacksCreator) -> None:
        self._dao.update(creator_id, snacks_creator)

    def get_all_snacks_creators(self) -> List[SnacksCreator]:
        return self._dao.find_all()

    def get_snacks_creator_by_id(self, creator_id: int) -> SnacksCreator:
        return self._dao.find_by_id(creator_id)

