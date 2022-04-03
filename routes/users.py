from server import app
from flask import jsonify
import jwt


@app.route('/test-user/', methods=['GET'])
def get_test_user():
    token = jwt.encode({"user_id": "12345"}, app.config['SECRET_KEY']).decode("utf-8")
    return jsonify({
        'token': str(token)
    })

