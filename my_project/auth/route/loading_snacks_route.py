from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response
from my_project.auth.controller.loading_snacks_controller import LoadingSnacksController
from my_project.auth.domain.orders.LoadingSnacks import LoadingSnacks

loading_snacks_bp = Blueprint('loading_snacks', __name__, url_prefix='/loading_snacks')
controller = LoadingSnacksController()

@loading_snacks_bp.route('/all', methods=['GET'])
def get_all_loading_snacks():
    loading_snacks = controller.find_all()
    dto = [ls.put_into_dto() for ls in loading_snacks]
    return make_response(jsonify(dto), HTTPStatus.OK)

@loading_snacks_bp.route('/<int:loading_machine_id>/<int:snack_id>', methods=['GET'])
def get_loading_snack_by_ids(loading_machine_id: int, snack_id: int):
    loading_snack = controller.find_by_ids(loading_machine_id, snack_id)
    if loading_snack:
        return make_response(jsonify(loading_snack.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Loading Snack not found"}), HTTPStatus.NOT_FOUND)

@loading_snacks_bp.route('', methods=['POST'])
def create_loading_snacks():
    content = request.get_json()
    loading_snack = LoadingSnacks.create_from_dto(content)
    controller.create(loading_snack)
    return make_response(jsonify(loading_snack.put_into_dto()), HTTPStatus.CREATED)

@loading_snacks_bp.route('/<int:loading_machine_id>/<int:snack_id>', methods=['DELETE'])
def delete_loading_snacks(loading_machine_id: int, snack_id: int):
    controller.delete(loading_machine_id, snack_id)
    return make_response(jsonify({"message": "Deleted successfully"}), HTTPStatus.OK)
