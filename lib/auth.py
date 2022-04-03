from functools import wraps
from flask import request, jsonify
from server import app
import jwt


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        # return 401 if token is not passed
        if not token:
            return jsonify({'message': 'Token is missing !!'}), 401

        try:
            # decoding the payload to fetch the stored details
            token = token.split(' ')[1]
            data = jwt.decode(token, app.config['SECRET_KEY'])
            user_id = data['user_id']
        except:
            return jsonify({
                'message': 'Token is invalid !!'
            }), 401
        # returns the current logged in users contex to the routes
        return f(*args, user_id=user_id, **kwargs)

    return decorated
