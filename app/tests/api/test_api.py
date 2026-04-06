import random

import pytest
import json
from tests.fixtures.individuos_gen_z import sample_individuo_gen_z_data
from tests.conftest import app, client, db_session
from models.individuo_gen_z import IndividuoGenZ


def test_home_redirect(client):
    """Testa se a rota home redireciona para o frontend"""
    response = client.get("/")
    assert response.status_code == 302
    assert "/front/index.html" in response.location


def test_docs_redirect(client):
    """Testa se a rota docs redireciona para openapi"""
    response = client.get("/docs")
    assert response.status_code == 302
    assert "/openapi" in response.location


def teste_get_individuos_gen_z_empty(client, db_session):
    """Testa a listagem de individuos_gen_z quando não há nenhum"""

    response = client.get("/individuos")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)


def test_add_patient_prediction(client, db_session, sample_individuo_gen_z_data):
    """Testa a adição de um IndividuoGenZ com predição"""
    # Primeiro, vamos limpar qualquer paciente existente com o mesmo nome

    individuo_teste = sample_individuo_gen_z_data[0]
    # Agora testamos a adição
    response = client.post(
        "/individuos",
        data=json.dumps(individuo_teste),
        content_type="application/json",
    )

    assert response.status_code == 201
    data = json.loads(response.data)

    # Verifica se o paciente foi criado com todas as informações
    assert data["name"] == individuo_teste["name"]
    assert data["age"] == individuo_teste["age"]
    assert data["cpf"] == individuo_teste["cpf"]
    assert (
        data["student_working_status"]
        == individuo_teste["student_working_status"]
    )
    assert data["screen_time_hours"] == individuo_teste["screen_time_hours"]

    # Verifica se a predição foi feita (outcome deve estar presente)
    assert "outcome" in data
    assert data["outcome"] in [
        "Baixo risco de burnout",
        "Médio risco de burnout",
        "Alto risco de burnout",
    ]

def test_get_individuo_by_name(client, db_session, sample_individuo_gen_z_data):
    """Testa a busca de um IndividuoGenZ por nome"""

    individuo_teste = sample_individuo_gen_z_data[0]
    response = client.post(
        "/individuos",
        data=json.dumps(individuo_teste),
        content_type="application/json",
    )
    assert response.status_code == 201

    # Verifica se um individuo foi encontrado
    response = client.get(f"/individuos/{individuo_teste['name']}")
    assert response.status_code == 200
    data = json.loads(response.data)

    assert data["name"] == individuo_teste["name"]
    
    # Verifica se um individuo nao foi encontrado
    response = client.get("/individuos/invalid_name")
    assert response.status_code == 404
    
def test_delete_individuo(client, db_session, sample_individuo_gen_z_data):
    """Testa a exclusão de um IndividuoGenZ"""
    individuo_teste = IndividuoGenZ(**sample_individuo_gen_z_data[0])
    db_session.session.add(individuo_teste)
    db_session.session.commit()

    # select individuo criado do banco
    result = db_session.session.query(IndividuoGenZ).filter_by(name=individuo_teste.name).first()
    id_individuo = result.id

    # Verifica se um individuo foi excluido
    response = client.delete(f"/individuos/{id_individuo}")
    assert response.status_code == 200
    
    result = db_session.session.query(IndividuoGenZ).filter_by(id=id_individuo).first()
    assert result is None

def random_float(min_val=0.0, max_val=10.0):
    return round(random.uniform(min_val, max_val), 2)
