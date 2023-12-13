# Librerias ---------------------------------------- 

import pandas as pd
import joblib
import numpy as np

# Loading data ---------------------------------------- 

target_test = pd.read_csv("files/datasets/intermediate/a03_target_test.csv")
features_test = pd.read_csv("files/datasets/intermediate/a03_features_test.csv")


model_rf = joblib.load(f"files/modeling_output/model_fit/b01_model_rf_2.joblib")

# Aplicar modelo ---------------------------------------- 

model_rf.score(features_test, target_test)

target_ejecucion = model_rf.predict(features_test)

# Guardar datos ---------------------------------------- 

np.savetxt("files/datasets/output/c01_target_ejecucion.csv", target_ejecucion, delimiter=',')