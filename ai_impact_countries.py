import pandas as pd                 #importing the pandas library for data manipulation
import matplotlib.pyplot as plt     #importing the matplotlib library for creating visualizations
import seaborn as sns               #importing the seaborn library for enhanced visualization styles
from scipy.stats import bernoulli   #importing the bernoulli function for statistical computations

#read the CSV file into a DataFrame, setting the first column as the index
ai_index_df = pd.read_csv('ai_index_data.csv', index_col=0)

#print the first few rows of the DataFrame to verify the data is read correctly
print(ai_index_df.head())

#calculate the mean for each numeric column and print it
print("Mean of each metric:")
means = ai_index_df.mean(numeric_only=True)
print(means)

#calculate the standard deviation for each numeric column and print it
print("\nStandard deviation of each metric:")
std_devs = ai_index_df.std(numeric_only=True)
print(std_devs)

#further statistical measures can also be calculated if we really wanted:
#calculate the minimum values for numeric columns and print them
print("\nMinimum values:")
min_vals = ai_index_df.min(numeric_only=True)
print(min_vals)

#calculate the maximum values for numeric columns and print them
print("\nMaximum values:")
max_vals = ai_index_df.max(numeric_only=True)
print(max_vals)

#print a summary of descriptive statistics for the DataFrame
print("\nDescriptive statistics summary:")
print(ai_index_df.describe())


#creating a barplot of "Talent" scores by country
plt.figure(figsize=(12, 8))         #setting figure size
sns.barplot(x=ai_index_df.index, y='Talent', data=ai_index_df.sort_values('Talent', ascending=False))       #sorting the data by "Talent" in descending order
plt.xticks(rotation=90)             #rotating the x-axis labels for better readability
plt.xlabel('Country')               #setting the x-axis label
plt.ylabel('Talent Score')          #setting the y-axis label
plt.title('Talent Score by Country')        #setting the title of the plot
plt.tight_layout()                  #adjust the layout of the plot
plt.show()                          #display the plot


#creating a histogram of the "Talent" scores to show the distribution
plt.figure(figsize=(10, 6))             #setting figure size
sns.histplot(ai_index_df['Talent'], kde=True)           #plotting the histogram with a kernel density estimate
plt.xlabel('Talent Score')              #setting the x-axis label
plt.ylabel('Frequency')                 #setting the y-axis label
plt.title('Distribution of Talent Score')       #setting the title of the plot
plt.show()                              #display the plot


#scatter plot of "Research" vs. "Total score" with annotations for each country
plt.figure(figsize=(10, 6))             #setting figure size
for i, point in ai_index_df.iterrows():     #iterating through each row in the DataFrame
    plt.scatter(point['Research'], point['Total score'])        #plotting scatter points
    plt.text(point['Research'], point['Total score'], i)        #annotating each point with country name

plt.xlabel('Research Score')        #setting the x-axis label
plt.ylabel('Total AI Score')        #setting the y-axis label
plt.title('Correlation between Research and Total AI Score')    #setting the title of the plot
plt.show()                          #display the plot


#scatter plot of "Government Strategy" vs. "Total score" with annotations for each country
plt.figure(figsize=(10, 6))                 #setting figure size
for i, point in ai_index_df.iterrows():     #iterating through each row in the DataFrame
    plt.scatter(point['Government Strategy'], point['Total score'])         #plotting scatter points
    plt.text(point['Government Strategy'], point['Total score'], i)         #annotating each point with country name
plt.xlabel('Government Strategy Score')     #setting the x-axis label
plt.ylabel('Total AI Score')                #setting the y-axis label
plt.title('Correlation between Government Strategy and Total AI Score')     #setting the title of the plot
plt.show()                          #display the plot


#list of categories to analyze
categories = ['Talent', 'Infrastructure', 'Operating Environment', 'Research', 
              'Development', 'Government Strategy', 'Commercial']

#calculate the mean AI impact for each category
mean_ai_impact_by_category = ai_index_df[categories].mean()

#set the figure size for the plot
plt.figure(figsize=(14, 8)) 

#create a bar plot of the mean AI impact by category
mean_ai_impact_by_category.plot(kind='bar', rot=45)         #plotting the mean AI impact as a bar chart with rotated x-axis labels for readability

#set the labels and title for the plot
plt.xlabel('Category', labelpad=20)             #label for the x-axis with padding for better spacing
plt.ylabel('Mean AI Impact', labelpad=20)       #label for the y-axis with padding for better spacing
plt.title('Mean AI Impact by Category')         #title for the plot

#adjust the layout to prevent the x-axis labels and other elements from being cut off
plt.tight_layout()

#display the bar plot
plt.show()
