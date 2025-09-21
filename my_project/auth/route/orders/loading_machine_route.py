from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response
from my_project.auth.controller import LoadingMachineController
from my_project.auth.domain import LoadingMachine

loading_machine_bp = Blueprint('loading_machine', __name__, url_prefix='/loading_machine')
controller = LoadingMachineController()

@loading_machine_bp.route('/all', methods=['GET'])
def get_all_loading_machines():
    machines = controller.find_all()
    dto = [machine.put_into_dto() for machine in machines]
    return make_response(jsonify(dto), HTTPStatus.OK)

@loading_machine_bp.route('/<int:id>', methods=['GET'])
def get_loading_machine_by_id(id: int):
    machine = controller.find_by_id(id)
    if machine:
        return make_response(jsonify(machine.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Loading Machine not found"}), HTTPStatus.NOT_FOUND)

@loading_machine_bp.route('', methods=['POST'])
def create_loading_machine():
    content = request.get_json()
    machine = LoadingMachine.create_from_dto(content)
    controller.create(machine)
    return make_response(jsonify(machine.put_into_dto()), HTTPStatus.CREATED)

@loading_machine_bp.route('/<int:id>', methods=['PUT'])
def update_loading_machine(id: int):
    content = request.get_json()
    machine = LoadingMachine.create_from_dto(content)
    controller.update(id, machine)
    return make_response(jsonify({"message": "Updated successfully"}), HTTPStatus.OK)

@loading_machine_bp.route('/<int:id>', methods=['DELETE'])
def delete_loading_machine(id: int):
    controller.delete(id)
    return make_response(jsonify({"message": "Deleted successfully"}), HTTPStatus.OK)
