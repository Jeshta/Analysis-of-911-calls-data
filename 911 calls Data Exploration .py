
# coding: utf-8

# In[ ]:

#Importing libraries #


# In[3]:

import numpy as np
import pandas as pd


# In[4]:

# Import visualization libraries and set %matplotlib inline #


# In[5]:

import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic('matplotlib inline')


# In[ ]:

#Read the data to dataframe called df


# In[6]:

df = pd.read_csv('911.csv')


# In[7]:

df.head(5)


# In[8]:

df.info()


# In[ ]:

#Basic Questions...?


# In[ ]:

#top 5 zipcodes for 911 calls?


# In[9]:

df['zip'].value_counts().head(5)


# In[12]:

#top 5 townships (twp) for 911 calls?


# In[13]:

df['twp'].value_counts().head(5)


# In[ ]:

#unique title codes


# In[14]:

df['title'].nunique()


# In[ ]:

#In the titles column there are "Reasons/Departments" specified before the title code. These are EMS, Fire, and Traffic. Use .apply() with a custom lambda expression to create a new column called "Reason" that contains this string value# 


# In[15]:

df['Reason'] = df['title'].apply(lambda title: title.split(':')[0])


# In[ ]:

##common Reason for a 911 call based off on the column 'Reason'?


# In[16]:

df['Reason'].value_counts()


# In[ ]:

#countplot of 911 calls by Reason.Using seaborn#


# In[17]:

sns.countplot(x='Reason',data=df,palette='viridis')


# In[ ]:

#time information. checking the data type of timeStamp column?


# In[18]:

type(df['timeStamp'].iloc[0])


# In[ ]:

#convert the column from strings to DateTime objects.


# In[19]:

df['timeStamp'] = pd.to_datetime(df['timeStamp'])


# In[ ]:

#grabbing specific attributes from a Datetime object


# In[20]:

df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
df['Month'] = df['timeStamp'].apply(lambda time: time.month)
df['Day of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek)


# In[ ]:

#Use the .map() with this dictionary to map the actual string names to the day of the week


# In[21]:

dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
df['Day of Week'] = df['Day of Week'].map(dmap)


# In[ ]:

#creating a countplot of the Day of Week column with the hue based off of the Reason column.Using Seaborn


# In[22]:

sns.countplot(x='Day of Week',data=df,hue='Reason',palette='viridis')


# In[ ]:

#creating a countplot of the Day of Week column


# In[24]:

sns.countplot(x='Month',data=df,hue='Reason',palette='viridis')


# In[ ]:

#LOL..:) 9,10, and 11 are missing.lets cc


# In[ ]:

#creating a gropuby object called byMonth, where we group the DataFrame by the month column and use the count() method for aggregation. Using head() method on this returned DataFrame.


# In[25]:

byMonth = df.groupby('Month').count()
byMonth.head()


# In[ ]:

#create a simple plot off of the dataframe indicating the count of calls per month


# In[26]:

byMonth['twp'].plot()


# In[ ]:

#creating a linear fit on the number of calls per month


# In[27]:

sns.lmplot(x='Month',y='twp',data=byMonth.reset_index())


# In[ ]:

#Create a new column called 'Date' that contains the date from the timeStamp column


# In[28]:

df['Date']=df['timeStamp'].apply(lambda t: t.date())


# In[ ]:

#groupby this Date column with the count() aggregate and creating a plot of counts of 911 calls


# In[29]:

df.groupby('Date').count()['twp'].plot()
plt.tight_layout()


# In[ ]:

#recreating this plot ,but 3 separate plots with each plot representing a Reason for the 911 call


# In[30]:

df[df['Reason']=='Traffic'].groupby('Date').count()['twp'].plot()
plt.title('Traffic')
plt.tight_layout()


# In[31]:

df[df['Reason']=='Fire'].groupby('Date').count()['twp'].plot()
plt.title('Fire')
plt.tight_layout()


# In[32]:

df[df['Reason']=='EMS'].groupby('Date').count()['twp'].plot()
plt.title('EMS')
plt.tight_layout()


# In[ ]:

#restructure the dataframe so that the columns become the Hours and the Index becomes the Day of the Week.


# In[33]:

dayHour = df.groupby(by=['Day of Week','Hour']).count()['Reason'].unstack()
dayHour.head()


# In[34]:

#creating a HeatMap using this new DataFrame


# In[35]:

plt.figure(figsize=(12,6))
sns.heatmap(dayHour,cmap='viridis')


# In[ ]:

#creating a clustermap using this DataFrame


# In[36]:

sns.clustermap(dayHour,cmap='viridis')


# In[ ]:

#repeating these same plots and operations, for a DataFrame that shows the Month as the column


# In[37]:

dayMonth = df.groupby(by=['Day of Week','Month']).count()['Reason'].unstack()
dayMonth.head()


# In[38]:

plt.figure(figsize=(12,6))
sns.heatmap(dayMonth,cmap='viridis')


# In[39]:

sns.clustermap(dayMonth,cmap='viridis')


# In[ ]:



