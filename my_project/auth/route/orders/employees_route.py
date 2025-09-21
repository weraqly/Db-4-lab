# employees_routes.py
from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import EmployeesController
from my_project.auth.domain import Employees

employees_bp = Blueprint('employees', __name__, url_prefix='/employees')
controller = EmployeesController()

@employees_bp.get('')
def get_all_employees() -> Response:
    employees = controller.find_all()
    dto = [e.put_into_dto() for e in employees]
    return make_response(jsonify(dto), HTTPStatus.OK)

@employees_bp.post('')
def create_employee() -> Response:
    content = request.get_json()
    employee = Employees.create_from_dto(content)
    controller.create(employee)
    return make_response(jsonify(employee.put_into_dto()), HTTPStatus.CREATED)

@employees_bp.get('/<int:id>')
def get_employee(id: int) -> Response:
    employee = controller.find_by_id(id)
    if employee:
        return make_response(jsonify(employee.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Employee not found"}), HTTPStatus.NOT_FOUND)

@employees_bp.put('/<int:id>')
def update_employee(id: int) -> Response:
    content = request.get_json()
    employee = Employees.create_from_dto(content)
    controller.update(id, employee)
    return make_response("Employee updated", HTTPStatus.OK)

@employees_bp.delete('/<int:id>')
def delete_employee(id: int) -> Response:
    controller.delete(id)
    return make_response("Employee deleted", HTTPStatus.NO_CONTENT)
