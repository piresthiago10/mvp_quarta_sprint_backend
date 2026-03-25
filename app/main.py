# from flask_openapi3 import OpenAPI, Info, Tag
# from flask import redirect, request
# from urllib.parse import unquote

# from sqlalchemy.exc import IntegrityError

# from models.individuo_gen_z import IndividuoGenZ
# from database.database import db
# from logger import logger
# from schemas.individuo_gen_z_schema import (
#     IndividuoGenZSchema,
#     IndividuoGenZViewSchema,
#     IndividuoGenZBuscaSchema,
#     ListaIndividuosGenZBuscaSchema,
#     IndividuoGenZDeleteSchema,
#     apresenta_individuo_gen_z
# )

# from models.pipeline import Pipeline
# from models.preprocessador import PreProcessador

# from schemas.error_schema import ErrorSchema
# from flask_cors import CORS

# from config import ProductionConfig

# # Instanciando o objeto OpenAPI
# info = Info(title="IndividuoGenZ", version="1.0.0")


# app = create_app(ProductionConfig)

# CORS(app)

# # Definindo tags para agrupamento das rotas
# home_tag = Tag(
#     name="Documentação",
#     description="Seleção de documentação: Swagger, Redoc ou RapiDoc",
# )
# individuo_tag = Tag(
#     name="IndividuoGenZ",
#     description="Adição, visualização, remoção e predição de pacientes com Diabetes",
# )


# @app.get("/", tags=[home_tag])
# def home():
#     """Redireciona para o index.html do frontend."""
#     return redirect("/front/index.html")

# # Rota para documentação OpenAPI


# @app.get("/docs", tags=[home_tag])
# def docs():
#     """Redireciona para /openapi, tela que permite a escolha do estilo de documentação."""
#     return redirect("/openapi")


# @app.get(
#     "/individuos_gen_z",
#     tags=[individuo_tag],
#     responses={"200": IndividuoGenZViewSchema, "404": ErrorSchema},
# )
# def get_individuos_gen_z():
#     """Lista todos os individuos_gen_z cadastrados na base
#     Args:
#        none

#     Returns:
#         list: lista de individuos_gen_z cadastrados na base
#     """
#     logger.debug("Coletando dados sobre todos os individuos_gen_z")

#     result = IndividuoGenZ.query.all()

#     if not result:
#         return {"individuos_gen_z": []}, 200
#     else:
#         logger.debug(f"%d individuos_gen_z econtrados" % len(result))
#         print(result)
#         return apresenta_individuo_gen_z(result), 200

# @app.post(
#     "/individuos_gen_z",
#     tags=[individuo_tag],
#     responses={
#         "200": IndividuoGenZViewSchema,
#         "400": ErrorSchema,
#         "409": ErrorSchema,
#     },
# )
# def predict(form: IndividuoGenZSchema):
#     """Adiciona um individuo_gen_z na base de dados
#     Args:
#         form (IndividuoGenZBuscaSchema): dados do individuo_gen_z a serem adicionados na base de dados

#     Returns:
#         IndividuoGenZViewSchema: individuo_gen_z adicionado
#     """

#     data = request.get_json()
#     form = IndividuoGenZSchema(**data)

#     preprocessador = PreProcessador()
#     pipeline = Pipeline()

#     # recuperando dados do formulário
#     name = form.name
#     cpf = form.cpf
#     age = form.age
#     gender = form.gender
#     student_working_status = form.student_working_status
#     daily_social_media_hours = form.daily_social_media_hours
#     screen_time_hours = form.screen_time_hours
#     night_scrolling_frequency = form.night_scrolling_frequency
#     online_gaming_hours = form.online_gaming_hours
#     content_type_preference = form.content_type_preference
#     exercise_frequency_per_week = form.exercise_frequency_per_week
#     daily_sleep_hours = form.daily_sleep_hours
#     caffeine_intake_cups = form.caffeine_intake_cups
#     study_work_hours_per_day = form.study_work_hours_per_day
#     overthinking_score = form.overthinking_score
#     anxiety_score = form.anxiety_score
#     mood_stability_score = form.mood_stability_score
#     social_comparison_index = form.social_comparison_index
#     sleep_quality_score = form.sleep_quality_score
#     motivation_level = form.motivation_level
#     emotional_fatigue_score = form.emotional_fatigue_score
#     wellbeing_index = form.wellbeing_index

#     X_input = preprocessador.preparar_form(form)
#     model_path = "app/machine_learning/pipelines/svm_gen_z_pipeline.pkl"
#     modelo = pipeline.carrega_pipeline(model_path)
#     outcome = modelo.predict(X_input)
#     mapa = {
#         0: "Baixo risco de burnout",
#         1: "Médio risco de burnout",
#         2: "Alto risco de burnout"
#     }
#     resultado = mapa[outcome[0]]

#     individuo = IndividuoGenZ(
#         name=name,
#         cpf=cpf,
#         age=age,
#         gender=gender,
#         student_working_status=student_working_status,
#         daily_social_media_hours=daily_social_media_hours,
#         screen_time_hours=screen_time_hours,
#         night_scrolling_frequency=night_scrolling_frequency,
#         online_gaming_hours=online_gaming_hours,
#         content_type_preference=content_type_preference,
#         exercise_frequency_per_week=exercise_frequency_per_week,
#         daily_sleep_hours=daily_sleep_hours,
#         caffeine_intake_cups=caffeine_intake_cups,
#         study_work_hours_per_day=study_work_hours_per_day,
#         overthinking_score=overthinking_score,
#         anxiety_score=anxiety_score,
#         mood_stability_score=mood_stability_score,
#         social_comparison_index=social_comparison_index,
#         sleep_quality_score=sleep_quality_score,
#         motivation_level=motivation_level,
#         emotional_fatigue_score=emotional_fatigue_score,
#         wellbeing_index=wellbeing_index,
#         outcome=resultado
#     )
#     logger.debug(f"Adicionando produto de nome: '{individuo.name}'")

#     try:
#         # Criando conexão com a base
#         session = Session()

#         # Checando se IndividuoGenZ já existe na base
#         if session.query(IndividuoGenZ).filter(IndividuoGenZ.name == form.name).first():
#             error_msg = "IndividuoGenZ já existente na base :/"
#             logger.warning(
#                 f"Erro ao adicionar IndividuoGenZ '{individuo.name}', {error_msg}"
#             )
#             return {"message": error_msg}, 409

#         # Adicionando IndividuoGenZ
#         session.add(individuo)
#         # Efetivando o comando de adição
#         session.commit()
#         # Concluindo a transação
#         logger.debug(f"Adicionado IndividuoGenZ de nome: '{individuo.name}'")
#         return apresenta_individuo_gen_z(individuo), 200

#         # Caso ocorra algum erro na adição
#     except Exception as e:
#         breakpoint()
#         error_msg = "Não foi possível salvar novo item :/"
#         logger.warning(
#             f"Erro ao adicionar IndividuoGenZ '{individuo.name}', {error_msg}"
#         )
#         return {"message": error_msg}, 400


# if __name__ == "__main__":
#     app.run(debug=True)

from api import create_app
from config import ProductionConfig

app = create_app(ProductionConfig)

if __name__ == "__main__":
    app.run(debug=True)
