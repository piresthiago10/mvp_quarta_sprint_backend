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
                    "Screen_Time_Hours": form.screen_time_hours,
                    "Night_Scrolling_Frequency": form.night_scrolling_frequency,
                    "Online_Gaming_Hours": form.online_gaming_hours,
                    "Content_Type_Preference": form.content_type_preference,
                    "Exercise_Frequency_per_Week": form.exercise_frequency_per_week,
                    "Daily_Sleep_Hours": form.daily_sleep_hours,
                    "Caffeine_Intake_Cups": form.caffeine_intake_cups,
                    "Study_Work_Hours_per_Day": form.study_work_hours_per_day,
                    "Overthinking_Score": form.overthinking_score,
                    "Anxiety_Score": form.anxiety_score,
                    "Mood_Stability_Score": form.mood_stability_score,
                    "Social_Comparison_Index": form.social_comparison_index,
                    "Sleep_Quality_Score": form.sleep_quality_score,
                    "Motivation_Level": form.motivation_level,
                    "Emotional_Fatigue_Score": form.emotional_fatigue_score,
                    "Wellbeing_Index": form.wellbeing_index,
                }
            ]
        )
        scaler = pickle.load(
            open("app/machine_learning/scalers/minmax_scaler_gen_z.pkl", "rb")
        )
        X_input = scaler.transform(X_input)
        print(X_input)
        return X_input

    def scaler(self, X_train):
        """Normaliza os dados."""
        # normalização/padronização
        scaler = pickle.load(
            open("./machine_learning/scalers/minmax_scaler_gen_z.pkl", "rb")
        )
        reescaled_X_train = scaler.transform(X_train)
        return reescaled_X_train
