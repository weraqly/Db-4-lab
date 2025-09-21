
from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import AddressMachineController
from my_project.auth.domain import AddressMachine

address_machine_bp = Blueprint('address_machine', __name__, url_prefix='/address_machine')
controller = AddressMachineController()

@address_machine_bp.get('')
def get_all_address_machines() -> Response:
    addresses = controller.find_all()
    dto = [a.put_into_dto() for a in addresses]
    return make_response(jsonify(dto), HTTPStatus.OK)

@address_machine_bp.post('')
def create_address_machine() -> Response:
    content = request.get_json()
    address = AddressMachine.create_from_dto(content)
    controller.create(address)
    return make_response(jsonify(address.put_into_dto()), HTTPStatus.CREATED)

@address_machine_bp.get('/<int:id>')
def get_address_machine(id: int) -> Response:
    address = controller.find_by_id(id)
    if address:
        return make_response(jsonify(address.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Address Machine not found"}), HTTPStatus.NOT_FOUND)

@address_machine_bp.put('/<int:id>')
def update_address_machine(id: int) -> Response:
    content = request.get_json()
    address = AddressMachine.create_from_dto(content)
    controller.update(id, address)
    return make_response("Address Machine updated", HTTPStatus.OK)

@address_machine_bp.delete('/<int:id>')
def delete_address_machine(id: int) -> Response:
    controller.delete(id)
    return make_response("Address Machine deleted", HTTPStatus.NO_CONTENT)
