from datetime import datetime
from typing import Union

from database.database import db


class IndividuoGenZ(db.Model):
    __tablename__ = "individuo_gen_z"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    cpf = db.Column(db.String(11))
    age = db.Column(db.Integer)
    gender = db.Column(db.String)
    student_working_status = db.Column(db.String)
    daily_sleep_hours = db.Column(db.Integer)
    screen_time_hours = db.Column(db.Float)
    sleep_quality_score = db.Column(db.Float)
    motivation_level = db.Column(db.Float)
    emotional_fatigue_score = db.Column(db.Float)
    content_type_preference = db.Column(db.Integer)
    outcome = db.Column(db.String(5), nullable=True)
    data_insercao = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(
        self,
        name: str,
        cpf: str,
        age: int,
        gender: str,
        student_working_status: str,
        daily_sleep_hours: int,
        screen_time_hours: float,
        sleep_quality_score: float,
        motivation_level: float,
        emotional_fatigue_score: float,
        content_type_preference: str,
        outcome: Union[str, None] = None,
        data_insercao: Union[datetime, None] = None,
    ):
        """_summary_
        Cria um novo individuo_gen_z

        Args:
            name (str): nome
            cpf (str): cpf
            age (int): idade
            gender (str): sexo
            student_working_status (str): status de estudante
            screen_time_hours (float): horas diarias de screen time
            sleep_quality_score (float): pontuação de qualidade de sono
            motivation_level (float): nível de motivação
            emotional_fatigue_score (float): pontuação de fadiga emocional
            content_type_preference (str): preferência de conteúdo
            outcome (Union[str, None], optional): resultado. Defaults to None
            data_insercao (Union[datetime, None], optional): data de inserção. Defaults to None.
        """
        self.name = name
        self.cpf = cpf
        self.age = age
        self.gender = gender
        self.student_working_status = student_working_status
        self.screen_time_hours = screen_time_hours
        self.content_type_preference = content_type_preference
        self.sleep_quality_score = sleep_quality_score
        self.motivation_level = motivation_level
        self.emotional_fatigue_score = emotional_fatigue_score
        self.daily_sleep_hours = daily_sleep_hours
        self.outcome = outcome

        # se não for informada, será a data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao

    def __mask_cpf(self, cpf: str) -> str:
        if not cpf or len(cpf) != 11:
            return None

        return "***.***.***-" + cpf[-2:]

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "cpf": self.__mask_cpf(self.cpf),
            "age": self.age,
            "gender": self.gender,
            "student_working_status": self.student_working_status,
            "screen_time_hours": self.screen_time_hours,
            "content_type_preference": self.content_type_preference,
            "sleep_quality_score": self.sleep_quality_score,
            "motivation_level": self.motivation_level,
            "emotional_fatigue_score": self.emotional_fatigue_score,
            "daily_sleep_hours": self.daily_sleep_hours,
            "outcome": self.outcome
        }