from flask import Blueprint, request, jsonify
from database.database import db
from models.individuo_gen_z import IndividuoGenZ

from logger import logger
from schemas.individuo_gen_z_schema import (
    IndividuoGenZSchema,
    IndividuoGenZViewSchema,
    IndividuoGenZBuscaSchema,
    ListaIndividuosGenZBuscaSchema,
    IndividuoGenZDeleteSchema,
    apresenta_individuo_gen_z,
)

from models.pipeline import Pipeline
from models.preprocessador import PreProcessador

individuo_bp = Blueprint("individuo", __name__)


@individuo_bp.route("/individuos", methods=["POST"])
def create_individuo():
    """Adiciona um individuo_gen_z na base de dados
    Args:
        form (IndividuoGenZBuscaSchema): dados do individuo_gen_z a serem adicionados na base de dados

    Returns:
        IndividuoGenZViewSchema: individuo_gen_z adicionado
    """

    data = request.get_json()
    form = IndividuoGenZSchema(**data)

    preprocessador = PreProcessador()
    pipeline = Pipeline()

    # recuperando dados do formulário
    name = form.name
    cpf = form.cpf
    age = form.age
    gender = form.gender
    student_working_status = form.student_working_status
    daily_social_media_hours = form.daily_social_media_hours
    screen_time_hours = form.screen_time_hours
    night_scrolling_frequency = form.night_scrolling_frequency
    online_gaming_hours = form.online_gaming_hours
    content_type_preference = form.content_type_preference
    exercise_frequency_per_week = form.exercise_frequency_per_week
    daily_sleep_hours = form.daily_sleep_hours
    caffeine_intake_cups = form.caffeine_intake_cups
    study_work_hours_per_day = form.study_work_hours_per_day
    overthinking_score = form.overthinking_score
    anxiety_score = form.anxiety_score
    mood_stability_score = form.mood_stability_score
    social_comparison_index = form.social_comparison_index
    sleep_quality_score = form.sleep_quality_score
    motivation_level = form.motivation_level
    emotional_fatigue_score = form.emotional_fatigue_score
    wellbeing_index = form.wellbeing_index

    X_input = preprocessador.preparar_form(form)
    model_path = "app/machine_learning/pipelines/svm_gen_z_pipeline.pkl"
    modelo = pipeline.carrega_pipeline(model_path)
    outcome = modelo.predict(X_input)
    mapa = {
        0: "Baixo risco de burnout",
        1: "Médio risco de burnout",
        2: "Alto risco de burnout",
    }
    resultado = mapa[outcome[0]]

    individuo = IndividuoGenZ(
        name=name,
        cpf=cpf,
        age=age,
        gender=gender,
        student_working_status=student_working_status,
        daily_social_media_hours=daily_social_media_hours,
        screen_time_hours=screen_time_hours,
        night_scrolling_frequency=night_scrolling_frequency,
        online_gaming_hours=online_gaming_hours,
        content_type_preference=content_type_preference,
        exercise_frequency_per_week=exercise_frequency_per_week,
        daily_sleep_hours=daily_sleep_hours,
        caffeine_intake_cups=caffeine_intake_cups,
        study_work_hours_per_day=study_work_hours_per_day,
        overthinking_score=overthinking_score,
        anxiety_score=anxiety_score,
        mood_stability_score=mood_stability_score,
        social_comparison_index=social_comparison_index,
        sleep_quality_score=sleep_quality_score,
        motivation_level=motivation_level,
        emotional_fatigue_score=emotional_fatigue_score,
        wellbeing_index=wellbeing_index,
        outcome=resultado,
    )
    logger.debug(f"Adicionando produto de nome: '{individuo.name}'")

    try:
        # Verifica duplicidade
        exists = IndividuoGenZ.query.filter_by(name=form.name).first()
        if exists:
            msg = "IndividuoGenZ já existente na base"
            logger.warning(f"{msg}: '{form.name}'")
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


@individuo_bp.route("/individuos", methods=["GET"])
def list_individuos():
    individuos = IndividuoGenZ.query.all()

    result = [i.to_dict() for i in individuos]

    return jsonify(result), 200

@individuo_bp.route("/individuos/<name>", methods=["GET"])
def get_individuo_by_name(name):
    individuo = IndividuoGenZ.query.filter_by(name=name).first()

    if not individuo:
        return {"message": "IndividuoGenZ não encontrado"}, 404

    return individuo.to_dict(), 200

@individuo_bp.route("/individuos/<id>", methods=["DELETE"])
def delete_individuo(id):
    individuo = IndividuoGenZ.query.filter_by(id=id).first()

    if not individuo:
        return {"message": "IndividuoGenZ nao encontrado"}, 404

    db.session.delete(individuo)
    db.session.commit()

    return {"message": "IndividuoGenZ removido"}, 200
