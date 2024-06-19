"""
    API desenvolvida com Flask e FlaskRESTful para cadastro de pessoas e tarefas. Implementa as funções báscias de
    GET, PUT, POST e DELETE com persistência de dados em SQLite usando SQLAlchemy.
"""
from flask import Flask
from flask import request
from flask_restful import Resource
from flask_restful import Api
from models import Person
from models import Tasks

app = Flask(__name__)
api = Api(app)


class PersonApi(Resource):
    def get(self, name):
        person = Person.query.filter_by(name=name).first()
        try:
            response = {
                'name': person.name,
                'age': person.age,
                'id': person.id
            }
        except AttributeError:
            response = {
                'status': 'Error.',
                'message': 'Person not found.'
            }
        return response

    def put(self, name):
        person = Person.query.filter_by(name=name).first()
        data = request.json
        if 'name' in data:
            person.name = data['name']
        if 'age' in data:
            person.age = data['age']

        person.save()

        response = {
            'id': person.id,
            'name': person.name,
            'age': person.age
        }
        return response

    def delete(self, name):
        person = Person.query.filter_by(name=name).first()
        message = f'Person {person.name} deleted successfully.'
        person.delete()
        return {
            'status': 'Success.',
            'message': message
        }


class PersonList(Resource):
    def get(self):
        person = Person.query.all()
        response = [{'id': p.id, 'name': p.name, 'age': p.age} for p in person]
        return response

    def post(self):
        data = request.json
        person = Person(name=data['name'], age=data['age'])
        person.save()
        response = {
            'id': person.id,
            'name': person.name,
            'age': person.age
        }
        return response


class TasksApi(Resource):
    def get(self):
        tasks = Tasks.query.all()
        response = [{'id': t.id, 'name': t.name, 'person': t.person.name} for t in tasks]
        return response

    def post(self):
        data = request.json
        person = Person.query.filter_by(name=data['person']).first()
        task = Tasks(name=data['name'], person=person)
        task.save()
        response = {
            'person': task.person.name,
            'name': task.name,
            'id': task.id
        }
        return response


api.add_resource(PersonApi, '/person/<string:name>/')
api.add_resource(PersonList, '/person/')
api.add_resource(TasksApi, '/tasks/')

if __name__ == '__main__':
    app.run()
