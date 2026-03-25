from models.avaliador import Avaliador
from models.carregador import Carregador
from models.model import Model
from models.pipeline import Pipeline

carregador = Carregador()
modelo = Model()
avaliador = Avaliador()
pipeline = Pipeline()

url_dados = "app/machine_learning/data/gen_z_full_dataset.csv"
colunas = [
    "Age",
    "Gender",
    "Student_Working_Status",
    "Daily_Social_Media_Hours",
    "Screen_Time_Hours",
    "Night_Scrolling_Frequency",
    "Online_Gaming_Hours",
    "Content_Type_Preference",
    "Exercise_Frequency_per_Week",
    "Daily_Sleep_Hours",
    "Caffeine_Intake_Cups",
    "Study_Work_Hours_per_Day",
    "Overthinking_Score",
    "Anxiety_Score",
    "Mood_Stability_Score",
    "Social_Comparison_Index",
    "Sleep_Quality_Score",
    "Motivation_Level",
    "Emotional_Fatigue_Score",
    "Wellbeing_Index",
    "Burnout_Risk",
]

dataset = carregador.carregar_dados(url_dados, colunas)
X = dataset.drop(["Burnout_Risk"], axis=1)
y = dataset["Burnout_Risk"]


def test_modelo_svm():
    pipeline_path = "app/machine_learning/pipelines/svm_gen_z_pipeline.pkl"
    modelo_svm = modelo.carrega_modelo(pipeline_path)

    acuracia = avaliador.avaliar(modelo_svm, X, y)

    assert acuracia >= 0.90
