import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

csv_path = Path("2022-2023.csv")

crashes_df = pd.read_csv(csv_path, low_memory=False)

crashes_df.dtypes

crash_type_column = crashes_df["FIRST_CRASH_TYPE"]
crash_type_column

crash_type_counts = crash_type_column.value_counts()

print(crash_type_counts)

crash_type_counts = crash_type_column.value_counts()

# Plotting the bar chart
crash_type_counts.plot(kind='bar')

# Adding title and labels
plt.title('Crash Type Counts')
plt.xlabel('Crash Type')
plt.ylabel('Count')

# Show the plot
plt.show()


# Calculate crash type counts
crash_type_counts = crash_type_column.value_counts()

# Create a DataFrame with crash types and their corresponding counts
crash_type_counts_df = pd.DataFrame({'Crash Type': crash_type_counts.index, 'Count': crash_type_counts.values})

print(crash_type_counts_df)


first_crash_type_damage = crashes_df[["FIRST_CRASH_TYPE", "DAMAGE"]]

# Displaying the extracted data
print(first_crash_type_damage)


first_crash_type_damage = crashes_df[["FIRST_CRASH_TYPE", "DAMAGE"]]

# Displaying the extracted data
print(first_crash_type_damage)

first_crash_type_damage.head()




# Assuming crashes_df is your DataFrame

# Extracting "First Crash Type" and "Damage" columns
first_crash_type_damage = crashes_df[["FIRST_CRASH_TYPE", "DAMAGE"]]

# Grouping by "Damage" and counting occurrences
damage_counts = first_crash_type_damage.groupby("DAMAGE").size()

# Sorting by damage counts in descending order
damage_counts = damage_counts.sort_values(ascending=False)

# Plotting the bar chart
plt.figure(figsize=(10, 6))
damage_counts.plot(kind='bar', color='skyblue')
plt.title('Number of Crashes by Damage Type')
plt.xlabel('Damage Type')
plt.ylabel('Number of Crashes')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# Assuming crashes_df is your DataFrame

# Selecting relevant columns for correlation analysis
selected_columns = ['FIRST_CRASH_TYPE', 'INJURIES_TOTAL']
correlation_data = crashes_df[selected_columns]

# Encoding categorical variables (First Crash Type) into numerical values
correlation_data = pd.get_dummies(correlation_data, columns=['FIRST_CRASH_TYPE'], drop_first=True)

# Calculating correlation matrix
correlation_matrix = correlation_data.corr()

# Extracting correlation values for 'INJURIES_TOTAL' column
injuries_total_correlation = correlation_matrix['INJURIES_TOTAL']

# Sorting correlation values in descending order
injuries_total_correlation = injuries_total_correlation.abs().sort_values(ascending=False)

print("Correlation between 'INJURIES_TOTAL' and 'FIRST_CRASH_TYPE' categories:")
print(injuries_total_correlation)


# Grouping the data by 'First Crash Type' and calculating the mean of 'Injuries Total' for each category
mean_injuries_per_type = crashes_df.groupby('FIRST_CRASH_TYPE')['INJURIES_TOTAL'].mean().sort_values()

# Plotting the bar chart
plt.figure(figsize=(12, 8))
mean_injuries_per_type.plot(kind='barh', color='skyblue')
plt.title('Average Injuries Total by First Crash Type')
plt.xlabel('Average Injuries Total')
plt.ylabel('First Crash Type')
plt.grid(axis='x')
plt.tight_layout()
plt.show()

# Assuming crashes_df is your DataFrame

# Grouping the data by 'First Crash Type' and calculating the mean of 'Injuries Total' for each category
mean_injuries_per_type = crashes_df.groupby('FIRST_CRASH_TYPE')['INJURIES_TOTAL'].mean().sort_values().reset_index()

# Plotting the bar chart using Plotly
fig = px.bar(mean_injuries_per_type, 
             x='INJURIES_TOTAL', 
             y='FIRST_CRASH_TYPE', 
             orientation='h', 
             title='Average Injuries Total by First Crash Type',
             labels={'INJURIES_TOTAL': 'Average Injuries Total', 'FIRST_CRASH_TYPE': 'First Crash Type'},
             height=600,
             width=800)

fig.show()