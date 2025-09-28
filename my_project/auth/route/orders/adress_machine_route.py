# my_project/auth/routes/address_machine.py
from __future__ import annotations

from http import HTTPStatus
from typing import Any, Dict, List, Optional

from flask import Blueprint, jsonify, Response, request, make_response, url_for

from my_project.auth.controller import AddressMachineController
from my_project.auth.domain import AddressMachine

address_machine_bp = Blueprint("address_machine", __name__, url_prefix="/address_machine")
controller = AddressMachineController()


@address_machine_bp.get("")
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
            properties:
              id:            { type: integer, example: 1 }
              city:          { type: string,  example: "Kyiv" }
              street:        { type: string,  example: "Khreshchatyk" }
              street_number: { type: integer, example: 1 }
              district:      { type: string,  example: "Shevchenkivskyi" }
              city_index:    { type: integer, example: 1001 }
              country:       { type: string,  example: "Ukraine" }
    """
    addresses: List[AddressMachine] = controller.find_all()
    dto = [a.put_into_dto() for a in addresses]
    return make_response(jsonify(dto), HTTPStatus.OK)


@address_machine_bp.post("")
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
          properties:
            city:          { type: string,  example: "Kyiv" }
            street:        { type: string,  example: "Khreshchatyk" }
            street_number: { type: integer, example: 1 }
            district:      { type: string,  example: "Shevchenkivskyi" }
            city_index:    { type: integer, example: 1001 }
            country:       { type: string,  example: "Ukraine" }
          required: [city, street, street_number, city_index, country]
    responses:
      201:
        description: Створено
        schema:
          type: object
          properties:
            id:            { type: integer, example: 3 }
            city:          { type: string }
            street:        { type: string }
            street_number: { type: integer }
            district:      { type: string }
            city_index:    { type: integer }
            country:       { type: string }
      400:
        description: Невірні дані
        schema:
          type: object
          properties:
            errors:
              type: array
              items: { type: string }
    """
    payload: Optional[Dict[str, Any]] = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return make_response(jsonify({"errors": ["Expected JSON object"]}), HTTPStatus.BAD_REQUEST)

    allowed_fields = {"city", "street", "street_number", "district", "city_index", "country"}
    required_fields = {"city", "street", "street_number", "city_index", "country"}
    errors: List[str] = []

    missing = [f for f in required_fields if f not in payload or payload.get(f) in (None, "")]
    if missing:
        errors.append(f"Missing required fields: {', '.join(missing)}")

    dto = {k: payload.get(k) for k in allowed_fields if k in payload}

    for int_field in ("street_number", "city_index"):
        if int_field in dto:
            try:
                dto[int_field] = int(dto[int_field])
            except (ValueError, TypeError):
                errors.append(f"Field '{int_field}' must be an integer")

    if "district" in dto and (dto["district"] is None or str(dto["district"]).strip() == ""):
        dto["district"] = None

    if errors:
        return make_response(jsonify({"errors": errors}), HTTPStatus.BAD_REQUEST)

    address = AddressMachine.create_from_dto(dto)
    controller.create(address)  # очікується, що присвоюється id

    body = address.put_into_dto()
    resp = make_response(jsonify(body), HTTPStatus.CREATED)
    try:
        resp.headers["Location"] = url_for("address_machine.get_address_machine", id=address.id, _external=True)
    except Exception:
        pass
    return resp


@address_machine_bp.get("/<int:id>")
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
          properties:
            id:            { type: integer }
            city:          { type: string }
            street:        { type: string }
            street_number: { type: integer }
            district:      { type: string }
            city_index:    { type: integer }
            country:       { type: string }
      404:
        description: Address Machine not found
        schema:
          type: object
          properties:
            error: { type: string, example: "Address Machine not found" }
    """
    address = controller.find_by_id(id)
    if address:
        return make_response(jsonify(address.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Address Machine not found"}), HTTPStatus.NOT_FOUND)


@address_machine_bp.put("/<int:id>")
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
          properties:
            city:          { type: string,  example: "Lviv" }
            street:        { type: string,  example: "Svobody Ave" }
            street_number: { type: integer, example: 5 }
            district:      { type: string,  example: "Halytskyi" }
            city_index:    { type: integer, example: 79000 }
            country:       { type: string,  example: "Ukraine" }
    responses:
      200:
        description: Оновлено
        schema:
          type: object
          properties:
            id:            { type: integer }
            city:          { type: string }
            street:        { type: string }
            street_number: { type: integer }
            district:      { type: string }
            city_index:    { type: integer }
            country:       { type: string }
      404:
        description: Address Machine not found
        schema:
          type: object
          properties:
            error: { type: string, example: "Address Machine not found" }
      400:
        description: Невірні дані
    """
    existing = controller.find_by_id(id)
    if not existing:
        return make_response(jsonify({"error": "Address Machine not found"}), HTTPStatus.NOT_FOUND)

    payload: Optional[Dict[str, Any]] = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return make_response(jsonify({"errors": ["Expected JSON object"]}), HTTPStatus.BAD_REQUEST)

    allowed_fields = {"city", "street", "street_number", "district", "city_index", "country"}
    dto = {k: payload.get(k) for k in allowed_fields if k in payload}

    errors: List[str] = []
    for int_field in ("street_number", "city_index"):
        if int_field in dto:
            try:
                dto[int_field] = int(dto[int_field])
            except (ValueError, TypeError):
                errors.append(f"Field '{int_field}' must be an integer")

    if "district" in dto and (dto["district"] is None or str(dto["district"]).strip() == ""):
        dto["district"] = None

    if errors:
        return make_response(jsonify({"errors": errors}), HTTPStatus.BAD_REQUEST)

    # Створимо об'єкт для оновлення з частковим DTO
    updated_obj = AddressMachine.create_from_dto({**existing.put_into_dto(), **dto})
    controller.update(id, updated_obj)

    # Повернемо оновлене DTO
    refreshed = controller.find_by_id(id)
    return make_response(jsonify(refreshed.put_into_dto() if refreshed else updated_obj.put_into_dto()), HTTPStatus.OK)


@address_machine_bp.delete("/<int:id>")
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
        schema:
          type: object
          properties:
            error: { type: string, example: "Address Machine not found" }
    """
    existing = controller.find_by_id(id)
    if not existing:
        return make_response(jsonify({"error": "Address Machine not found"}), HTTPStatus.NOT_FOUND)

    controller.delete(id)
    # 204 — без тіла
    return make_response(("",), HTTPStatus.NO_CONTENT)
