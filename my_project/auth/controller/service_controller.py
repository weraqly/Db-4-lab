# ServiceController.py
from typing import List
from my_project.auth.dao.service_dao import ServiceDao
from my_project.auth.domain.orders.Services import Services

class ServiceController:
    _dao = ServiceDao()

    def find_all(self) -> List[Services]:
        return self._dao.find_all()

    def create(self, service: Services) -> None:
        self._dao.create(service)

    def find_by_id(self, service_id: int) -> Services:
        return self._dao.find_by_id(service_id)

    def update(self, service_id: int, service: Services) -> None:
        self._dao.update(service_id, service)

    def delete(self, service_id: int) -> None:
        self._dao.delete(service_id)
