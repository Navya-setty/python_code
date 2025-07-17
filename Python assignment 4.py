#!/usr/bin/env python
# coding: utf-8

# In[1]:


#%pip install mysql-connector-python
#%pip install pymysql


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
print(type(engine))


# In[5]:


df = pd.read_sql_table(table_name, con=engine)
print(type(df))


# In[6]:


df.head()


# In[7]:


df["gender"]= df["gender"].str.replace("-"," ",regex=False)
df[["minimum_salary","maximum_salary"]]= df["salary_range"].str.split("-",n=1,expand= True)
df.drop("salary_range",axis=1, inplace=True)
#df["maximum_salary"]= df["maximum_salary"].str.repalce("k","",regex=False)


# In[8]:


df.head()


# In[9]:


df["maximum_salary"]= df["maximum_salary"].str.replace("k","",regex=False)


# In[10]:


df.head()


# In[11]:


df["minimum_salary"]= df["minimum_salary"].astype("str")+"000"


# In[12]:


df["maximum_salary"]= df["maximum_salary"].astype("str")+"000"
df.head()


# In[13]:


df["employee_id"]= df["employee_id"].str.replace("-","",regex=False)
df.head()


# In[14]:


df[["city","country"]]= df["location"].str.split(",",n=1,expand= True)
df.head()


# In[15]:


df.drop("location",axis=1, inplace=True)
df.head()


# In[16]:


df.to_sql(name="hello_from_python", con=engine, if_exists="replace", index=False)

