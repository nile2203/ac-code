import json
from flask import request

from . import department
from .department import DepartmentEntity
from ..utils.response_builder import ResponseBuilder


@department.route('/create/', methods=['POST'])
def create():
    response = ResponseBuilder()
    post_data = json.loads(request.data)
    name = post_data.get('name', None)
    if not name:
        return response.bad_request_400().get_response()

    status, message, result = DepartmentEntity.create(name=name)
    if status == 0:
        return response.success().get_response()

    return response.created().result_object(result).get_response()


@department.route('/get/<id>', methods=['GET'])
def get(id):
    response = ResponseBuilder()
    if not id:
        return response.bad_request_400().get_response()

    department_entity = DepartmentEntity.get_by_id(department_id=id)
    if not department_entity:
        return response.not_found_404().get_response()

    result = department_entity.get_serialized()
    return response.success().result_object(result).get_response()


@department.route('/update/', methods=['POST'])
def update():
    response = ResponseBuilder()
    post_data = json.loads(request.data)
    name = post_data.get('name', None)
    id = post_data.get('id', None)
    employee_id = post_data.get('employee_id', None)
    if not id:
        return response.bad_request_400().get_response()

    department_entity = DepartmentEntity.get_by_id(department_id=id)
    if not department_entity:
        return response.not_found_404().get_response()

    status, message, result = department_entity.update(name, employee_id)
    if status == 0:
        return response.success().get_response()

    return response.updated().result_object(result).get_response()


@department.route('/delete/', methods=['POST'])
def delete():
    response = ResponseBuilder()
    post_data = json.loads(request.data)
    department_id = post_data.get('id', None)
    if not department_id:
        return response.bad_request_400().get_response()

    department_entity = DepartmentEntity.get_by_id(department_id=department_id)
    if not department_entity:
        return response.not_found_404().get_response()

    status, message = department_entity.delete()
    if status == 0:
        return response.success().get_response()

    return response.deleted().get_response()

