# menu_routes.py
from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import MenuController
from my_project.auth.domain import Menu

menu_bp = Blueprint('menu', __name__, url_prefix='/menu')
controller = MenuController()

@menu_bp.get('')
def get_all_menus() -> Response:
    menus = controller.find_all()
    dto = [m.put_into_dto() for m in menus]
    return make_response(jsonify(dto), HTTPStatus.OK)

@menu_bp.post('')
def create_menu() -> Response:
    content = request.get_json()
    menu = Menu.create_from_dto(content)
    controller.create(menu)
    return make_response(jsonify(menu.put_into_dto()), HTTPStatus.CREATED)

@menu_bp.get('/<int:id>')
def get_menu(id: int) -> Response:
    menu = controller.find_by_id(id)
    if menu:
        return make_response(jsonify(menu.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Menu not found"}), HTTPStatus.NOT_FOUND)

@menu_bp.put('/<int:id>')
def update_menu(id: int) -> Response:
    content = request.get_json()
    menu = Menu.create_from_dto(content)
    controller.update(id, menu)
    return make_response("Menu updated", HTTPStatus.OK)

@menu_bp.delete('/<int:id>')
def delete_menu(id: int) -> Response:
    controller.delete(id)
    return make_response("Menu deleted", HTTPStatus.NO_CONTENT)
