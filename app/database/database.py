from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

# importando os elementos definidos no modelo
from app.models.base import Base
from app.models.individuo_gen_z import IndividuoGenZ
from app.models.model import Model
from app.models.pipeline import Pipeline
from app.models.preprocessador import PreProcessador
from app.models.avaliador import Avaliador
from app.models.carregador import Carregador

db_path = "database/"
# Verifica se o diretorio não existe
if not os.path.exists(db_path):
   # então cria o diretorio
   os.makedirs(db_path)

# url de acesso ao banco (essa é uma url de acesso ao sqlite local)
db_url = 'sqlite:///%s/pacientes.sqlite3' % db_path

# cria a engine de conexão com o banco
engine = create_engine(db_url, echo=False)

# Instancia um criador de seção com o banco
Session = sessionmaker(bind=engine)

# cria o banco se ele não existir 
if not database_exists(engine.url):
    create_database(engine.url) 

# cria as tabelas do banco, caso não existam
Base.metadata.create_all(engine)