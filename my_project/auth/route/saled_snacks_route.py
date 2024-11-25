# saled_snacks_routes.py
from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.saled_snacks_controller import SaledSnacksController
from my_project.auth.domain.orders.SaledSnacks import SaledSnacks

saled_snacks_bp = Blueprint('saled_snacks', __name__, url_prefix='/saled_snacks')
controller = SaledSnacksController()

@saled_snacks_bp.get('')
def get_all_saled_snacks() -> Response:
    snacks = controller.find_all()
    dto = [ss.put_into_dto() for ss in snacks]
    return make_response(jsonify(dto), HTTPStatus.OK)

@saled_snacks_bp.post('')
def create_saled_snack() -> Response:
    content = request.get_json()
    snack = SaledSnacks.create_from_dto(content)
    controller.create(snack)
    return make_response(jsonify(snack.put_into_dto()), HTTPStatus.CREATED)

@saled_snacks_bp.get('/<int:id>')
def get_saled_snack(id: int) -> Response:
    snack = controller.find_by_id(id)
    if snack:
        return make_response(jsonify(snack.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Saled Snack not found"}), HTTPStatus.NOT_FOUND)

@saled_snacks_bp.put('/<int:id>')
def update_saled_snack(id: int) -> Response:
    content = request.get_json()
    snack = SaledSnacks.create_from_dto(content)
    controller.update(id, snack)
    return make_response("Saled Snack updated", HTTPStatus.OK)

@saled_snacks_bp.delete('/<int:id>')
def delete_saled_snack(id: int) -> Response:
    controller.delete(id)
    return make_response("Saled Snack deleted", HTTPStatus.NO_CONTENT)
