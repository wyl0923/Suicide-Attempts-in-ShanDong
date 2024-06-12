#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings("ignore")


# In[22]:


df = pd.read_csv("C:\\Users\\HP\\Downloads\\archive\\SuicideChina.csv")
df.head()


# In[6]:


df.info()


# In[7]:


# Checking null values
df.isna().sum()


# In[8]:


# Drop unnecessary columns
df.drop(['Unnamed: 0', 'Person_ID'], axis = 1, inplace = True)


# In[9]:


# Columns Value Count
print(df['Hospitalised'].value_counts())
print('-'*30)
print(df['Died'].value_counts())
print('-'*30)
print(df['Urban'].value_counts())
print('-'*30)
print(df['Education'].value_counts())
print('-'*30)
print(df['Occupation'].value_counts())
print('-'*30)
print(df['method'].value_counts())


# In[11]:


def plots(df, x):
    plt.style.use('dark_background')
    f, ax = plt.subplots(1, 2, figsize = (25, 10))
    Group_data = df.groupby(x)
    sns.barplot(x = Group_data['Age'].mean().index, y = Group_data['Age'].mean().values, ax = ax[0], palette = 'viridis')
    
    for container in ax[0].containers:
        ax[0].bar_label(container, color = 'white', size = 20)

    palette_color = sns.color_palette('viridis')
    plt.pie(x = df[x].value_counts(),
            labels = df[x].value_counts().index,
            autopct = '%.0f%%',
            shadow = True,
            colors = palette_color)
    plt.suptitle(x, fontsize = 25)
    plt.show()


# In[12]:


for i in df.columns:
    if i != 'Age':
        plots(df, i)


# In[13]:


plt.style.use('dark_background')
plt.figure(figsize = (12,20))

list_columns = list(df.columns)

for i in range(len(list_columns)):
    plt.subplot(5, 2, i + 1)
    plt.title(list_columns[i])
    plt.hist(df[list_columns[i]])
    plt.grid(alpha = 0.5)
    
plt.tight_layout()


# In[14]:


plt.style.use('dark_background')

fig, axs = plt.subplots(6, 2, figsize = (10, 20))
i = 1
for feature in df.columns:
    if feature not in ['Died'] and i < 14:
        plt.subplot(5, 2, i)
        sns.histplot(data = df, x = feature,
                     kde = True, palette = 'winter', 
                     hue = 'Died', alpha = 0.8)
        plt.grid(alpha = 0.5)
        i += 1


# In[15]:


plt.figure(figsize = (10, 7))
plt.style.use('dark_background')

sns.violinplot(x = 'Died', y = 'Month', data = df, palette = 'viridis')


# In[16]:


plt.style.use('dark_background')
plt.figure(figsize = (12, 10))

plt.hexbin(df['Age'], df['Month'], gridsize = 12, cmap = 'viridis', mincnt = 1)
plt.colorbar(label = 'Count')
plt.xlabel('Age')
plt.ylabel('Month')
plt.title('Age Compared to Month of Occurrence')
plt.show()


# In[17]:


plt.style.use('dark_background')
plt.figure(figsize = (10, 5))

plt.hexbin(df['Age'], df['Year'], gridsize = 3, cmap = 'viridis', mincnt = 1)
plt.colorbar(label = 'Count')
plt.xlabel('Age')
plt.ylabel('Year')
plt.title('Age Compared to Year of Occurrence')
plt.show()


# In[18]:


list_str = df.select_dtypes(include = 'object').columns
le = LabelEncoder()

for c in list_str:
    df[c] = le.fit_transform(df[c])


# In[19]:


plt.figure(figsize = (15, 12))
plt.style.use('dark_background')
sns.heatmap(df.corr(), annot = True, cmap = 'viridis')


# In[ ]:




