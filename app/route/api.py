# Created by Zhen-Yi Yu on 2024/03/19

import json
from flask import Blueprint, request, jsonify, flash
from flask import current_app as flask_current_app


import requests
apis = Blueprint('api', __name__)

# Error Handler
@apis.errorhandler(Exception)
def handle_exception(e):
    # Get the route that encountered the exception
    route = request.path
    user_ip = request.access_route[0]       
    return jsonify({'error': str(e)}), 500


# Query the user list
@apis.route('/helloworld', methods=['GET'])
def helloworld():
    return jsonify({'response': 'Hello World'}), 200
