import pandas as pd
import matplotlib.pyplot as plt

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
first_30_job_titles = df.index[:30]  # Assuming the job titles are in the index
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

# Probability of AI impact