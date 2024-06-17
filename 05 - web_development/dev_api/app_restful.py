"""

"""
import json
from flask import Flask
from flask import request
from flask_restful import Resource
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

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


class GetDeveloper(Resource):
    def get(self, id):
        try:
            response = developers[id]
        except IndexError:
            message = f'Developer with ID {id} does not exist.'
            response = {'status': 'Error.', 'message': message}
        except Exception:
            message = 'Unknown error. Contact the API\'s admin.'
            response = {'status': 'Error.', 'message': message}
        return response


class PutDeveloper(Resource):
    def put(self, id):
        data = json.loads(request.data)
        data['id'] = len(developers)
        data['id'] = id
        developers[id] = data
        return data


class DeleteDeveloper(Resource):
    def delete(self, id):
        developers.pop(id)
        for developer in developers:
            if developer['id'] <= id:
                pass
            elif developer['id'] > id:
                developer['id'] -= 1
        return {'status': 'Success.', 'message': 'Record deleted.'}


class DevelopersList(Resource):
    def get(self):
        return developers

    def post(self):
        data = json.loads(request.data)
        position = len(developers)
        data['id'] = position
        developers.append(data)
        return developers[position]


api.add_resource(GetDeveloper, '/dev/<int:id>/')
api.add_resource(PutDeveloper, '/dev/<int:id>/')
api.add_resource(DeleteDeveloper, '/dev/<int:id>/')
api.add_resource(DevelopersList, '/dev/')

if __name__ == '__main__':
    app.run()
