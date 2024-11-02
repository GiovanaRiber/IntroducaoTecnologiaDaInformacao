#!/usr/bin/env python
# coding: utf-8

# In[101]:

import numpy as np
import pandas as pd
from sklearn import datasets

# In[102]:

iris = datasets.load_iris()

df_iris = pd.DataFrame(iris.data)
df_iris.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
df_iris['target'] = iris.target

df_iris.head()

# In[93]:

x = df_iris.drop(['target'], axis=1)
y = df_iris['target']

# In[94]:

from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(
  max_depth=4,
  criterion='entropy',
  random_state=1
)

model.fit( x , y )
print('.predict(x):\n')
print(model.predict(x))
print('\n\n.predict_proba(x):')
model.predict_proba(x)

# In[75]:

x_regressao = df_iris.drop(['target', 'petal_length'], axis = 1)
y_regressao = df_iris['petal_length']


# In[76]:

from sklearn.tree import DecisionTreeRegressor

model_regressao = DecisionTreeRegressor(
    max_depth = 4,
    criterion = 'squared_error',
    random_state = 1
)

model_regressao.fit( x_regressao, y_regressao)

print('.predict(x):\n')
print(model_regressao.predict(x_regressao))

# In[95]:

from sklearn.model_selection import train_test_split
from sklearn import metrics

x_train, x_test, y_train, y_test = train_test_split(
  x,
  y,
  test_size=0.33,
  random_state=1
)

print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)

x_train.head()

# In[96]:

model = DecisionTreeClassifier(
    max_depth = 4,
    criterion = 'entropy',
    random_state = 1
)

model.fit(
    x_train, y_train
)

y_pred = model.predict(x_test)
y_pred

# In[79]:

metrics.f1_score(
  y_test,
  y_pred,
  average = None
)

# In[92]:

from sklearn.metrics import confusion_matrix
from matplotlib import pyplot as plt

conf_mat = confusion_matrix(y_true=y_test, y_pred=y_pred)
print('Matriz de confusão:\n', conf_mat)

labels = iris.target_names.tolist()
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(conf_mat, cmap=plt.cm.Blues)
fig.colorbar(cax)
ax.set_xticklabels([''] + labels)
ax.set_yticklabels([''] + labels)
plt.xlabel('Predicted')
plt.ylabel('Expected')
plt.show()

# In[81]:

from sklearn.model_selection import cross_val_score
scores = cross_val_score(
    model,
    x,
    y,
    cv = 3,
    scoring = 'accuracy',
    n_jobs = -1
)

print('Score de cada fold', scores)
print('Acurácia média:', np.mean(scores))
print('Desvio padrão:', np.std(scores))

# In[97]:

from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

model = RandomForestClassifier(
    max_depth = 4,
    n_estimators = 25,
    n_jobs = -1,
    random_state = 1
)

model.fit(
    x_train, y_train
)

model.predict(x_test)

# In[98]:

from sklearn.neural_network import MLPClassifier, MLPRegressor
from sklearn.preprocessing import *

std = StandardScaler()
std.fit(x_train)

X_train = std.transform(x_train)
X_test = std.transform(x_test)

model = MLPClassifier(
  hidden_layer_sizes = (50, 15),
  activation = 'relu',
  max_iter=500,
  random_state = 1
)
model.fit(
  x_train, y_train
)

model.predict(x_test)

# In[99]:

from sklearn.svm import SVC, SVR

model = SVC(
    kernel = 'rbf',
    C = 1.0,
    random_state = 1
)

model.fit(
    x_train, y_train
)

model.predict(x_test)

# In[100]:

from xgboost import XGBClassifier, XGBRegressor
model = XGBClassifier(
  n_estimators=100,
  max_depth=3,
  n_jobs=-1,
  random_state=1
)

model.fit(
  x_train, y_train
)

model.predict(x_test)