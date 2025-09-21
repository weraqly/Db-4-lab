from typing import List
from my_project.auth.dao import LoadingSnacksDao
from my_project.auth.domain import LoadingSnacks

class LoadingSnacksController:
    _dao = LoadingSnacksDao()

    def find_all(self) -> List[LoadingSnacks]:
        return self._dao.find_all()

    def find_by_ids(self, loading_machine_id: int, snack_id: int) -> LoadingSnacks:
        return self._dao.find_by_ids(loading_machine_id, snack_id)

    def create(self, loading_snack: LoadingSnacks) -> None:
        self._dao.create(loading_snack)

    def delete(self, loading_machine_id: int, snack_id: int) -> None:
        self._dao.delete(loading_machine_id, snack_id)
