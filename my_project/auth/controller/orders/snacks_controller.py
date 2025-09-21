from typing import List
from my_project.auth.dao import SnacksDao
from my_project.auth.domain import Snacks

class SnacksController:
    _dao = SnacksDao()

    def find_all(self) -> List[Snacks]:
        """
        Отримати всі снеки.
        """
        return self._dao.find_all()

    def create(self, snack: Snacks) -> None:
        """
        Створити новий запис для снеків.
        """
        self._dao.create(snack)

    def find_by_id(self, snack_id: int) -> Snacks:
        """
        Знайти снеки за ID.
        """
        return self._dao.find_by_id(snack_id)

    def update(self, snack_id: int, snack: Snacks) -> None:
        self._dao.update(snack_id, snack)

    def delete(self, snack_id: int) -> None:
        """
        Видалити снеки за ID.
        """
        self._dao.delete(snack_id)
