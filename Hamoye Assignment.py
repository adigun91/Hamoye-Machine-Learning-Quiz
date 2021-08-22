#!/usr/bin/env python
# coding: utf-8

# In[14]:


#list
A = [1,2,3,4,5,6]
B = [13, 21, 34]
C = A + B
D = A.append(B)
E = A.extend(B)
print(C)
print(D) #append does not work
print(E) #extend does not work


# In[17]:


import numpy as np
np.identity(3) #3x3 array of identity matrix


# In[20]:


#Pandas
import pandas as pd
csv_df = pd.read_csv('https://raw.githubusercontent.com/WalePhenomenon/climate_change/master/fuel_ferc1.csv')
#csv_df.to_csv('https://raw.githubusercontent.com/WalePhenomenon/climate_change/master/fuel_ferc1.csv', index=False)


# In[22]:


url='https://raw.githubusercontent.com/WalePhenomenon/climate_change/master/fuel_ferc1.csv' 
fuel_data = pd.read_csv(url, error_bad_lines=False) 
fuel_data.describe(include='all')


# In[23]:


#check for missing values 
fuel_data.isnull().sum()


# In[24]:


#use groupby to count the sum of each unique value in the fuel unit column 
fuel_data.groupby('fuel_unit')['fuel_unit'].count() 
fuel_data[['fuel_unit']] = fuel_data[['fuel_unit']].fillna(value='mcf')  


# In[25]:


#check if missing values have been filled 
fuel_data.isnull().sum() 
fuel_data.groupby('report_year')['report_year'].count() 


# In[26]:


#group by the fuel type code year and print the first entries in all the groups formed              
fuel_data.groupby('fuel_type_code_pudl').first()


# In[28]:


#Merging in Pandas can be likened to join operations in relational databases like SQL 
fuel_df1 = fuel_data.iloc[0:19000].reset_index(drop=True) 
fuel_df2 = fuel_data.iloc[19000:].reset_index(drop=True)
#check that the length of both dataframes sum to the expected length assert 
len(fuel_data) == (len(fuel_df1) + len(fuel_df2))  


# In[29]:


#outer merge returns all rows in both dataframes 
pd.merge(fuel_df1, fuel_df2, how="outer")  


# In[30]:


#removes rows from the right dataframe that do not have a match with the left 
#and keeps all rows from the left 
pd.merge(fuel_df1, fuel_df2, how="left") 


# In[32]:


#standard deviattion
print(fuel_data.std())


# In[34]:


#75th percentile
print(fuel_data.quantile(0.75)) # 75th percentile


# In[35]:


#skew
dataFrame = pd.DataFrame(data=fuel_data);
skewValue = dataFrame.skew(axis=1)
print(skewValue)


# In[37]:


#kurt
dataFrame = pd.DataFrame(data=fuel_data);
kurt = dataFrame.kurt(axis=1)
print(kurt)

