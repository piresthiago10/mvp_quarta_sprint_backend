import pytest


@pytest.fixture
def sample_individuo_gen_z_data():
    """Dados de exemplo para teste de genz."""
    return [
        {
            "name": "Baixo Risco",
            "age": 20,
            "cpf": "12345678900",
            "gender": 1,
            "student_working_status": 0,
            "daily_social_media_hours": 0.40,
            "screen_time_hours": 5.0,
            "night_scrolling_frequency": 0.23,
            "online_gaming_hours": 0.50,
            "content_type_preference": 3,
            "exercise_frequency_per_week": 5.19,
            "daily_sleep_hours": 10,
            "caffeine_intake_cups": 3,
            "study_work_hours_per_day": 6,
            "overthinking_score": 2,
            "anxiety_score": 1.2,
            "mood_stability_score": 7,
            "social_comparison_index": 1.79,
            "sleep_quality_score": 9.5,
            "motivation_level": 6.80,
            "emotional_fatigue_score": 3.28,
            "wellbeing_index": 8.07,
        }
    ]
