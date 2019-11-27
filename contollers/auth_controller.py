from flask import Blueprint, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from services import bcrypt
from services.client_service import create_client
from models.client_model import Client

auth_blueprint = Blueprint('auth_api', __name__)




@auth_blueprint.route('/login', methods=['POST'])
def login():
    body = request.json

    to_check = Client.query.filter_by(email=body['email']).first()

    if bcrypt.check_password_hash(to_check.password, body['password']):
        access_token = create_access_token(to_check.id)
        return {'message': 'Hey you logged in', 'Token:' : access_token}
    else:
        return {'message': 'Incorrect password'}
        
@auth_blueprint.route('/register', methods=['POST'])
def register():
    body = request.json

    email = body['email']
    password = bcrypt.generate_password_hash(body['password']).decode('utf-8')
    client_name = body['client_name']
    
    message = create_client(email, password, client_name)

    return {'message': message}


@auth_blueprint.route('/logout', methods=['POST'])
@jwt_required
def logout():
    return 'Logout'



