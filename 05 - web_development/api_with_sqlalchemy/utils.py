"""
    Programa utilitário que implementa funções de inserção, atualização,
    consulta e deleção para a tabela 'Person' e 'Users'.
"""
from models import Person
from models import Users


# Insere pessoas na tabela pessoa
def insert_person():
    person = Person(name="Guilherme", age="19")
    print(person)
    person.save()


# Consulta pessoas na tabela pessoa
def query_person():
    person = Person.query.all()
    print(person)


# Atualiza pessoas na tabela pessoa
def update_person():
    person = Person.query.filter_by(name="Guilherme").first()
    person.age = 22
    person.save()


# Deleta pessoas na tabela pessoa
def delete_person():
    person = Person.query.filter_by(name="Guilherme").first()
    person.delete()


def insert_user(login, password):
    user = Users(login=login, password=password)
    user.save()


def query_all_users():
    user = Users.query.all()
    print(user)


if __name__ == '__main__':
    # insert_user("guilherme", "123")
    # insert_user("henrique", "321")
    query_all_users()
    # insert_person()
    # update_person()
    # query_person()
