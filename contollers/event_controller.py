from flask import Blueprint, request, Response, json
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.event_service import create_event, fetch_one_event, edit_event, delete_event,fetch_events
from datetime import datetime, date

event_blueprint = Blueprint('event_api', __name__)

@event_blueprint.route('/new', methods=['POST'])
@jwt_required
def new_event():
    data = request.json

    return create_event(data)

@event_blueprint.route('/<int:event_id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required
def single_event(event_id):
    if request.method == 'GET':
        event = fetch_one_event(event_id)
        if event:
            return custom_response(event, 200)

    elif request.method == 'PUT':
        data = request.json
        # user = 1
        user = get_jwt_identity()
        event = fetch_one_event(event_id)
        if user == event['client_id']:
            return custom_response(edit_event(event_id, data), 200)

    elif request.method == 'DELETE':
        # user = 1
        user = get_jwt_identity()
        event = fetch_one_event(event_id)
        if user == event['client_id']:
            return custom_response(delete_event(event), 200)
    else:
        return 'Method not allowed', 405


@event_blueprint.route('/all', methods=['POST'])
@jwt_required
def all_event():
    x = fetch_events()
    return custom_response(x, 200)


def custom_response(res, status_code):
    return Response(
        mimetype='application/json',
        response=json.dumps(res),
        status=status_code
    )  