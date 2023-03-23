#!/usr/bin/env python
# coding: utf-8

# # DATA EXPLORATION USING PANDAS

# ## List of Top 50 Largest Companies in India

# #### 
# This Dataset lists the Top 50 largest companies in India in terms of their revenue, net profit and total assets, according to the American business magazines Fortune and Forbes.
# 
# 2022 Forbes List
# 
# This list is based on the Forbes Global 2000, which ranks the world's 2,000 largest publicly traded companies. The Forbes list takes into account a multitude of factors, including the revenue, net profit, total assets and market value of each company; each factor is given a weighted rank in terms of importance when considering the overall ranking. The table below also lists the headquarters location and industry sector of each company. The figures are in billions of US dollars and are for the year 2022. All 50 companies from India in the Forbes 2000 are listed.
# 

# In[1]:


import pandas as pd


# #### pandas library imported as pd for data exploration

# In[2]:


sample=pd.read_csv("C://Users//indhu//OneDrive//Documents//PYTHON WORKINGS//List of largest companies in India.csv")


# #### List of largest companies in India.csv dataset is read from the location 

# In[3]:


sample


# #### This dataset is downloaded from kaggle.com

# In[4]:


sample.head()


# #### The first 5 observations of the dataset

# In[5]:


sample.tail()


# #### The last 5 observations of the dataset

# In[6]:


sample.count()


# #### Counts number of observations in the dataset 

# In[7]:


sample.info()


# #### To know the datatype of the variables and memory usage of the dataset.

# In[8]:


sample.describe()


# #### Basic statistics of the dataset

# In[9]:


sample.shape


# #### 50 observations and 10 variables 

# In[10]:


sample.columns


# #### The column names of the dataset

# In[11]:


sample.index


# #### The range of the dataset starts from 0 and ends at 50

# In[12]:


sample.sort_values(['Revenue(billions US$)'],ascending=True)


# #### Arranged values of dataset in ascending order by using 'Revenue(billions US$)' variable 

# In[13]:


sample['Headquarters'].value_counts()


# #### The count of values in 'Headquarters' variable.

# In[14]:


sample.drop_duplicates(inplace=True)


# #### There are no duplicate values present in the dataset

# In[15]:


sample_subset=sample[['Name','Headquarters','Industry']]


# #### The subset is created for 'Name','Headquarters' and 'Industry'

# In[16]:


sample_subset


# #### This dataset is the subset of sample dataset

# In[17]:


sample_row=sample[sample['Profit(billions US$)']>2]


# #### To view the conditional dataset, using sample_row.¶

# In[18]:


sample_row


# #### The row subset is created for the value above 2 in 'Profit(billions US$)' variable.

# In[19]:


sample['Expenses']=sample['Revenue(billions US$)']-sample['Profit(billions US$)']


# #### An additional value 'Expenses' is added to the dataset

# In[20]:


sample


# #### The dataset after adding a variable 'Expenses'

# In[21]:


sample_index=sample.set_index("Name")


# #### To change the default index position of the 'Name' variable

# In[22]:


sample_index


# #### The dataset after setting 'Name' as index

# In[23]:


sample_index=sample_index.reset_index()


# #### To remove the variable as an index in the dataset

# In[24]:


sample_index


# #### The dataset after changing the 'Name' variable as index to default index

# In[25]:


sample_loc=sample.loc[(sample.Expenses>=15)&(sample.Headquarters=='Mumbai')]


# #### Specific value 'Mumbai' is only located in the dataset

# In[26]:


sample_loc


# #### The dataset after performing locate function

# In[27]:


sample_iloc=sample.iloc[0:6,2:5]


# #### Specific observations and variables[0:6,2:5] are located using the index

# In[28]:


sample_iloc


# #### The dataset after performing index location function

# In[29]:


sample_agg=sample.groupby("Headquarters")['Assets(billions US$)'].mean()


# #### Performed aggregation using groupby 

# In[30]:


sample_agg


# #### The dataset after performing groupby function

# In[31]:


sample['Forbes 2000 rank']=sample['Forbes 2000 rank'].astype('object')


# #### The astype function helps to change the data type of the variables

# In[32]:


sample.info()


# #### To check whether the datatype of 'Forbes 2000 rank' is changed as 'object' or not
