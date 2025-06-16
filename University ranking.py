import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:\python\cwurData.csv')

universities_by_country = df.groupby('country')['institution'].nunique().reset_index()
universities_by_country = universities_by_country.rename(columns={'institution': 'total_universities'})


# Plot
plt.figure(figsize=(12, 8))
sns.barplot(x='country', y='total_universities', data=universities_by_country, palette='viridis')

plt.title('Total Number of Universities by Country')
plt.xlabel('Country')
plt.ylabel('Total Universities')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Group by country and sum patents
patents_by_country = df.groupby('country')['patents'].sum().reset_index()
plt.figure(figsize=(12, 8))
sns.barplot(x='country', y='patents', data=patents_by_country, palette='viridis')

plt.title('Total Number of Patents by Country')
plt.xlabel('Country')
plt.ylabel('Total Patents')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
