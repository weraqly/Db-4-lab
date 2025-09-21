# MoneyLoadingController.py
from typing import List
from my_project.auth.dao import MoneyLoadingDao
from my_project.auth.domain import MoneyLoading

class MoneyLoadingController:
    _dao = MoneyLoadingDao()

    def find_all(self) -> List[MoneyLoading]:
        return self._dao.find_all()

    def create(self, loading: MoneyLoading) -> None:
        self._dao.create(loading)

    def find_by_id(self, loading_id: int) -> MoneyLoading:
        return self._dao.find_by_id(loading_id)

    def update(self, loading_id: int, loading: MoneyLoading) -> None:
        self._dao.update(loading_id, loading)

    def delete(self, loading_id: int) -> None:
        self._dao.delete(loading_id)
