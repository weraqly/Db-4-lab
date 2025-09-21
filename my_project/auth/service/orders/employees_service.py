from typing import List
from my_project.auth.dao.orders import employees_dao
from my_project.auth.service.orders.general_service import GeneralService
from my_project.auth.domain import Employees


class EmployeesService(GeneralService):
    _dao = employees_dao

    def create(self, employee: Employees) -> None:
        self._dao.create(employee)

    def update(self, employee_id: int, employee: Employees) -> None:
        self._dao.update(employee_id, employee)

    def get_all_employees(self) -> List[Employees]:
        return self._dao.find_all()

    def get_employee_by_id(self, employee_id: int) -> Employees:
        return self._dao.find_by_id(employee_id)
