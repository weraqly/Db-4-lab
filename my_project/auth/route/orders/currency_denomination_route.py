# currency_denominations_routes.py
from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import CurrencyDenominationsController
from my_project.auth.domain import CurrencyDenominations

currency_denominations_bp = Blueprint('currency_denominations', __name__, url_prefix='/currency_denominations')
controller = CurrencyDenominationsController()

@currency_denominations_bp.get('')
def get_all_currency_denominations() -> Response:
    denominations = controller.find_all()
    dto = [cd.put_into_dto() for cd in denominations]
    return make_response(jsonify(dto), HTTPStatus.OK)

@currency_denominations_bp.post('')
def create_currency_denomination() -> Response:
    content = request.get_json()
    denomination = CurrencyDenominations.create_from_dto(content)
    controller.create(denomination)
    return make_response(jsonify(denomination.put_into_dto()), HTTPStatus.CREATED)

@currency_denominations_bp.get('/<int:id>')
def get_currency_denomination(id: int) -> Response:
    denomination = controller.find_by_id(id)
    if denomination:
        return make_response(jsonify(denomination.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Currency Denomination not found"}), HTTPStatus.NOT_FOUND)

@currency_denominations_bp.put('/<int:id>')
def update_currency_denomination(id: int) -> Response:
    content = request.get_json()
    denomination = CurrencyDenominations.create_from_dto(content)
    controller.update(id, denomination)
    return make_response("Currency Denomination updated", HTTPStatus.OK)

@currency_denominations_bp.delete('/<int:id>')
def delete_currency_denomination(id: int) -> Response:
    controller.delete(id)
    return make_response("Currency Denomination deleted", HTTPStatus.NO_CONTENT)
