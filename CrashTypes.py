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


# Grouping the data by 'First Crash Type' and calculating the mean of 'Injuries Total' for each category
mean_injuries_per_type = crashes_df.groupby('FIRST_CRASH_TYPE')['INJURIES_TOTAL'].mean().sort_values()


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

# Last chart

# Extracting "First Crash Type" and "Damage" columns
first_crash_type_damage = crashes_df[["FIRST_CRASH_TYPE", "DAMAGE"]]

# Grouping by "Damage" and counting occurrences
damage_counts = first_crash_type_damage.groupby("DAMAGE").size()

# Sorting by damage counts in descending order
damage_counts = damage_counts.sort_values(ascending=False)

# Convert damage_counts Series to DataFrame
damage_counts_df = damage_counts.reset_index(name='Number of Crashes')

fig = px.bar(damage_counts_df, 
             x='DAMAGE', 
             y='Number of Crashes', 
             title='Number of Crashes by Damage Amount',
             labels={'DAMAGE': 'Average Damage Cost', 'Number of Crashes': 'Number of Crashes'},
             height=600,
             width=800)

# Rotate x-axis labels for better readability
fig.update_layout(xaxis=dict(tickangle=-45))

# Show the interactive plot
fig.show()