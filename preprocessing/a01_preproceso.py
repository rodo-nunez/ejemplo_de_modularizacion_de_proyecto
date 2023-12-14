# Librerias ---------------------------------------- 

import pandas as pd
import os, sys
sys.path.append(os.getcwd()) # Esto es para agregar al path la ruta de ejecución actual y poder importar respecto a la ruta del proyecto, desde donde se debe ejecutar el código

# Loading data ---------------------------------------- 
users_behavior_raw = pd.read_csv("files/datasets/input/users_behavior.csv")

# Cleaning columns ---------------------------------------- 

def limpiar_columnas(dataset):
                return dataset

users_behavior = limpiar_columnas(users_behavior_raw)

# Eliminating duplicates per period ---------------------------------------- 

# ...

# Checking NAs ---------------------------------------- 

# ...

# Guardar datos ---------------------------------------- 

users_behavior.to_csv("files/datasets/intermediate/a01_users_behavior_cleaned.csv", index=False)


