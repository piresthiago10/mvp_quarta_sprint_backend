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

    individuo_baixo_risco = sample_individuo_gen_z_data[0]
    # Agora testamos a adição
    response = client.post(
        "/individuos",
        data=json.dumps(individuo_baixo_risco),
        content_type="application/json",
    )

    assert response.status_code == 201
    data = json.loads(response.data)

    # Verifica se o paciente foi criado com todas as informações
    assert data["name"] == individuo_baixo_risco["name"]
    assert data["age"] == individuo_baixo_risco["age"]
    assert data["cpf"] == individuo_baixo_risco["cpf"]
    assert (
        data["student_working_status"]
        == individuo_baixo_risco["student_working_status"]
    )
    assert (
        data["daily_social_media_hours"]
        == individuo_baixo_risco["daily_social_media_hours"]
    )
    assert data["screen_time_hours"] == individuo_baixo_risco["screen_time_hours"]
    assert (
        data["night_scrolling_frequency"]
        == individuo_baixo_risco["night_scrolling_frequency"]
    )
    assert data["online_gaming_hours"] == individuo_baixo_risco["online_gaming_hours"]
    assert (
        data["content_type_preference"]
        == individuo_baixo_risco["content_type_preference"]
    )

    # Verifica se a predição foi feita (outcome deve estar presente)
    assert "outcome" in data
    assert data["outcome"] in [
        "Baixo risco de burnout",
        "Médio risco de burnout",
        "Alto risco de burnout",
    ]
