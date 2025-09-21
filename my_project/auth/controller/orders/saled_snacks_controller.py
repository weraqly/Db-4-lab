
from typing import List
from my_project.auth.dao import SaledSnacksDao
from my_project.auth.domain import SaledSnacks

class SaledSnacksController:
    _dao = SaledSnacksDao()

    def find_all(self) -> List[SaledSnacks]:
        return self._dao.find_all()

    def create(self, saled_snacks: SaledSnacks) -> None:
        self._dao.create(saled_snacks)

    def find_by_id(self, saled_id: int) -> SaledSnacks:
        return self._dao.find_by_id(saled_id)

    def update(self, saled_id: int, saled_snacks: SaledSnacks) -> None:
        self._dao.update(saled_id, saled_snacks)

    def delete(self, saled_id: int) -> None:
        self._dao.delete(saled_id)
