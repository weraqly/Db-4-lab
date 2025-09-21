# SnacksCreatorController.py
from typing import List
from my_project.auth.dao import SnacksCreatorDao
from my_project.auth.domain import SnacksCreator

class SnacksCreatorController:
    _dao = SnacksCreatorDao()

    def find_all(self) -> List[SnacksCreator]:
        return self._dao.find_all()

    def create(self, snacks_creator: SnacksCreator) -> None:
        self._dao.create(snacks_creator)

    def find_by_id(self, creator_id: int) -> SnacksCreator:
        return self._dao.find_by_id(creator_id)

    def update(self, creator_id: int, snacks_creator: SnacksCreator) -> None:
        self._dao.update(creator_id, snacks_creator)

    def delete(self, creator_id: int) -> None:
        self._dao.delete(creator_id)
