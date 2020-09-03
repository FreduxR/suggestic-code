from flask import Blueprint, request, jsonify, make_response

process_blueprint = Blueprint(__name__, 'process')

from app.bin.process.model import Process

from app import app

process_dao = Process(app)


@process_blueprint.route('/nested_list', methods=['POST'])
@app.exception_handler
def nested_list():
    body = request.get_json(silent=True)

    if 'items' in body:
        result_list = []
        process_dao.process_nested_list(body['items'], result_list)
        return make_response(jsonify({'result': result_list}), 200)
    else:
        app.log.error('Body dont have items')
        return make_response(jsonify({'error': 'Body dont have items'}), 500)
