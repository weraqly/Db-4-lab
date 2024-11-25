# ServiceService.py
from typing import List
from my_project.auth.dao import service_dao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.Services import Services

class ServiceService(GeneralService):
    _dao = service_dao

    def create(self, service: Services) -> None:
        self._dao.create(service)

    def update(self, service_id: int, service: Services) -> None:
        self._dao.update(service_id, service)

    def get_all_services(self) -> List[Services]:
        return self._dao.find_all()

    def get_service_by_id(self, service_id: int) -> Services:
        return self._dao.find_by_id(service_id)