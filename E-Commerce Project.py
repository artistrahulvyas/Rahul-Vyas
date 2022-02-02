#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
import numpy as np


# In[2]:


data = pd.read_csv('e_commerce.csv')


# In[3]:


data.info()


# In[4]:


data.isnull().sum()


# In[5]:


data.fillna(0, inplace=True)


# In[6]:


purchases = data.groupby(['User_ID']).sum().reset_index()


# In[7]:


data[data['User_ID'] == 1000001]


# In[9]:


purchase_by_age = data.groupby('Age')['Purchase'].mean().reset_index()


# In[11]:


plt.figure(figsize=(16,4))


# In[17]:



plt.grid()
plt.xlabel('Age Group', fontsize=10)
plt.ylabel('Total Purchases in $', fontsize=10)
plt.title('Average Sales distributed by age group', fontsize=15)
plt.show()


# In[18]:


age_and_gender = data.groupby('Age')['Gender'].count().reset_index()
gender = data.groupby('Gender')['Age'].count().reset_index()


# In[19]:


plt.figure(figsize=(12,9))


# In[22]:


plt.pie(age_and_gender['Gender'], labels=age_and_gender['Age'],autopct='%d%%', colors=['cyan', 'steelblue','peru','blue','yellowgreen','salmon','#0040FF'])
plt.axis('equal')
plt.title("Age Distribution", fontsize='20')
plt.show()


# In[23]:


plt.figure(figsize=(12,9))


# In[24]:


plt.pie(gender['Age'], labels=gender['Gender'],autopct='%d%%', colors=['salmon','steelblue'])
plt.axis('equal')
plt.title("Gender Distribution", fontsize='20')
plt.show()


# In[25]:


occupation = data.groupby('Occupation')['Purchase'].mean().reset_index()


# In[27]:


sns.set(style="white", rc={"lines.linewidth": 3})
fig, ax1 = plt.subplots(figsize=(12,9))
sns.barplot(x=occupation['Occupation'],y=occupation['Purchase'],color='#004488',ax=ax1)
sns.lineplot(x=occupation['Occupation'],y=occupation['Purchase'],color='salmon',marker="o",ax=ax1)
plt.axis([-1,21,8000,10000])
plt.title('Occupation Bar Chart', fontsize='15')
plt.show()
sns.set()


# In[28]:


product = data.groupby('Product_ID')['Purchase'].count().reset_index()
product.rename(columns={'Purchase':'Count'},inplace=True)
product_sorted = product.sort_values('Count',ascending=False)


# In[29]:


plt.figure(figsize=(14,8))
plt.plot(product_sorted['Product_ID'][:10], product_sorted['Count'][:10], linestyle='-', color='purple', marker='o')
plt.title("Best-selling Products", fontsize='15')
plt.xlabel('Product ID', fontsize='15')
plt.ylabel('Products Sold', fontsize='15')
plt.show()


# In[ ]:




