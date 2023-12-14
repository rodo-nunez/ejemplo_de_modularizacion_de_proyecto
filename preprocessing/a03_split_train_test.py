# Librerias ---------------------------------------- 

import pandas as pd
import os, sys
sys.path.append(os.getcwd()) # Esto es para agregar al path la ruta de ejecución actual y poder importar respecto a la ruta del proyecto, desde donde se debe ejecutar el código

# Loading data ---------------------------------------- 

users_behavior_cleaned = pd.read_csv("files/datasets/intermediate/a02_users_behavior_cleaned.csv")

# Splitting data into sets ---------------------------------------- 

from sklearn.model_selection import train_test_split

train_valid, test = train_test_split(users_behavior_cleaned, test_size=0.2)
train, valid = train_test_split(train_valid, test_size=0.25)

features_train = train.drop(['is_ultra'], axis=1)
target_train = train['is_ultra']
features_valid = valid.drop(['is_ultra'], axis=1)
target_valid = valid['is_ultra']
features_test = test.drop(['is_ultra'], axis=1)
target_test = test['is_ultra']

# Save data ---------------------------------------- 

train_valid.to_csv("files/datasets/intermediate/a03_train_valid.csv", index=False)

features_train.to_csv("files/datasets/intermediate/a03_features_train.csv", index=False)
target_train.to_csv("files/datasets/intermediate/a03_target_train.csv", index=False)
features_valid.to_csv("files/datasets/intermediate/a03_features_valid.csv", index=False)
target_valid.to_csv("files/datasets/intermediate/a03_target_valid.csv", index=False)
features_test.to_csv("files/datasets/intermediate/a03_features_test.csv", index=False)
target_test.to_csv("files/datasets/intermediate/a03_target_test.csv", index=False)
