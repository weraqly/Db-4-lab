# MoneyLoadingService.py
from typing import List
from my_project.auth.dao.orders import money_loading_dao
from my_project.auth.service.orders.general_service import GeneralService
from my_project.auth.domain import MoneyLoading

class MoneyLoadingService(GeneralService):
    _dao = money_loading_dao

    def create(self, loading: MoneyLoading) -> None:
        self._dao.create(loading)

    def update(self, loading_id: int, loading: MoneyLoading) -> None:
        self._dao.update(loading_id, loading)

    def get_all_money_loadings(self) -> List[MoneyLoading]:
        return self._dao.find_all()

    def get_money_loading_by_id(self, loading_id: int) -> MoneyLoading:
        return self._dao.find_by_id(loading_id)

