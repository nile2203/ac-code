import json
from flask import request

from . import employee
from .employee import EmployeeEntity
from ..utils.response_builder import ResponseBuilder


@employee.route('/create/', methods=['POST'])
def create():
    response = ResponseBuilder()
    post_data = json.loads(request.data)
    email = post_data.get('email', None)
    first_name = post_data.get('first_name', None)
    last_name = post_data.get('last_name', None)
    department_id = post_data.get('id', None)
    if not (email and first_name and department_id):
        return response.bad_request_400().get_response()

    status, message, result = EmployeeEntity.create(
        email=email, first_name=first_name, last_name=last_name, department_id=department_id)
    if status == 0:
        return response.success().get_response()

    return response.created().result_object(result).get_response()


@employee.route('/get/<id>', methods=['GET'])
def get(id):
    response = ResponseBuilder()
    if not id:
        return response.bad_request_400().get_response()

    employee_entity = EmployeeEntity.get_by_id(employee_id=id)
    if not employee_entity:
        return response.not_found_404().get_response()

    result = employee_entity.get_serialized()
    return response.success().result_object(result).get_response()


@employee.route('/update/', methods=['POST'])
def update():
    response = ResponseBuilder()
    post_data = json.loads(request.data)
    first_name = post_data.get('first_name', None)
    last_name = post_data.get('last_name', None)
    employee_id = post_data.get('id', None)
    department_id = post_data.get('department_id', None)
    if not employee_id:
        return response.bad_request_400().get_response()

    employee_entity = EmployeeEntity.get_by_id(employee_id=employee_id)
    if not employee_entity:
        return response.not_found_404().get_response()

    status, message, result = employee_entity.update(
        first_name=first_name, last_name=last_name, department=department_id)
    if status == 0:
        return response.success().get_response()

    return response.updated().result_object(result).get_response()


@employee.route('/delete/', methods=['POST'])
def delete():
    response = ResponseBuilder()
    post_data = json.loads(request.data)
    employee_id = post_data.get('id', None)
    if not employee_id:
        return response.bad_request_400().get_response()

    employee_entity = EmployeeEntity.get_by_id(employee_id=employee_id)
    if not employee_entity:
        return response.not_found_404().get_response()

    status, message = employee_entity.delete()
    if status == 0:
        return response.success().get_response()

    return response.deleted().get_response()

