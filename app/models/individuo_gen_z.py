from datetime import datetime
from typing import Union

from database.database import db

# colunas = Pregnancies,Glucose,BloodPressure,SkinThickness,test,BMI,DiabetesPedigreeFunction,Age,Outcome


class IndividuoGenZ(db.Model):
    __tablename__ = "individuo_gen_z"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    cpf = db.Column(db.String(11))
    age = db.Column(db.Integer)
    gender = db.Column(db.Integer)
    student_working_status = db.Column(db.Integer)
    daily_social_media_hours = db.Column(db.Float)
    screen_time_hours = db.Column(db.Float)
    night_scrolling_frequency = db.Column(db.Float)
    online_gaming_hours = db.Column(db.Float)
    content_type_preference = db.Column(db.Integer)
    exercise_frequency_per_week = db.Column(db.Float)
    daily_sleep_hours = db.Column(db.Integer)
    caffeine_intake_cups = db.Column(db.Integer)
    study_work_hours_per_day = db.Column(db.Integer)
    overthinking_score = db.Column(db.Float)
    anxiety_score = db.Column(db.Float)
    mood_stability_score = db.Column(db.Float)
    social_comparison_index = db.Column(db.Float)
    sleep_quality_score = db.Column(db.Float)
    motivation_level = db.Column(db.Float)
    emotional_fatigue_score = db.Column(db.Float)
    wellbeing_index = db.Column(db.Float)
    outcome = db.Column(db.String(5), nullable=True)
    data_insercao = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(
        self,
        name: str,
        cpf: str,
        age: int,
        gender: int,
        student_working_status: int,
        daily_social_media_hours: float,
        screen_time_hours: float,
        night_scrolling_frequency: float,
        online_gaming_hours: float,
        content_type_preference: int,
        exercise_frequency_per_week: float,
        daily_sleep_hours: int,
        caffeine_intake_cups: int,
        study_work_hours_per_day: int,
        overthinking_score: float,
        anxiety_score: float,
        mood_stability_score: float,
        social_comparison_index: float,
        sleep_quality_score: float,
        motivation_level: float,
        emotional_fatigue_score: float,
        wellbeing_index: float,
        outcome: Union[str, None] = None,
        data_insercao: Union[datetime, None] = None,
    ):
        """_summary_
        Cria um novo individuo_gen_z

        Args:
            name (str): nome
            cpf (str): cpf
            age (int): idade
            gender (int): gênero
            student_working_status (int): status de estudos/trabalho
            daily_social_media_hours (float): horas diarias de social media
            screen_time_hours (float): tempo de tela
            night_scrolling_frequency (float): frequencia de rolagem noturna
            online_gaming_hours (float): horas diarias de jogo online
            content_type_preference (int): tipo de conteudo preferido
            exercise_frequency_per_week (float): frequencia de exercicios
            daily_sleep_hours (int): horas diarias de sono
            caffeine_intake_cups (int): quantidade de copos de café
            study_work_hours_per_day (int): horas diarias de estudo/trabalho
            overthinking_score (float): pontuação de overthinking
            anxiety_score (float): pontuação de ansiedade
            mood_stability_score (float): pontuação de estabilidade de humor
            social_comparison_index (float): índice de comparação social
            sleep_quality_score (float): índice de qualidade de sono
            motivation_level (float): nível de motivação
            emotional_fatigue_score (float): pontuação de fadiga emocional
            wellbeing_index (float): índice de bem-estar
            data_insercao (Union[DateTime, None], optional): data de inserção. Defaults to None.
        """
        self.name = name
        self.cpf = cpf
        self.age = age
        self.gender = gender
        self.student_working_status = student_working_status
        self.daily_social_media_hours = daily_social_media_hours
        self.screen_time_hours = screen_time_hours
        self.night_scrolling_frequency = night_scrolling_frequency
        self.online_gaming_hours = online_gaming_hours
        self.content_type_preference = content_type_preference
        self.exercise_frequency_per_week = exercise_frequency_per_week
        self.daily_sleep_hours = daily_sleep_hours
        self.caffeine_intake_cups = caffeine_intake_cups
        self.study_work_hours_per_day = study_work_hours_per_day
        self.overthinking_score = overthinking_score
        self.anxiety_score = anxiety_score
        self.mood_stability_score = mood_stability_score
        self.social_comparison_index = social_comparison_index
        self.sleep_quality_score = sleep_quality_score
        self.motivation_level = motivation_level
        self.emotional_fatigue_score = emotional_fatigue_score
        self.webwellbeing_index = wellbeing_index
        self.outcome = outcome

        # se não for informada, será a data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao
