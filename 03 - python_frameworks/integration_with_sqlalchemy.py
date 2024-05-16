"""
    Este arquivo tem como objetivo a integração do Python com o sqlAlchemy utilizando do modelo ORM
    para fazer o mapeamento das classes para o modelo relacional do Banco de Dados.
"""

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy import Column
from sqlalchemy import func
from sqlalchemy import select
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import ForeignKey

Base = declarative_base()


class Client(Base):
    __tablename__ = "client"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    cpf = Column(String(9), unique=True, nullable=False)
    address = Column(String, nullable=False)

    account = relationship(
       "Account", back_populates="client", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"Client(id={self.id}, name={self.name}, cpf={self.cpf}, address={self.address})"


class Account(Base):
    __tablename__ = "account"

    id = Column(Integer, primary_key=True)
    type = Column(String, default="Checking Account")
    agency = Column(String, nullable=False)
    number = Column(Integer, nullable=False)
    balance = Column(Float, nullable=False)
    client_id = Column(Integer, ForeignKey("client.id"), nullable=False)

    client = relationship(
        "Client", back_populates="account"
    )

    def __repr__(self):
        return (f"Account(id={self.id}, type={self.type}, agency={self.agency}, "
                f"number={self.number}, balance={self.balance})")


engine = create_engine("sqlite://")

Base.metadata.create_all(engine)

inspector = inspect(engine)

with Session(engine) as session:
    guilherme = Client(
        name="guilherme",
        cpf="093582394",
        address="Rua Rosa Nascimento Lima, 381",
        account=[Account(type="", agency="0001", number=241, balance=150.01)]
    )

    izabel = Client(
        name="izabel",
        cpf="984567873",
        address="Rua Rosa Nascimento Lima, 302",
        account=[Account(type="Savings Account", agency="0002", number=921, balance=680.52)]
    )

session.add_all([guilherme, izabel])

session.commit()

statement = select(Client).where(Client.name.in_(['guilherme', 'izabel']))
print("\nRecuperando dados do cliente pela condição de filtragem:")
for client in session.scalars(statement):
    print(client)

statement_account = select(Account).where(Account.client_id.in_([2]))
print("\nRecuperando informações da conta de guilherme:")
for account in session.scalars(statement_account):
    print(account)

statement_order = select(Client).order_by(Client.name.desc())
print("\nRecuperando e ordenando nome de clientes em ordem decrescente:")
for result in session.scalars(statement_order):
    print(result)

statement_join = select(Client.cpf, Account.balance).join_from(Client, Account)
connection = engine.connect()
results = connection.execute(statement_join).fetchall()
print("\nJuntando as tabelas Client e Account e executando o statement a partir da connection:")
for result in results:
    print(result)

statement_count = select(func.count('*')).select_from(Client)
print("\nContando todas as instâncias de Client:")
for result in session.scalars(statement_count):
    print(result)
