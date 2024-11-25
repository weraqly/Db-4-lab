# service_routes.py
from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.service_controller import ServiceController
from my_project.auth.domain.orders.Services import Services

service_bp = Blueprint('service', __name__, url_prefix='/service')
controller = ServiceController()

@service_bp.get('')
def get_all_services() -> Response:
    services = controller.find_all()
    dto = [s.put_into_dto() for s in services]
    return make_response(jsonify(dto), HTTPStatus.OK)

@service_bp.post('')
def create_service() -> Response:
    content = request.get_json()
    service = Services.create_from_dto(content)
    controller.create(service)
    return make_response(jsonify(service.put_into_dto()), HTTPStatus.CREATED)

@service_bp.get('/<int:id>')
def get_service(id: int) -> Response:
    service = controller.find_by_id(id)
    if service:
        return make_response(jsonify(service.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Service not found"}), HTTPStatus.NOT_FOUND)

@service_bp.put('/<int:id>')
def update_service(id: int) -> Response:
    content = request.get_json()
    service = Services.create_from_dto(content)
    controller.update(id, service)
    return make_response("Service updated", HTTPStatus.OK)

@service_bp.delete('/<int:id>')
def delete_service(id: int) -> Response:
    controller.delete(id)
    return make_response("Service deleted", HTTPStatus.NO_CONTENT)
