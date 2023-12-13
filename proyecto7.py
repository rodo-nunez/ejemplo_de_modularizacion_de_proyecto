# Librerias ---------------------------------------- 

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Loading data ---------------------------------------- 
df = pd.read_csv('files/datasets/input/users_behavior.csv')

# Splitting data into sets ---------------------------------------- 

from sklearn.model_selection import train_test_split

train_valid, test = train_test_split(df, test_size=0.2)
train, valid = train_test_split(train_valid, test_size=0.25)

features_train = train.drop(['is_ultra'], axis=1)
target_train = train['is_ultra']
features_valid = valid.drop(['is_ultra'], axis=1)
target_valid = valid['is_ultra']
features_test = test.drop(['is_ultra'], axis=1)
target_test = test['is_ultra']

# Tuning models ---------------------------------------- 

print("Decision Tree")
for depth in range(1, 11):
    model = DecisionTreeClassifier(max_depth=depth, random_state=12345)
    model.fit(features_train, target_train)
    print("max_depth =", depth)
    print("Train:", model.score(features_train, target_train))
    print("Valid:", model.score(features_valid, target_valid))

print("Random Forest")
for estim in range(10, 101, 10):
    model = RandomForestClassifier(n_estimators=estim, random_state=12345)
    model.fit(features_train, target_train)
    print("n_estimators =", estim)
    print("Train:", model.score(features_train, target_train))
    print("Valid:", model.score(features_valid, target_valid))

print("Logistic Regression")
model = LogisticRegression(random_state=12345)
model.fit(features_train, target_train)
print("Train:", model.score(features_train, target_train))
print("Valid:", model.score(features_valid, target_valid))

# Testing model ---------------------------------------- 

features_full_train = train_valid.drop(['is_ultra'], axis=1)
target_full_train = train_valid['is_ultra']

model = RandomForestClassifier(n_estimators=80, random_state=12345)
model.fit(features_full_train, target_full_train)
model.score(features_test, target_test)


# Sanity check ---------------------------------------- 

print(f"Sanity check: {df['is_ultra'].value_counts() / df.shape[0]}")

