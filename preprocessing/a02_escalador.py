# Librerias ---------------------------------------- 

import pandas as pd

users_behavior = pd.read_csv("files/datasets/intermediate/a01_users_behavior_cleaned.csv")

# Creación del escalador ---------------------------------------- 

# Guardar escalador ---------------------------------------- 

users_behavior.to_csv("files/datasets/intermediate/a02_users_behavior_cleaned.csv")
