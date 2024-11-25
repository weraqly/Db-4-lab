# money_loading_routes.py
from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.money_loading_controller import MoneyLoadingController
from my_project.auth.domain.orders.MoneyLoading import MoneyLoading

money_loading_bp = Blueprint('money_loading', __name__, url_prefix='/money_loading')
controller = MoneyLoadingController()

@money_loading_bp.get('')
def get_all_money_loadings() -> Response:
    loadings = controller.find_all()
    dto = [ml.put_into_dto() for ml in loadings]
    return make_response(jsonify(dto), HTTPStatus.OK)

@money_loading_bp.post('')
def create_money_loading() -> Response:
    content = request.get_json()
    loading = MoneyLoading.create_from_dto(content)
    controller.create(loading)
    return make_response(jsonify(loading.put_into_dto()), HTTPStatus.CREATED)

@money_loading_bp.get('/<int:id>')
def get_money_loading(id: int) -> Response:
    loading = controller.find_by_id(id)
    if loading:
        return make_response(jsonify(loading.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Money Loading not found"}), HTTPStatus.NOT_FOUND)

@money_loading_bp.put('/<int:id>')
def update_money_loading(id: int) -> Response:
    content = request.get_json()
    loading = MoneyLoading.create_from_dto(content)
    controller.update(id, loading)
    return make_response("Money Loading updated", HTTPStatus.OK)

@money_loading_bp.delete('/<int:id>')
def delete_money_loading(id: int) -> Response:
    controller.delete(id)
    return make_response("Money Loading deleted", HTTPStatus.NO_CONTENT)
