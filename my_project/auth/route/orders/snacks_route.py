from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response
from my_project.auth.controller import SnacksController
from my_project.auth.domain import Snacks

snacks_bp = Blueprint('snacks', __name__, url_prefix='/snacks')
controller = SnacksController()

@snacks_bp.route('/all', methods=['GET'])
def get_all_snacks():
    """
    Отримати всі снеки.
    """
    snacks = controller.find_all()
    dto = [snack.put_into_dto() for snack in snacks]
    return make_response(jsonify(dto), HTTPStatus.OK)

@snacks_bp.route('', methods=['POST'])
def create_snack():
    """
    Створити новий запис для снеків.
    """
    content = request.get_json()
    snack = Snacks.create_from_dto(content)
    controller.create(snack)
    return make_response(jsonify(snack.put_into_dto()), HTTPStatus.CREATED)

@snacks_bp.route('/<int:id>', methods=['GET'])
def get_snack_by_id(id: int):
    """
    Знайти снеки за ID.
    """
    snack = controller.find_by_id(id)
    if snack:
        return make_response(jsonify(snack.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Snack not found"}), HTTPStatus.NOT_FOUND)

@snacks_bp.route('/<int:id>', methods=['PUT'])
def update_snack(id: int):
    content = request.get_json()
    snack = Snacks.create_from_dto(content)
    controller.update(id, snack)
    return make_response(jsonify({"message": "Updated successfully"}), HTTPStatus.OK)

@snacks_bp.route('/<int:id>', methods=['DELETE'])
def delete_snack(id: int):
    """
    Видалити снеки за ID.
    """
    controller.delete(id)
    return make_response(jsonify({"message": "Snack deleted successfully"}), HTTPStatus.OK)
