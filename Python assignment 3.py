#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pip', 'install mysql-connector-python')
get_ipython().run_line_magic('pip', 'install pymysql')


# In[2]:


from sqlalchemy import create_engine
import pandas as pd


# In[3]:


host = 'localhost'       # or your IP
port = 3306              # default MySQL port
database = 'db5'
user = 'root'
password = 'password'
table_name = 'workpatterns_clean3'


# In[4]:


engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}')


# In[5]:


df = pd.read_sql_table(table_name, con=engine)


# In[6]:


df.head()


# In[ ]:




