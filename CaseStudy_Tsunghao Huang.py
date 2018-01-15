import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats.stats import pearsonr

#Read CSV and take a first look
df = pd.read_csv('/CaseStudy_PerformanceChart.csv')
df.info()

#Data cleaning
for i in range(0,len(df)):
    df.Time[i] = df.Time[i].replace(":00 PM", "")
    df.Time[i] = df.Time[i].replace(":00 AM", "")


df['Time'] = pd.to_datetime(df['Time'])


#Corrlation Map
f,ax = plt.subplots(figsize=(18, 18))
sns.heatmap(df.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax)
#pearson correlation test
pearsonr(df['% Availability'], df['Mdn Webpage Response (ms)'])
pearsonr(df['Avg Script Bytes'], df['Mdn Webpage Response (ms)'])

#Scatter plots
df.plot(kind = "scatter",x='Avg Script Bytes',y = 'Mdn Webpage Response (ms)')

#plot variables with datetime
df.plot(kind = 'line', x='Time', y='% Availability', grid = True,figsize=(20, 10), color = 'g')
plt.axhline(y = df['% Availability'].mean(), linewidth=2, color='r', ls = 'dashed')


#check outliers
x = df['% Availability'] < 70
df[x]

#plot multiple outliers together
df.plot(kind = 'line', x='Time', 
        y=['Mdn DNS (ms)',
           'Avg Time To First Byte (ms)',
           'Mdn Render Start (ms)'], 
        label=['Mdn DNS (ms)',
               'Avg Time To First Byte (ms)', 
               'Mdn Render Start (ms)'],
                    
           grid = True,figsize=(20, 10))


#Bar Chart
labels = ('Image', 'Script', 'Css')
y_pos = np.arange(len(labels))
sizes = [df['Avg Image Bytes'].mean()*0.001, 
         df['Avg Script Bytes'].mean()*0.001, 
         df['Avg Css Bytes'].mean()*0.001]
plt.barh(y_pos, sizes, align='center', alpha=0.5)
plt.yticks(y_pos, labels)
plt.xlabel('sizes kb')
plt.title('Avg Content Composition')

#Pie Chart
plt.pie(sizes,labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.show()

 
#Some Test don't need to run
#df.describe()
#type(df.Time[1])
#len(df)
#df.Time[1]
#print(':00 PM' in df.Time[i])
#print(df.Time[190].replace(":00 PM", ""))
#df.columns

#(df['Avg Image Bytes'].mean()*0.001 + df['Avg Script Bytes'].mean()*0.001 + df['Avg Css Bytes'].mean()*0.001)*0.001