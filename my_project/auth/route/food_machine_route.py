from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response
from my_project.auth.controller.food_machine_controller import FoodMachineController
from my_project.auth.domain.orders.FoodMachines import FoodMachine

food_machine_bp = Blueprint('food_machine', __name__, url_prefix='/food_machine')
controller = FoodMachineController()

@food_machine_bp.route('/all', methods=['GET'])
def get_all_food_machines():
    machines = controller.find_all()
    dto = [machine.put_into_dto() for machine in machines]
    return make_response(jsonify(dto), HTTPStatus.OK)

@food_machine_bp.route('/<int:id>', methods=['GET'])
def get_food_machine_by_id(id: int):
    machine = controller.find_by_id(id)
    if machine:
        return make_response(jsonify(machine.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Food Machine not found"}), HTTPStatus.NOT_FOUND)

@food_machine_bp.route('', methods=['POST'])
def create_food_machine():
    content = request.get_json()
    machine = FoodMachine.create_from_dto(content)
    controller.create(machine)
    return make_response(jsonify(machine.put_into_dto()), HTTPStatus.CREATED)

@food_machine_bp.route('/<int:id>', methods=['PUT'])
def update_food_machine(id: int):
    content = request.get_json()
    machine = FoodMachine.create_from_dto(content)
    controller.update(id, machine)
    return make_response(jsonify({"message": "Updated successfully"}), HTTPStatus.OK)

@food_machine_bp.route('/<int:id>', methods=['DELETE'])
def delete_food_machine(id: int):
    controller.delete(id)
    return make_response(jsonify({"message": "Deleted successfully"}), HTTPStatus.OK)
