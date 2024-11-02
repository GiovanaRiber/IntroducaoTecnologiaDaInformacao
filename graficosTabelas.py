#!/usr/bin/env python
# coding: utf-8

# In[66]:

import numpy as np
import pandas as pd
from sklearn import datasets

# In[67]:

iris = datasets.load_iris()

# In[68]:

iris.data


# In[69]:

iris.target

# In[70]:

df_iris = pd.DataFrame(iris.data)
df_iris['target'] = iris.target

df_iris.head()

# In[71]:

df_iris.columns.tolist()

# In[72]:

df_iris.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'type']
df_iris.head(10)


# In[73]:


df_iris.shape


# In[74]:


df_iris['sepal_length'].head()


# In[75]:


df_iris[['sepal_length', 'petal_length']].head()


# In[76]:


df_iris.drop(['type'], axis = 1).head()


# In[77]:


df_iris[df_iris['type'] == 2].head()


# In[78]:


df_iris[df_iris['petal_length'] > 5].head()


# In[79]:


df_iris[
    (df_iris['type'] == 2) & (df_iris['petal_length'] > 5)
].head()


# In[80]:


print('Menor:', df_iris['petal_width'].min())
print('Maior:', df_iris['petal_width'].max())
print('Média:', df_iris['petal_width'].mean())


# In[89]:


from sklearn.neural_network import MLPClassifier

mlp = MLPClassifier(
    hidden_layer_sizes = (100, 50),
    tol = 0.01
)

mlp.fit(
    df_iris.drop(['type'], axis = 1),
    df_iris['type']
)

mlp.predict(
    [
        [6, 5, 5, 1],
        [6, 5, 5, 10],
        [2, 2, 4, 2]
    ]
)


# In[82]:


src = 'https://raw.githubusercontent.com/rafjaa/machine_learning_fecib/master/src/wine-quality-classifier/dados/winequality-red.csv'

df_wine = pd.read_csv(src, sep = ';')
df_wine.head()


# In[83]:


s_wine = df_wine.groupby('Qualidade').count()['Álcool']

print('\nTotal de vinhos: ', df_wine.shape[0])
s_wine.plot(kind = 'bar', title = 'Total de vinhos para cada nota(distribuução de frequência)')


# In[84]:


import matplotlib.pyplot as plt
import seaborn as sns

corr_mat = df_wine.corr()

f, ax = plt.subplots(figsize=(10, 10))

sns.heatmap(
corr_mat,
annot=True,
square=True,
vmax=1,
vmin= -1
)


# In[85]:


df_wine['Qualidade'] = df_wine['Qualidade'].apply(lambda x: 0 if x < 6 else 1)

df_wine.groupby('Qualidade').count()['Álcool'].plot(kind = 'bar', title = 'Vinhos bons(1) e ruins(0)')


# In[86]:


from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(
    n_estimators = 50,
    max_depth = 5
)

clf.fit(
   df_wine.drop(['Qualidade'], axis=1),
   df_wine['Qualidade']
)

clf.feature_importances_

# In[87]:
feat_importances = pd.Series(
   clf.feature_importances_,
   index=df_wine.drop(['Qualidade'], axis=1).columns
)
plt.style.use('ggplot')
feat_importances.plot(kind='barh');