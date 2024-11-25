# employess_address_routes.py
from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.employees_address_controller import EmployessAddressController
from my_project.auth.domain.orders.EmployessAddress import EmployessAddress

employess_address_bp = Blueprint('employess_address', __name__, url_prefix='/employess_address')
controller = EmployessAddressController()

@employess_address_bp.get('')
def get_all_employess_addresses() -> Response:
    addresses = controller.find_all()
    dto = [ea.put_into_dto() for ea in addresses]
    return make_response(jsonify(dto), HTTPStatus.OK)

@employess_address_bp.post('')
def create_employess_address() -> Response:
    content = request.get_json()
    address = EmployessAddress.create_from_dto(content)
    controller.create(address)
    return make_response(jsonify(address.put_into_dto()), HTTPStatus.CREATED)

@employess_address_bp.get('/<int:id>')
def get_employess_address(id: int) -> Response:
    address = controller.find_by_id(id)
    if address:
        return make_response(jsonify(address.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Employess Address not found"}), HTTPStatus.NOT_FOUND)

@employess_address_bp.put('/<int:id>')
def update_employess_address(id: int) -> Response:
    content = request.get_json()
    address = EmployessAddress.create_from_dto(content)
    controller.update(id, address)
    return make_response("Employess Address updated", HTTPStatus.OK)

@employess_address_bp.delete('/<int:id>')
def delete_employess_address(id: int) -> Response:
    controller.delete(id)
    return make_response("Employess Address deleted", HTTPStatus.NO_CONTENT)
