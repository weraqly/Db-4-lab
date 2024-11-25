# snacks_creator_routes.py
from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.snacks_creator_controller import SnacksCreatorController
from my_project.auth.domain.orders.SnacksCreator import SnacksCreator

snacks_creator_bp = Blueprint('snacks_creator', __name__, url_prefix='/snacks_creator')
controller = SnacksCreatorController()

@snacks_creator_bp.get('')
def get_all_snacks_creators() -> Response:
    creators = controller.find_all()
    dto = [sc.put_into_dto() for sc in creators]
    return make_response(jsonify(dto), HTTPStatus.OK)

@snacks_creator_bp.post('')
def create_snacks_creator() -> Response:
    content = request.get_json()
    creator = SnacksCreator.create_from_dto(content)
    controller.create(creator)
    return make_response(jsonify(creator.put_into_dto()), HTTPStatus.CREATED)

@snacks_creator_bp.get('/<int:id>')
def get_snacks_creator(id: int) -> Response:
    creator = controller.find_by_id(id)
    if creator:
        return make_response(jsonify(creator.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Snacks Creator not found"}), HTTPStatus.NOT_FOUND)

@snacks_creator_bp.put('/<int:id>')
def update_snacks_creator(id: int) -> Response:
    content = request.get_json()
    creator = SnacksCreator.create_from_dto(content)
    controller.update(id, creator)
    return make_response("Snacks Creator updated", HTTPStatus.OK)

@snacks_creator_bp.delete('/<int:id>')
def delete_snacks_creator(id: int) -> Response:
    controller.delete(id)
    return make_response("Snacks Creator deleted", HTTPStatus.NO_CONTENT)
