"""
    Este arquivo tem como objetivo a integração do Python com o MongoDB.
"""

import datetime
import pprint

import pymongo as py_mongo

client = py_mongo.MongoClient(
    "mongodb+srv://guilherme:12d15i23g@firstproject.8vj4qzu.mongodb.net/"
    "?retryWrites=true&w=majority&appName=firstProject"
)

db = client.project
collection = db.project.collection

# Insert de um documento
bank = {
    "client_name": "emilly",
    "cpf": "153674937",
    "address": "Rua Rosa Nascimento Lima, 231",
    "type": "Checking Account",
    "agency": "0001",
    "number": 643,
    "balance": 200,
    "tags": ["account", "client", "bank", "checking_account"],
    "creation_date": datetime.datetime.utcnow()
}

banks = db.banks
banks.insert_one(bank)

# Bulk insert
bank = [
    {
        "client_name": "guilherme",
        "cpf": "093582394",
        "address": "Rua Rosa Nascimento Lima, 381",
        "type": "Checking Account",
        "agency": "0002",
        "number": 241,
        "balance": 150.01,
        "tags": ["account", "client", "bank", "checking_account"],
        "creation_date": datetime.datetime.utcnow()
    },
    {
        "client_name": "izabel",
        "cpf": "984567873",
        "address": "Rua Rosa Nascimento Lima, 302",
        "type": "Savings Account",
        "agency": "0003",
        "number": 921,
        "balance": 680.52,
        "tags": ["account", "client", "bank", "savings_account"],
        "creation_date": datetime.datetime.utcnow()
    }
]

bank_id = banks.insert_many(bank).inserted_ids
print("Verificando IDs dos documentos inseridos:")
print(bank_id)

print("\nRecuperação de dados:")
pprint.pprint(db.banks.find_one({"client_name": "guilherme"}))

print("\nDocumentos presentes na coleção banks:")
for bank in banks.find():
    pprint.pprint(bank)

print("\nContando a quantidade de documentos em banks:")
print(banks.count_documents({}))

print("\nContando a quantidade de documentos em banks com condição de filtragem:")
print(banks.count_documents({"type": "Checking Account"}))

print("\nRecuperando informações da coleção banks de maneira ordenada:")
for bank in banks.find({}).sort("creation_date"):
    pprint.pprint(bank)

print("\nRecuperando index:")
result = db.banks.create_index({'client_name': py_mongo.ASCENDING}, unique=True)
print(sorted(list(db.banks.index_information())))

print("\nColeções armazenadas no mongoDB:")
collections = db.list_collection_names()
for collection in collections:
    print(collection)

# Apagando o banco de dados
client.drop_database('project')

print("\nColeções após exclusão:")
print(db.list_collection_names())
