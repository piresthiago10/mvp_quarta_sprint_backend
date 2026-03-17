from pydantic import BaseModel
from typing import List
from models.individuo_gen_z import IndividuoGenZ


class IndividuoGenZSchema(BaseModel):
    """ Define como um novo IndividuoGenZ a ser inserido deve ser representado."""
    name: str = "João da Silva"
    age: int = 20
    gender: int = 1
    student_working_status: int = 1
    daily_social_media_hours: float = 0.0
    screen_time_hours: float = 0.0
    night_scrolling_frequency: float = 0.0
    online_gaming_hours: float = 0.0
    content_type_preference: int = 1
    exercise_frequency_per_week: float = 0.0
    daily_sleep_hours: int = 0
    caffeine_intake_cups: int = 0
    study_work_hours_per_day: int = 0
    overthinking_score: float = 0.0
    anxiety_score: float = 0.0
    mood_stability_score: float = 0.0
    social_comparison_index: float = 0.0
    sleep_quality_score: float = 0.0
    motivation_level: float = 0.0
    emotional_fatigue_score: float = 0.0
    wellbeing_index: float = 0.0


class IndividuoGenZViewSchema(BaseModel):
    """Define como um IndividuoGenZ será retornado."""
    id: int = 1
    name: str = "João da Silva"
    age: int = 20
    gender: int = 1
    student_working_status: int = 1
    daily_social_media_hours: float = 0.0
    screen_time_hours: float = 0.0
    night_scrolling_frequency: float = 0.0
    online_gaming_hours: float = 0.0
    content_type_preference: int = 1
    exercise_frequency_per_week: float = 0.0
    daily_sleep_hours: int = 0
    caffeine_intake_cups: int = 0
    study_work_hours_per_day: int = 0
    overthinking_score: float = 0.0
    anxiety_score: float = 0.0
    mood_stability_score: float = 0.0
    social_comparison_index: float = 0.0
    sleep_quality_score: float = 0.0
    motivation_level: float = 0.0
    emotional_fatigue_score: float = 0.0
    wellbeing_index: float = 0.0
    resultado: str = "Baixo"


class IndividuoGenZBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca.
    Ela será feita com base no nome do IndividuoGenZ.
    """
    name: str = "João da Silva"


class ListaIndividuosGenZBuscaSchema(BaseModel):
    """Define como uma lista de IndividuosGenZ será representada.
    """
    individuos: List[IndividuoGenZViewSchema]


def apresenta_individuo_gen_z(individuo_gen_z: IndividuoGenZ):
    """Retorna uma representação do IndividuoGenZ seguindo o schema definido em
        IndividuoGenZViewSchema.
    """

    return {
        "id": individuo_gen_z.id,
        "name": individuo_gen_z.name,
        "age": individuo_gen_z.age,
        "gender": individuo_gen_z.gender,
        "student_working_status": individuo_gen_z.student_working_status,
        "daily_social_media_hours": individuo_gen_z.daily_social_media_hours,
        "screen_time_hours": individuo_gen_z.screen_time_hours,
        "night_scrolling_frequency": individuo_gen_z.night_scrolling_frequency,
        "online_gaming_hours": individuo_gen_z.online_gaming_hours,
        "content_type_preference": individuo_gen_z.content_type_preference,
        "exercise_frequency_per_week": individuo_gen_z.exercise_frequency_per_week,
        "daily_sleep_hours": individuo_gen_z.daily_sleep_hours,
        "caffeine_intake_cups": individuo_gen_z.caffeine_intake_cups,
        "study_work_hours_per_day": individuo_gen_z.study_work_hours_per_day,
        "overthinking_score": individuo_gen_z.overthinking_score,
        "anxiety_score": individuo_gen_z.anxiety_score,
        "mood_stability_score": individuo_gen_z.mood_stability_score,
        "social_comparison_index": individuo_gen_z.social_comparison_index,
        "sleep_quality_score": individuo_gen_z.sleep_quality_score,
        "motivation_level": individuo_gen_z.motivation_level,
        "emotional_fatigue_score": individuo_gen_z.emotional_fatigue_score,
        "wellbeing_index": individuo_gen_z.wellbeing_index,
        "resultado": individuo_gen_z.resultado
    }


def apresenta_individuos_gen_z(individuos_gen_z: List[IndividuoGenZ]):
    """ Retorna uma representação do IndividuoGenZ seguindo o schema definido em
        IndividuoGenZViewSchema.
    """
    result = []
    for individuo_gen_z in individuos_gen_z:
        result.append(apresenta_individuo_gen_z(individuo_gen_z))

    return {"individuos_gen_z": result}
