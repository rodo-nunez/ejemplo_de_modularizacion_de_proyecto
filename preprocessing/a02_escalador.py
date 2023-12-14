# Librerias ---------------------------------------- 

import pandas as pd
import os, sys
sys.path.append(os.getcwd()) # Esto es para agregar al path la ruta de ejecución actual y poder importar respecto a la ruta del proyecto, desde donde se debe ejecutar el código

# Loading data ---------------------------------------- 

users_behavior = pd.read_csv("files/datasets/intermediate/a01_users_behavior_cleaned.csv")

# Creación del escalador ---------------------------------------- 

# Guardar escalador ---------------------------------------- 

users_behavior.to_csv("files/datasets/intermediate/a02_users_behavior_cleaned.csv", index=False)
