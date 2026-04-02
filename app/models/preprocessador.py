from sklearn.model_selection import train_test_split
import pickle
import numpy as np
import pandas as pd


class PreProcessador:

    def __init__(self):
        """Inicializa o preprocessador"""
        pass

    def separa_teste_treino(self, dataset, percentual_teste, seed=7):
        """Cuida de todo o pré-processamento."""
        # limpeza dos dados e eliminação de outliers

        # feature selection

        # divisão em treino e teste
        X_train, X_test, Y_train, Y_test = self.__preparar_holdout(
            dataset, percentual_teste, seed
        )
        # normalização/padronização

        return (X_train, X_test, Y_train, Y_test)

    def __preparar_holdout(self, dataset, percentual_teste, seed):
        """Divide os dados em treino e teste usando o método holdout.
        Assume que a variável target está na última coluna.
        O parâmetro test_size é o percentual de dados de teste.
        """
        dados = dataset.values
        X = dados[:, 0:-1]
        Y = dados[:, -1]
        return train_test_split(X, Y, test_size=percentual_teste, random_state=seed)

    def preparar_form(self, form):
        """Prepara os dados recebidos do front para serem usados no modelo."""
        X_input = pd.DataFrame(
            [
                {
                    "Age": form.age,
                    "Gender": form.gender,
                    "Student_Working_Status": form.student_working_status,
                    "Daily_Social_Media_Hours": form.daily_social_media_hours,
                    "Daily_Sleep_Hours": form.daily_sleep_hours,
                    "Screen_Time_Hours": form.screen_time_hours,
                    "Sleep_Quality_Score": form.sleep_quality_score,
                    "Motivation_Level": form.motivation_level,
                    "Emotional_Fatigue_Score": form.emotional_fatigue_score,
                    "Content_Type_Preference": form.content_type_preference
                }
            ]
        )
        X_input['Sleep_Efficiency'] = X_input['Sleep_Quality_Score'] / (X_input['Daily_Sleep_Hours'] + 1)
        X_input['Screen_Time_Ratio'] = X_input['Screen_Time_Hours'] / (24 - X_input['Daily_Sleep_Hours'])
        X_input['Wellbeing_Balance'] = X_input['Motivation_Level'] - X_input['Emotional_Fatigue_Score']
        return X_input
