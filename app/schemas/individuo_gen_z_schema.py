from pydantic import BaseModel
from typing import List
from models.individuo_gen_z import IndividuoGenZ


class IndividuoGenZSchema(BaseModel):
    """Define como um novo IndividuoGenZ a ser inserido deve ser representado."""

    name: str = "João da Silva"
    age: int = 20
    cpf: str = "12345678901"
    gender: str = 'Male'
    student_working_status: str = 'Student'
    daily_social_media_hours: float = 0.0
    daily_sleep_hours: float = 7
    screen_time_hours: float = 0.0
    sleep_quality_score: float = 0.0
    motivation_level: float = 0.0
    emotional_fatigue_score: float = 0.0
    content_type_preference: str = "Educational"


class IndividuoGenZViewSchema(BaseModel):
    """Define como um IndividuoGenZ será retornado."""

    id: int = 1
    name: str = "João da Silva"
    age: int = 20
    gender: int = 1
    student_working_status: str = 'Student'
    daily_social_media_hours: float = 0.0
    screen_time_hours: float = 0.0
    sleep_quality_score: float = 0.0
    motivation_level: float = 0.0
    emotional_fatigue_score: float = 0.0
    content_type_preference: str = "Educational"
    outcome: str = "Baixo"


class IndividuoGenZBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca.
    Ela será feita com base no nome do IndividuoGenZ.
    """

    name: str = "João da Silva"


class ListaIndividuosGenZBuscaSchema(BaseModel):
    """Define como uma lista de IndividuosGenZ será representada."""

    individuos: List[IndividuoGenZViewSchema]


class IndividuoGenZDeleteSchema(BaseModel):
    """Define como um paciente para deleção será representado"""

    name: str = "Maria"


def apresenta_individuo_gen_z(individuo_gen_z: IndividuoGenZ):
    """Retorna uma representação do IndividuoGenZ seguindo o schema definido em
    IndividuoGenZViewSchema.
    """

    return {
        "id": individuo_gen_z.id,
        "name": individuo_gen_z.name,
        "age": individuo_gen_z.age,
        "cpf": individuo_gen_z.cpf,
        "gender": individuo_gen_z.gender,
        "student_working_status": individuo_gen_z.student_working_status,
        "daily_social_media_hours": individuo_gen_z.daily_social_media_hours,
        "screen_time_hours": individuo_gen_z.screen_time_hours,
        "sleep_quality_score": individuo_gen_z.sleep_quality_score,
        "motivation_level": individuo_gen_z.motivation_level,
        "emotional_fatigue_score": individuo_gen_z.emotional_fatigue_score,
        "content_type_preference": individuo_gen_z.content_type_preference,
        "outcome": individuo_gen_z.outcome,
    }


def apresenta_individuos_gen_z(individuos_gen_z: List[IndividuoGenZ]):
    """Retorna uma representação do IndividuoGenZ seguindo o schema definido em
    IndividuoGenZViewSchema.
    """
    result = []
    for individuo_gen_z in individuos_gen_z:
        result.append(apresenta_individuo_gen_z(individuo_gen_z))

    return {"individuos_gen_z": result}
