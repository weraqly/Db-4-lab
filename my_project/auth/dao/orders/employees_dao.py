from typing import List
from my_project import db
from my_project.auth.domain import Employees

class EmployeesDao:
    @staticmethod
    def create(employee: Employees) -> None:
        db.session.add(employee)
        db.session.commit()

    @staticmethod
    def update(employee_id: int, employee: Employees) -> None:
        db.session.query(Employees).filter_by(id=employee_id).update({
            "first_name": employee.first_name,
            "last_name": employee.last_name,
            "phone_number": employee.phone_number,
            "experience": employee.experience,
            "email": employee.email,
            "employess_address_id": employee.employess_address_id,
        })
        db.session.commit()

    @staticmethod
    def find_all() -> List[Employees]:
        return db.session.query(Employees).all()

    @staticmethod
    def find_by_id(employee_id: int) -> Employees:
        return db.session.query(Employees).filter_by(id=employee_id).first()