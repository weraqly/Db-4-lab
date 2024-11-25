# machine_manifecture_routes.py
from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.machine_manifecture_controller import MachineManifectureController
from my_project.auth.domain.orders.MachineManifecture import MachineManifecture

machine_manifecture_bp = Blueprint('machine_manifecture', __name__, url_prefix='/machine_manifecture')
controller = MachineManifectureController()

@machine_manifecture_bp.get('')
def get_all_machine_manifectures() -> Response:
    manifectures = controller.find_all()
    dto = [m.put_into_dto() for m in manifectures]
    return make_response(jsonify(dto), HTTPStatus.OK)

@machine_manifecture_bp.post('')
def create_machine_manifecture() -> Response:
    content = request.get_json()
    manifecture = MachineManifecture.create_from_dto(content)
    controller.create(manifecture)
    return make_response(jsonify(manifecture.put_into_dto()), HTTPStatus.CREATED)

@machine_manifecture_bp.get('/<int:id>')
def get_machine_manifecture(id: int) -> Response:
    manifecture = controller.find_by_id(id)
    if manifecture:
        return make_response(jsonify(manifecture.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Machine Manifecture not found"}), HTTPStatus.NOT_FOUND)

@machine_manifecture_bp.put('/<int:id>')
def update_machine_manifecture(id: int) -> Response:
    content = request.get_json()
    manifecture = MachineManifecture.create_from_dto(content)
    controller.update(id, manifecture)
    return make_response("Machine Manifecture updated", HTTPStatus.OK)

@machine_manifecture_bp.delete('/<int:id>')
def delete_machine_manifecture(id: int) -> Response:
    controller.delete(id)
    return make_response("Machine Manifecture deleted", HTTPStatus.NO_CONTENT)
