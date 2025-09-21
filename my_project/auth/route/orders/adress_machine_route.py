from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import AddressMachineController
from my_project.auth.domain import AddressMachine

address_machine_bp = Blueprint('address_machine', __name__, url_prefix='/address_machine')
controller = AddressMachineController()


@address_machine_bp.get('')
def get_all_address_machines() -> Response:
    """
    Отримати список всіх адрес автоматів
    ---
    tags:
      - AddressMachine
    summary: List all address machines
    responses:
      200:
        description: Список адрес
        schema:
          type: array
          items:
            type: object
            additionalProperties: true
        examples:
          application/json:
            - id: 1
              address: "Kyiv, Khreshchatyk 1"
              machine_id: 10
            - id: 2
              address: "Lviv, Svobody Ave 5"
              machine_id: 11
    """
    addresses = controller.find_all()
    dto = [a.put_into_dto() for a in addresses]
    return make_response(jsonify(dto), HTTPStatus.OK)


@address_machine_bp.post('')
def create_address_machine() -> Response:
    """
    Створити нову адресу автомата
    ---
    tags:
      - AddressMachine
    summary: Create address machine
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        description: Дані адреси автомата (DTO)
        schema:
          type: object
          additionalProperties: true
        examples:
          application/json:
            address: "Kyiv, Khreshchatyk 1"
            machine_id: 10
    responses:
      201:
        description: Створено
        schema:
          type: object
          additionalProperties: true
        examples:
          application/json:
            id: 3
            address: "Kyiv, Khreshchatyk 1"
            machine_id: 10
      400:
        description: Невірні дані
    """
    content = request.get_json()
    address = AddressMachine.create_from_dto(content)
    controller.create(address)
    return make_response(jsonify(address.put_into_dto()), HTTPStatus.CREATED)


@address_machine_bp.get('/<int:id>')
def get_address_machine(id: int) -> Response:
    """
    Отримати адресу автомата за ID
    ---
    tags:
      - AddressMachine
    summary: Get address machine by ID
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: Ідентифікатор адреси
    responses:
      200:
        description: Знайдена адреса
        schema:
          type: object
          additionalProperties: true
        examples:
          application/json:
            id: 1
            address: "Kyiv, Khreshchatyk 1"
            machine_id: 10
      404:
        description: Address Machine not found
        examples:
          application/json:
            error: "Address Machine not found"
    """
    address = controller.find_by_id(id)
    if address:
        return make_response(jsonify(address.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Address Machine not found"}), HTTPStatus.NOT_FOUND)


@address_machine_bp.put('/<int:id>')
def update_address_machine(id: int) -> Response:
    """
    Оновити адресу автомата за ID
    ---
    tags:
      - AddressMachine
    summary: Update address machine by ID
    consumes:
      - application/json
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: Ідентифікатор адреси
      - in: body
        name: body
        required: true
        description: Нові дані адреси (DTO)
        schema:
          type: object
          additionalProperties: true
        examples:
          application/json:
            address: "Lviv, Svobody Ave 5"
            machine_id: 11
    responses:
      200:
        description: Оновлено
        examples:
          text/plain: "Address Machine updated"
      404:
        description: Address Machine not found
    """
    content = request.get_json()
    address = AddressMachine.create_from_dto(content)
    controller.update(id, address)
    return make_response("Address Machine updated", HTTPStatus.OK)


@address_machine_bp.delete('/<int:id>')
def delete_address_machine(id: int) -> Response:
    """
    Видалити адресу автомата за ID
    ---
    tags:
      - AddressMachine
    summary: Delete address machine by ID
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: Ідентифікатор адреси
    responses:
      204:
        description: Видалено (без тіла відповіді)
      404:
        description: Address Machine not found
    """
    controller.delete(id)
    return make_response("Address Machine deleted", HTTPStatus.NO_CONTENT)
