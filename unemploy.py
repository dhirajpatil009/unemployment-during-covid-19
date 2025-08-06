import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("unemploy.csv")
df.head()

df.info()
df.describe()
df.isnull().sum()

df.columns = df.columns.str.strip()

df[' Date'] = pd.to_datetime(df['Date'])

print(df.head())

# Line plot of Unemployment Rate over time
plt.figure(figsize=(10, 6))
sns.lineplot(x='Date', y='Estimated Unemployment Rate (%)', data=df)
plt.title('Unemployment Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.grid(True)
plt.show()

# Bar plot by State
plt.figure(figsize=(12, 8))
state_avg = df.groupby('Region')['Estimated Unemployment Rate (%)'].mean().sort_values()
state_avg.plot(kind='barh', color='skyblue')
plt.title('Average Unemployment Rate by State')
plt.xlabel('Average Unemployment Rate (%)')
plt.show()

covid_period = df[(df['Date'] >= '2020-03-01') & (df['Date'] <= '2021-12-31')]
sns.lineplot(data=covid_period, x='Date', y='Estimated Unemployment Rate (%)', hue='Region')
plt.title('Unemployment During COVID-19')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

