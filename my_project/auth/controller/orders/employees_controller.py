# EmployeesController.py
from typing import List
from my_project.auth.dao import EmployeesDao
from my_project.auth.domain import Employees

class EmployeesController:
    _dao = EmployeesDao()

    def find_all(self) -> List[Employees]:
        return self._dao.find_all()

    def create(self, employee: Employees) -> None:
        self._dao.create(employee)

    def find_by_id(self, employee_id: int) -> Employees:
        return self._dao.find_by_id(employee_id)

    def update(self, employee_id: int, employee: Employees) -> None:
        self._dao.update(employee_id, employee)

    def delete(self, employee_id: int) -> None:
        self._dao.delete(employee_id)
