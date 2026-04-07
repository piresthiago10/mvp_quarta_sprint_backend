from flask_openapi3 import APIBlueprint
from flask import request, jsonify
from database.database import db
from models.individuo_gen_z import IndividuoGenZ

from logger import logger
from schemas.individuo_gen_z_schema import (
    IndividuoGenZSchema,
    IndividuoGenZViewSchema,
    IndividuoGenZBuscaSchema,
    ListaIndividuosGenZBuscaSchema,
    IndividuoGenZDeleteSchema,
    IndividuoPathSchema,
    apresenta_individuo_gen_z,
)

from models.pipeline import Pipeline
from models.preprocessador import PreProcessador

individuo_bp = APIBlueprint("individuo", __name__)


@individuo_bp.post("/individuos", methods=["POST"], responses={201: IndividuoGenZViewSchema})
def create_individuo(body: IndividuoGenZSchema):
    """Adiciona um individuo_gen_z na base de dados
    Args:
        body (IndividuoGenZBuscaSchema): dados do individuo_gen_z a serem adicionados na base de dados

    Returns:
        IndividuoGenZViewSchema: individuo_gen_z adicionado
    """

    preprocessador = PreProcessador()
    pipeline = Pipeline()

    # recuperando dados do formulário
    name = body.name
    cpf = body.cpf
    age = float(body.age)
    gender = body.gender
    student_working_status = body.student_working_status
    screen_time_hours = float(body.screen_time_hours)
    sleep_quality_score = float(body.sleep_quality_score)
    daily_sleep_hours = float(body.daily_sleep_hours)
    motivation_level = float(body.motivation_level)
    emotional_fatigue_score = float(body.emotional_fatigue_score)
    content_type_preference = body.content_type_preference
    
    X_input = preprocessador.preparar_form(body)
    model_path = "app/machine_learning/pipelines/svm_gen_z_pipeline.pkl"
    modelo = pipeline.carrega_pipeline(model_path)
    outcome = modelo.predict(X_input)

    mapa = {
        "Low": "Baixo risco de burnout",
        "Medium": "Médio risco de burnout",
        "High": "Alto risco de burnout",
    }
    resultado = mapa[outcome[0]]

    individuo = IndividuoGenZ(
        name=name,
        cpf=cpf,
        age=age,
        gender=gender,
        student_working_status=student_working_status,
        screen_time_hours=screen_time_hours,
        daily_sleep_hours=daily_sleep_hours,
        sleep_quality_score=sleep_quality_score,
        motivation_level=motivation_level,
        emotional_fatigue_score=emotional_fatigue_score,
        content_type_preference=content_type_preference,
        outcome=resultado,
    )
    logger.debug(f"Adicionando produto de nome: '{individuo.name}'")

    try:
        # Verifica duplicidade
        exists = IndividuoGenZ.query.filter_by(name=body.name).first()
        if exists:
            msg = "IndividuoGenZ já existente na base"
            logger.warning(f"{msg}: '{body.name}'")
            return {"message": msg}, 409

        # Persistência
        db.session.add(individuo)
        db.session.commit()

        logger.debug(f"IndividuoGenZ criado: '{individuo.name}'")

        return apresenta_individuo_gen_z(individuo), 201

    except Exception as e:
        db.session.rollback()

        logger.exception(f"Erro ao adicionar IndividuoGenZ '{individuo.name}'")

        return {"message": "Erro interno ao salvar item"}, 500


@individuo_bp.get("/individuos", methods=["GET"], responses={200: ListaIndividuosGenZBuscaSchema})
def list_individuos():
    """
    Retorna uma lista de todos os IndividuoGenZ registrados na base.

    Returns:
        list: lista de IndividuoGenZ encontrados
    """
    individuos = IndividuoGenZ.query.all()

    result = [i.to_dict() for i in individuos]

    return jsonify(result), 200

@individuo_bp.get("/individuos/<int:id>", methods=["GET"], responses={200: IndividuoGenZBuscaSchema})
def get_individuo_by_id(path: IndividuoPathSchema):
    """
    Retorna um individuo_gen_z com base no seu id.

    Args:
        id (int): id do individuo_gen_z a ser retornado

    Returns:
        dict: individuo_gen_z encontrado
    """
    individuo = IndividuoGenZ.query.filter_by(id=path.id).first()

    if not individuo:
        return {"message": "IndividuoGenZ não encontrado"}, 404

    return individuo.to_dict(), 200

@individuo_bp.delete("/individuos/<int:id>", methods=["DELETE"], responses={200: IndividuoGenZDeleteSchema})
def delete_individuo(path: IndividuoPathSchema):
    """
    Remove um IndividuoGenZ da base com base no seu id.

    Args:
        id (int): id do IndividuoGenZ a ser removido

    Returns:
        dict: mensagem de resultado da remoção do IndividuoGenZ
    """
    individuo = IndividuoGenZ.query.filter_by(id=path.id).first()

    if not individuo:
        return {"message": "IndividuoGenZ nao encontrado"}, 404

    db.session.delete(individuo)
    db.session.commit()

    return {"message": "IndividuoGenZ removido"}, 200
