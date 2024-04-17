import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from scipy.stats import bernoulli

# Read CSV file into DataFrame df
df = pd.read_csv('ai_job_data.csv', index_col=0)

#calculating the average Ai impact for each job in dataset
df["AI Impact"] = df["AI Impact"].str.rstrip("%").astype("int") / 100
average_ai_impact = df["AI Impact"].mean(axis=0)

print(average_ai_impact * 100)

#calculating the standard deviation for each job being replaced by AI
std = df["AI Impact"].std()

print(std)

# Plotting the graph of job titles and AI impact relativeness
first_30_job_titles = df.index[:30] 
first_30_AI_workplace_impact_ratio = df["AI_Workload_Ratio"].head(30)

# Create a bar plot
plt.bar(first_30_job_titles, first_30_AI_workplace_impact_ratio)

# Rotate x-axis labels for better readability
plt.xticks(rotation=90)

# Add labels and title
plt.xlabel('Job Titles')
plt.ylabel('AI Impact Ratio')
plt.title('AI Impact on Jobs')

# Show the plot
plt.show()

# Probability of AI impact on the all unique domains
AI_rate = average_ai_impact
unique_domain_count = df["Domain"].nunique() # counts the different types of domains

# Bernoulli distrubtion showing the AI rate of all the domains in the dataset
data = bernoulli.rvs(size = unique_domain_count , p = AI_rate)

#Visualizing the results
sb.set_style('whitegrid')
sb.displot(data, discrete=True, shrink=.8 , color = 'k')
plt.title('Probability of AI Impact on Domain')
plt.ylabel('Number of domains')
plt.xlabel('Probability of domain')
plt.show()

#I believe the data appears to be uniformally distributed
data = df["AI Impact"].head(30)

# Plot the density plot for your dataset
pd.DataFrame(data).plot(kind='density')

# Customize the plot (optional)
plt.xlabel('AI Impact')
plt.ylabel('Density')
plt.title('Density Plot of AI Impact')

# Show the plot
plt.show()

# graph that shows the domain and their AI score
grouped_data = df.groupby("Domain")["AI Impact"].mean().head(30)

# Extracting data
first_30_domain = grouped_data.index
first_30_AI = grouped_data.values

# Plotting
plt.plot(first_30_domain, first_30_AI)
plt.xlabel('Domain')
plt.xticks(rotation=90)
plt.ylabel('Average AI Score')

plt.show()