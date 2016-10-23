
# coding: utf-8

# In[1]:


#anaconda3
import pandas as pd


# In[2]:

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pylab import *


# # loading data

# In[18]:

df = pd.read_csv("allmovie_IMDB.csv" ,encoding="utf-8" ,header=0,dtype=np.str,error_bad_lines=False)


# In[6]:

df.head()


# # missing values

# In[7]:

num_lines=df.shape[0]
num_lines


# In[8]:

missing_num_length=num_lines-len(df.length.dropna())
missing_num_name=num_lines-len(df.name.dropna())
missing_num_stars=num_lines-len(df.stars.dropna())
missing_rate_length=float(missing_num_length)/num_lines*100
missing_rate_title=float(missing_num_name)/num_lines*100
missing_rate_stars=float(missing_num_stars)/num_lines*100
print("missing_length: number:%s,rate:%s"%(missing_num_length,missing_rate_length) +r"%")
print("missing_title: number:%s,rate:%s"%(missing_num_name,missing_rate_title) +r"%")
print("missing_stars: number:%s,rate:%s"%(missing_num_stars,missing_rate_stars) +r"%")


# # this task is to analise distributions of diffrent textual columns 

# In[9]:

length_values=df.length.dropna().apply(len)
length_avg, length_max, length_min=length_values.mean(),length_values.max(),length_values.min()
print("the len of column 'length':\naverage_len %s\nmax_len %s\nmin_len %s" %(length_avg,length_max,length_min))


# In[10]:

name_values=df.name.dropna().apply(len)
name_avg, name_max, name_min=name_values.mean(),name_values.max(),name_values.min()
print("the len of column 'name':\naverage_len %s\nmax_len %s\nmin_len %s" %(name_avg,name_max,name_min))


# In[11]:

stars_values=df.stars.dropna().apply(len)
stars_avg, stars_max, stars_min=stars_values.mean(),stars_values.max(),stars_values.min()
print("the len of column 'stars:\naverage_len %s\nmax_len %s\nmin_len %s" %(stars_avg,stars_max,stars_min))


# # Task5:Outliers and Anomalies

# In[12]:

name_values=df.name.dropna().apply(len)
plt.figure(figsize=(12,6))
plt.hist(name_values,bins=name_values.max())
plt.xlabel("the len of name")
plt.ylabel("count")
plt.grid()
plt.title("the hist of the name_len")
plt.show()


# In[13]:

#From the histogram above we can sight that there are few points larger than 50, 
#which are outliers or anomalies.


# In[14]:

length_values=df.length.dropna().apply(len)
plt.figure(figsize=(12,6))
plt.hist(length_values,bins=length_values.max())
plt.xlabel("the len of length")
plt.ylabel("count")
plt.grid()
plt.title("the hist of the length_len")
plt.show()


# In[15]:

stars_values=df.stars.dropna().apply(len)
plt.figure(figsize=(12,6))
plt.hist(stars_values,bins=stars_values.max())
plt.xlabel("the len of stars")
plt.ylabel("count")
plt.grid()
plt.title("the hist of the stars_len")
plt.show()


# In[16]:

# From the histogram above we can sight that there are few points larger than 60 or smaller than 20,
# which are outliers or anomalies.


# In[ ]:



