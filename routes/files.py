from server import app, request
from models import File
from lib.auth import token_required
from botocore.exceptions import ClientError
import uuid


@app.route('/files/', methods=['POST'])
@token_required
def create_file(user_id):
    body = request.json
    file_id = str(uuid.uuid1())
    file = File(file_id)
    file.update_data(body, user_id)
    return {
        'file_id': file_id
    }


@app.route('/files/<file_id>', methods=['GET'])
@token_required
def get_file(file_id, user_id):
    try:
        file = File(file_id)
        return file.get_data()
    except ClientError:
        return {
            'message': 'File not found!!!'
        }


@app.route('/files/<file_id>', methods=['PUT'])
@token_required
def update_file(file_id, user_id):
    body = request.json
    file = File(file_id)
    file.update_data(body, user_id)
    return {
        'message': 'File updated successfully!!!',
        'file': file.get_data()
    }


@app.route('/files/<file_id>', methods=['DELETE'])
@token_required
def delete_file(file_id, user_id):
    file = File(file_id)
    file.delete()
    return {
        'message': 'File deleted successfully!!!'
    }
