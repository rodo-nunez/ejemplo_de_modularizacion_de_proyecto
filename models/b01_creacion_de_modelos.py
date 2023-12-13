import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import joblib

# Leer datos ---------------------------------------- 

train_valid = pd.read_csv("files/datasets/intermediate/a03_train_valid.csv")

features_train = pd.read_csv("files/datasets/intermediate/a03_features_train.csv")
target_train = pd.read_csv("files/datasets/intermediate/a03_target_train.csv")
features_valid = pd.read_csv("files/datasets/intermediate/a03_features_valid.csv")
target_valid = pd.read_csv("files/datasets/intermediate/a03_target_valid.csv")
features_test = pd.read_csv("files/datasets/intermediate/a03_features_test.csv")
target_test = pd.read_csv("files/datasets/intermediate/a03_target_test.csv")

# Tuning models ---------------------------------------- 

print("Decision Tree")
for depth in range(1, 11):
    model_dt = DecisionTreeClassifier(max_depth=depth, random_state=12345)
    model_dt.fit(features_train, target_train)
    print("max_depth =", depth)
    print("Train:", model_dt.score(features_train, target_train))
    print("Valid:", model_dt.score(features_valid, target_valid))

print("Random Forest")
for estim in range(10, 101, 10):
    model_rf = RandomForestClassifier(n_estimators=estim, random_state=12345)
    model_rf.fit(features_train, target_train)
    print("n_estimators =", estim)
    print("Train:", model_rf.score(features_train, target_train))
    print("Valid:", model_rf.score(features_valid, target_valid))

print("Logistic Regression")
model_lr = LogisticRegression(random_state=12345)
model_lr.fit(features_train, target_train)
print("Train:", model_lr.score(features_train, target_train))
print("Valid:", model_lr.score(features_valid, target_valid))

# Testing model ---------------------------------------- 

features_full_train = train_valid.drop(['is_ultra'], axis=1)
target_full_train = train_valid['is_ultra']

model = RandomForestClassifier(n_estimators=80, random_state=12345)
model.fit(features_full_train, target_full_train)
model.score(features_test, target_test)

# Save model ---------------------------------------- 

joblib.dump(
        model_dt,
        f"files/modeling_output/model_fit/b01_model_dt.joblib"
        )

joblib.dump(
        model_rf,
        f"files/modeling_output/model_fit/b01_model_rf.joblib"
        )

joblib.dump(
        model_lr,
        f"files/modeling_output/model_fit/b01_model_lr.joblib"
        )
