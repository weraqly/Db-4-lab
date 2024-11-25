# LoadingSnacksService.py
from typing import List
from my_project.auth.dao import loading_snacks_dao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.LoadingSnacks import LoadingSnacks

class LoadingSnacksService(GeneralService):
    _dao = loading_snacks_dao

    def create(self, loading_snacks: LoadingSnacks) -> None:
        self._dao.create(loading_snacks)

    def update(self, loading_id: int, loading_snacks: LoadingSnacks) -> None:
        self._dao.update(loading_id, loading_snacks)

    def get_all_loading_snacks(self) -> List[LoadingSnacks]:
        return self._dao.find_all()

    def get_loading_snacks_by_id(self, loading_id: int) -> LoadingSnacks:
        return self._dao.find_by_id(loading_id)