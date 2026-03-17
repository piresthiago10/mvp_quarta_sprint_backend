from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from models import Base

# colunas = Pregnancies,Glucose,BloodPressure,SkinThickness,test,BMI,DiabetesPedigreeFunction,Age,Outcome

class IndividuoGenZ(Base):
    __tablename__ = 'individuo_gen_z'
    
    id = Column(Integer, primary_key=True)
    name= Column(String(50))
    age = Column(Integer)
    gender = Column(Integer)
    student_working_status = Column(Integer)
    daily_social_media_hours = Column(Float)
    screen_time_hours = Column(Float)
    night_scrolling_frequency = Column(Float)
    online_gaming_hours = Column(Float)
    content_type_preference = Column(Integer)
    exercise_frequency_per_week = Column(Float)
    daily_sleep_hours = Column(Integer)
    caffeine_intake_cups = Column(Integer)
    study_work_hours_per_day = Column(Integer)
    overthinking_score = Column(Float)
    anxiety_score = Column(Float)
    mood_stability_score = Column(Float)
    social_comparison_index = Column(Float)
    sleep_quality_score = Column(Float)
    motivation_level = Column(Float)
    emotional_fatigue_score = Column(Float)
    wellbeing_index = Column(Float)
    resultado = Column(String(5), nullable=True)
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(
        self, 
        name:str, 
        age:int, 
        gender:int, 
        student_working_status:int, 
        daily_social_media_hours:float, 
        screen_time_hours:float, 
        night_scrolling_frequency:float, 
        online_gaming_hours:float,
        content_type_preference:int, 
        exercise_frequency_per_week:float, 
        daily_sleep_hours:int,
        caffeine_intake_cups:int, 
        study_work_hours_per_day:int, 
        overthinking_score:float,
        anxiety_score:float, 
        mood_stability_score:float, 
        social_comparison_index:float,
        sleep_quality_score:float, 
        motivation_level:float, 
        emotional_fatigue_score:float,
        wellbeing_index:float, 
        data_insercao:Union[DateTime, None] = None
        ):
        """_summary_
        Cria um novo individuo_gen_z

        Args:
            name (str): nome
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
        self.name=name
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

        # se não for informada, será a data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao