import pytest
    
@pytest.fixture
def sample_individuo_gen_z_data():
    """Dados de exemplo para teste de genz."""
    return [
        {
            "name": "John Doe",
            "age": 20,
            "cpf": "12345678900",
            "gender": 'Male',
            "student_working_status": "Student",
            "screen_time_hours": 5.0,
            "sleep_quality_score": 9.5,
            "daily_sleep_hours": 10,
            "motivation_level": 6.80,
            "emotional_fatigue_score": 3.28,
            "content_type_preference": "Educational"
        }
    ]
