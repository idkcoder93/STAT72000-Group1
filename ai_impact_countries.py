import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import bernoulli

#read CSV file into DataFrame df
ai_index_df = pd.read_csv('ai_index_data.csv', index_col=0)

#print the first few rows to check the data
print(ai_index_df.head())

#calculate and print the mean for each numeric column
print("Mean of each metric:")
means = ai_index_df.mean(numeric_only=True)
print(means)

#calculate and print the standard deviation for each numeric column
print("\nStandard deviation of each metric:")
std_devs = ai_index_df.std(numeric_only=True)
print(std_devs)

#further statistical measures can also be calculated if we really wanted
#calculating minimum values
print("\nMinimum values:")
min_vals = ai_index_df.min(numeric_only=True)
print(min_vals)

#calculating maximum values
print("\nMaximum values:")
max_vals = ai_index_df.max(numeric_only=True)
print(max_vals)

#descriptive statistics summary
print("\nDescriptive statistics summary:")
print(ai_index_df.describe())

#talent score by country
plt.figure(figsize=(12, 8))
sns.barplot(x=ai_index_df.index, y='Talent', data=ai_index_df.sort_values('Talent', ascending=False))
plt.xticks(rotation=90)
plt.xlabel('Country')
plt.ylabel('Talent Score')
plt.title('Talent Score by Country')
plt.tight_layout()
plt.show()

#histogram of Talent to show distribution
plt.figure(figsize=(10, 6))
sns.histplot(ai_index_df['Talent'], kde=True)
plt.xlabel('Talent Score')
plt.ylabel('Frequency')
plt.title('Distribution of Talent Score')
plt.show()

#scatter plot of research vs. total score with country annotations
plt.figure(figsize=(10, 6))
for i, point in ai_index_df.iterrows():
    plt.scatter(point['Research'], point['Total score'])
    plt.text(point['Research'], point['Total score'], i)

plt.xlabel('Research Score')
plt.ylabel('Total AI Score')
plt.title('Correlation between Research and Total AI Score')
plt.show()

#scatter plot of government strategy vs. total score with country annotations
plt.figure(figsize=(10, 6))
for i, point in ai_index_df.iterrows():
    plt.scatter(point['Government Strategy'], point['Total score'])
    plt.text(point['Government Strategy'], point['Total score'], i)     
plt.xlabel('Government Strategy Score')
plt.ylabel('Total AI Score')
plt.title('Correlation between Government Strategy and Total AI Score')
plt.show()


# Calculate the mean AI impact for each category
ai_index_df = pd.read_csv('ai_index_data.csv', index_col=0)
categories = ['Talent', 'Infrastructure', 'Operating Environment', 'Research', 'Development', 'Government Strategy', 'Commercial']
mean_ai_impact_by_category = ai_index_df[categories].mean()

plt.figure(figsize=(10, 6)) 
mean_ai_impact_by_category.plot(kind='bar')
plt.xlabel('Category')
plt.ylabel('Mean AI Impact')
plt.title('Mean AI Impact by Category')
plt.show()