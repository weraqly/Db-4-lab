# money_transfer_routes.py
from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.money_transfer_controller import MoneyTransferController
from my_project.auth.domain.orders.MoneyTransfer import MoneyTransfer

money_transfer_bp = Blueprint('money_transfer', __name__, url_prefix='/money_transfer')
controller = MoneyTransferController()

@money_transfer_bp.get('')
def get_all_money_transfers() -> Response:
    transfers = controller.find_all()
    dto = [mt.put_into_dto() for mt in transfers]
    return make_response(jsonify(dto), HTTPStatus.OK)

@money_transfer_bp.post('')
def create_money_transfer() -> Response:
    content = request.get_json()
    transfer = MoneyTransfer.create_from_dto(content)
    controller.create(transfer)
    return make_response(jsonify(transfer.put_into_dto()), HTTPStatus.CREATED)

@money_transfer_bp.get('/<int:id>')
def get_money_transfer(id: int) -> Response:
    transfer = controller.find_by_id(id)
    if transfer:
        return make_response(jsonify(transfer.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Money Transfer not found"}), HTTPStatus.NOT_FOUND)

@money_transfer_bp.put('/<int:id>')
def update_money_transfer(id: int) -> Response:
    content = request.get_json()
    transfer = MoneyTransfer.create_from_dto(content)
    controller.update(id, transfer)
    return make_response("Money Transfer updated", HTTPStatus.OK)

@money_transfer_bp.delete('/<int:id>')
def delete_money_transfer(id: int) -> Response:
    controller.delete(id)
    return make_response("Money Transfer deleted", HTTPStatus.NO_CONTENT)
