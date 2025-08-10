import matplotlib as plt
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv(r'C:\Users\tanvi\OneDrive\Desktop\Streamlit\weather\weather.csv')
print(df.head())
print(df.columns)
plt.plot(df.index[:10],df['MaxTemp'].iloc[:10],linestyle = '-',color = 'blue', marker = 'o', markersize = 5)
plt.xlabel('Days')
plt.ylabel('Max Temperature')
plt.title('Max Temperature Trend Over 10 Days')
plt.legend()
plt.show()
plt.bar(df.index[:10],df['Rainfall'].iloc[:10], color='blue', width=0.5)
plt.xlabel('Days')
plt.ylabel('Rainfall')
plt.title('Rainfall Over 10 Days')
plt.show()
plt.hist(df['Humidity3pm'].iloc[:10], bins=10, linewidth=0.5, edgecolor="white")
plt.xlabel('Humidity at 3 PM')
plt.ylabel('Frequency') 
plt.show()