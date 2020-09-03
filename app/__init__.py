import os
import logging
from flask import Flask, jsonify, make_response

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)


def get_app_base_path():
    return os.path.dirname(os.path.realpath(__file__))


app = Flask(__name__, instance_path=get_app_base_path(), instance_relative_config=True)

app.config['JWT_SECRET_KEY'] = 'AB73WK2345BKKSWNPK1349'

app.log = logging


def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            app.log.info(f'Try use {func.__name__}')
            return func(*args, **kwargs)
        except Exception as e:
            app.log.error(f'Error in function {func.__name__}, error: {e}')
            return make_response(jsonify({'error': f'Error, {e}'}), 500)

    wrapper.__name__ = func.__name__
    return wrapper


app.exception_handler = exception_handler

from .bin.process.routes import process_blueprint


app.register_blueprint(process_blueprint)
