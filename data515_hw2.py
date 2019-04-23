
# coding: utf-8

# In[43]:


import pandas as pd
import numpy as np

permits = pd.read_csv("https://data.seattle.gov/api/views/76t5-zqzr/rows.csv?accessType=DOWNLOAD",
                      usecols=["PermitClass", "PermitClassMapped", "PermitTypeDesc"],
                      dtype=object)
permits.head()


# In[46]:


def test_create_dataframe(df):
    '''(3 points) Create the function test_create_dataframe that takes a pandas DataFrame as input and returns True if the following conditions hold:
   1. The DataFrame contains only the columns that you specified in #1.
   1. The columns contain the correct data type
   1. There are at least 10 rows in the DataFrame.
'''
    rows = np.size(df, 0)
    columns = np.size(df, 1)
    TorF = False
    if columns == 3:
        if rows >= 10:
            for col in range(columns):
                if df.iloc[:,0].dtype == object:
                    TorF = True
    return TorF


# In[47]:


test_create_dataframe(permits)

