import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

iris_data = load_iris()

x = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
y = pd.DataFrame(iris_data.target, columns=['class'])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=5)
y_train = y_train.values.ravel()

model = RandomForestClassifier(n_estimators=100, max_depth=4)

model.fit(x_train, y_train)
model.predict(x_test)
model.score(x_test, y_test)
