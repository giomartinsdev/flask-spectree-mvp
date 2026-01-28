from flask import Blueprint, request, jsonify
from spectree import Response
from src.infrastructure.dependency_container import container
from src.infrastructure.spec.spec_tree import api
from src.presentation.dtos.user_dto import (
    UserCreateRequest, 
    UserUpdateRequest, 
    UserResponse, 
    UserListResponse,
    ErrorResponse
)

user_bp = Blueprint('users', __name__, url_prefix='/api/users')

def get_user_service():
    return container.get('user_service')
 
 
@user_bp.route('', methods=['POST'])
@api.validate(
    json=UserCreateRequest,
    resp=Response(HTTP_201=UserResponse, HTTP_400=ErrorResponse),
    tags=['Users']
)
def create_user(json: UserCreateRequest):
    user_service = get_user_service()
    user = user_service.create_user(
        name=json.name,
        email=json.email
    )
    return UserResponse.model_validate(user.__dict__).__dict__, 201
 
 
@user_bp.route('', methods=['GET'])
@api.validate(
    resp=Response(HTTP_200=UserListResponse),
    tags=['Users']
)
def get_users():
    user_service = get_user_service()
    users = user_service.get_all_users()
    user_responses = [UserResponse.model_validate(user.__dict__).__dict__ for user in users]
    return UserListResponse(users=user_responses, total=len(users)).model_dump(), 200
 
 
@user_bp.route('/<int:user_id>', methods=['GET'])
@api.validate(
    resp=Response(HTTP_200=UserResponse, HTTP_404=ErrorResponse),
    tags=['Users']
)
def get_user(user_id):
    user_service = get_user_service()
    user = user_service.get_user(user_id)
    return UserResponse.model_validate(user.__dict__).__dict__, 200
 
 
@user_bp.route('/<int:user_id>', methods=['PUT'])
@api.validate(
    json=UserUpdateRequest,
    resp=Response(HTTP_200=UserResponse, HTTP_400=ErrorResponse, HTTP_404=ErrorResponse),
    tags=['Users']
)
def update_user(user_id, json: UserUpdateRequest):
    user_service = get_user_service()
    user = user_service.update_user(
        user_id=user_id,
        name=json.name,
        email=json.email
    )
    return UserResponse.model_validate(user.__dict__).__dict__, 200
 
 
@user_bp.route('/<int:user_id>', methods=['DELETE'])
@api.validate(
    resp=Response(HTTP_204=None, HTTP_404=ErrorResponse),
    tags=['Users']
)
def delete_user(user_id):
    user_service = get_user_service()
    user_service.delete_user(user_id)
    return '', 204
