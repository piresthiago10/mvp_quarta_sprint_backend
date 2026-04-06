from models.avaliador import Avaliador
from models.carregador import Carregador
from models.model import Model
from models.pipeline import Pipeline
import pandas as pd

carregador = Carregador()
modelo = Model()
avaliador = Avaliador()
pipeline = Pipeline()



def test_modelo_svm():
    pipeline_path = "app/machine_learning/pipelines/svm_gen_z_pipeline.pkl"
    pipeline_svm = pipeline.carrega_pipeline(pipeline_path)
    X_test = pd.read_csv("app/machine_learning/data/X_test_dataset_gen_z.csv")
    y_test = pd.read_csv("app/machine_learning/data/y_test_dataset_gen_z.csv")
    y_test = y_test.squeeze()

    acuracia = avaliador.avaliar(pipeline_svm, X_test, y_test)

    assert acuracia >= 0.80
