import json

from flask_jwt_extended import jwt_refresh_token_required, jwt_required

from . import user
from .user import CustomUserEntity
from ..utils.response_builder import ResponseBuilder
from flask import request


@user.route('/register/', methods=['POST'])
def register():
    response_builder = ResponseBuilder()
    post_data = json.loads(request.data)
    username = post_data.get('username', None)
    password = post_data.get('password', None)
    role_id = post_data.get('role_id', None)
    if not (username and password and role_id):
        return response_builder.bad_request_400().get_response()

    status, message, user_entity = CustomUserEntity.create(username=username, password=password, role=role_id)
    if status == 0:
        return response_builder.success().get_response()

    result = user_entity.get_serialized()
    tokens = user_entity.create_token()
    result.update(tokens)
    return response_builder.created().result_object(result).get_response()


@user.route('/login/', methods=['POST'])
def login():
    response_builder = ResponseBuilder()
    post_data = json.loads(request.data)
    username = post_data.get('username', None)
    password = post_data.get('password', None)
    if not (username and password):
        return response_builder.bad_request_400().get_response()

    result = dict(message='User does not exists')
    user_entity = CustomUserEntity.get_by_username(username)
    if not user_entity:
        return response_builder.success().result_object(result).get_response()

    if user_entity.verify_password(password) == 0:
        result['message'] = 'Invalid credentials. Please try again'
        return response_builder.unauthorized().result_object(result).get_response()

    result['message'] = 'User logged in'
    result.update(user_entity.create_token())
    return response_builder.success().result_object(result).get_response()


@user.route('/update/', methods=['POST'])
def update():
    response_builder = ResponseBuilder()
    post_data = json.loads(request.data)
    old_username = post_data.get('old_username', None)
    new_username = post_data.get('new_username', None)

    result = {
        'message': 'Only admins can update username'
    }
    access_token = CustomUserEntity.get_header_token(request.headers)
    if CustomUserEntity.is_user_admin(access_token) == 0:
        return response_builder.unauthorized().result_object(result).get_response()

    user_entity = CustomUserEntity.get_by_username(old_username)
    if not user_entity:
        result['message'] = 'User does not exists with this username'
        return response_builder.success().result_object(result).get_response()

    status, message = user_entity.update(new_username)
    if status == 0:
        return response_builder.success().result_object(result).get_response()

    result['message'] = 'User updated successfully'
    result.update(user_entity.get_serialized())
    return response_builder.success().result_object(result).get_response()


@user.route('/token/refresh/', methods=['POST'])
@jwt_refresh_token_required
def refresh_token():
    token = CustomUserEntity.get_header_token(request.headers)
    result = CustomUserEntity.refresh_token(token)
    result['message'] = 'Token refreshed'
    return ResponseBuilder().success().result_object(result).get_response()
