"""
    API desenvolvida com Flask para cadastrar desenvolvedores. Implementa as funções báscias de
    GET, PUT, POST e DELETE.
"""
import json
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

developers = [
    {
        'id': 0,
        'name': 'Guilherme',
        'skills': ['Python', 'Flask']
    },
    {
        'id': 1,
        'name': 'Henrique',
        'skills': ['JavaScript', 'Angular']
    }
]


@app.route('/get-dev/<int:id>/', methods=['GET'])
def get_developer(id):
    if request.method == 'GET':
        try:
            response = developers[id]
        except IndexError:
            message = f'Developer with ID {id} does not exist.'
            response = {'status': 'Error.', 'message': message}
        except Exception:
            message = 'Unknown error. Contact the API\'s admin.'
            response = {'status': 'Error.', 'message': message}
        return jsonify(response)


@app.route('/put-dev/<int:id>/', methods=['PUT', 'GET'])
def put_developer(id):
    if request.method == 'PUT':
        data = json.loads(request.data)
        data['id'] = id
        developers[id] = data
        return jsonify(data)


@app.route('/delete-dev/<int:id>/', methods=['DELETE', 'GET'])
def delete_developer(id):
    if request.method == 'DELETE':
        developers.pop(id)
        for developer in developers:
            developer['id'] -= 1
        return jsonify({'status': 'Success.', 'message': 'Record deleted.'})


@app.route('/dev/', methods=['POST', 'GET'])
def developers_list():
    if request.method == 'POST':
        data = json.loads(request.data)
        position = len(developers)
        data['id'] = position
        developers.append(data)
        return jsonify(developers[position])
    elif request.method == 'GET':
        return jsonify(developers)


if __name__ == '__main__':
    app.run()
