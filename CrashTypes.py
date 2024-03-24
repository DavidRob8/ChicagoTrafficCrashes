#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import libraries
import pandas as pd
import plotly.graph_objs as go 
import plotly.express as px 
import dash
from dash import Dash, dcc, html, Input, Output


# In[2]:


# Assigning variable to csv path
file_path = '2022-2023.csv'


# In[3]:


# Reading in csv file as Pandas DataFrame
init_data_df = pd.read_csv(file_path)
init_data_df.head()


# In[4]:


init_data_df['TRAFFIC_CONTROL_DEVICE'].unique()


# In[5]:


delete_values = ['UNKNOWN', 'OTHER', 'OTHER REG. SIGN']
mask = init_data_df['TRAFFIC_CONTROL_DEVICE'].isin(delete_values)
filtered_init_data_df = init_data_df[~mask]
len(filtered_init_data_df)


# In[6]:


# Deleting rows with no longitude or latitude values
clean_filtered_df = filtered_init_data_df.dropna(subset=['LATITUDE', 'LONGITUDE', 'MOST_SEVERE_INJURY'])
len(clean_filtered_df)


# In[7]:


clean_filtered_df['MOST_SEVERE_INJURY'].unique()


# In[8]:


delete_values = ['NO INDICATION OF INJURY', 'REPORTED, NOT EVIDENT', 'NONINCAPACITATING INJURY']
mask = clean_filtered_df['MOST_SEVERE_INJURY'].isin(delete_values)
final_data = clean_filtered_df[~mask]
print(len(final_data))
final_data.head()


# In[9]:


final_data['CRASH_DATE'] = pd.to_datetime(final_data['CRASH_DATE'])
final_data.head()


# In[10]:


final_data.info()


# In[11]:


final_data['CATEGORIES'] = ''

final_data.loc[(final_data['MOST_SEVERE_INJURY'] == 'FATAL') & (final_data['TRAFFIC_CONTROL_DEVICE'] != 'NO CONTROLS'), 'CATEGORIES'] = 'FATAL with Device'
final_data.loc[(final_data['MOST_SEVERE_INJURY'] == 'FATAL') & (final_data['TRAFFIC_CONTROL_DEVICE'] == 'NO CONTROLS'), 'CATEGORIES'] = 'FATAL without Device'
final_data.loc[(final_data['MOST_SEVERE_INJURY'] == 'INCAPACITATING INJURY') & (final_data['TRAFFIC_CONTROL_DEVICE'] != 'NO CONTROLS'), 'CATEGORIES'] = 'INCAPACITATING INJURY with Device'
final_data.loc[(final_data['MOST_SEVERE_INJURY'] == 'INCAPACITATING INJURY') & (final_data['TRAFFIC_CONTROL_DEVICE'] == 'NO CONTROLS'), 'CATEGORIES'] = 'INCAPACITATING INJURY without Device'

final_data.head()


# In[12]:


final_data.info()


# In[13]:


final_data.to_csv('scatter_mapbox_data.csv', index=False)


# In[13]:


categories = final_data['CATEGORIES'].unique()
categories


# In[14]:


# Initialize the Dash app
app = dash.Dash(__name__)


# In[15]:


# Extract unique years and months from the CRASH_DATE column
# Manually define unique months for correct order in dropdown menu
unique_years = final_data['CRASH_DATE'].dt.year.unique()
unique_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


# In[16]:


# Create list of dictionaries to give user option to select data for full year
year_options = [{'label': 'All of 2022', 'value': 'All of 2022'},
                {'label': 'All of 2023', 'value': 'All of 2023'}]


# In[17]:


# Create the layout using html.Div 
app.layout = html.Div([
    # H1 element for the title
    html.H1("Impact of Traffic Control Devices on Car Accidents",  style={'width': '500px', 'white-space': 'pre-wrap'}),
    html.Div([
        html.Div([
            # Creating dropdown for year for user to select
            html.Label("Select Year:", style={'font-size': '14px'}),
            dcc.Dropdown(
                id='year-dropdown',
                # This creates options to select a year along with a month or a full year (2022 or 2023)
                options=[{'label': str(year), 'value': year} for year in unique_years] + year_options,
                # default value is "All of 2022"
                value=year_options[0]['value'],
                # Styled by using CSS for positioning in the map and font size
                style={'width': '150px', 'font-size': '14px'}
            )
        ], style={'position': 'absolute', 'top': '10px', 'right': '180px'}),
        
        html.Div([
            # Creating dropdown for month for user to select
            html.Label("Select Month:", style={'font-size': '14px'}),
            dcc.Dropdown(
                id='month-dropdown',
                options=[{'label': month, 'value': month} for month in unique_months],
                value=unique_months[0],
                style={'width': '150px', 'font-size': '14px'}
            )
        ], style={'position': 'absolute', 'top': '10px', 'right': '10px'}),
    ], style={'position': 'relative', 'height': '100px'}),    
    # Create a graph for displaying the map
    dcc.Graph(id='map-graph')
])
    


# In[18]:


# Define callback to update month dropdown options based on selected year
@app.callback(
    dash.dependencies.Output('month-dropdown', 'options'),
    [dash.dependencies.Input('year-dropdown', 'value')])

# defined a function that takes selected year as input and returns the month optioms
def update_month_options(selected_year):
    if selected_year in ['All of 2022', 'All of 2023']:
        # If "All of 2022" or "All of 2023" is selected, return an empty list for month options
        return []
    else:
        # Return the options for all months if "All of 2022" or "All of 2023" is NOT selected
        return [{'label': month, 'value': month} for month in unique_months]

# Define callback to update the map based on user selection
@app.callback(
    dash.dependencies.Output('map-graph', 'figure'),
    [dash.dependencies.Input('year-dropdown', 'value'),
     dash.dependencies.Input('month-dropdown', 'value')]
)

# Function that takes selected year and selected month as input
def update_map(selected_year, selected_month):
    # Convert month name to numeric values
    month_to_num = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
                    'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}

    # Check if "All of 2022" or "All of 2023" is selected
    if selected_year in ['All of 2022', 'All of 2023']:
        # Filter the DataFrame for the entire year
        # Splits the selected year string into a list of strings, whitespace is delimiter, selects last element of that list
        filtered_df = final_data[final_data['CRASH_DATE'].dt.year == int(selected_year.split()[-1])]
    else:
        # Convert selected year to integer and filter df based on selected year and month
        selected_year = int(selected_year)
        selected_month_num = month_to_num[selected_month]
        filtered_df = final_data[(final_data['CRASH_DATE'].dt.year == selected_year) & 
                                 (final_data['CRASH_DATE'].dt.month == selected_month_num)]

    # Create map using Plotly Express
    fig = px.scatter_mapbox(filtered_df, lat='LATITUDE', lon='LONGITUDE', zoom=10)

    # Define categories and colors
    categories = sorted(filtered_df['CATEGORIES'].unique())
    colors = ['red', 'blue', 'yellow', 'green']
    
    # Add markers for each category
    for category, color in zip(categories, colors):
        # Filtering based on selected category
        filtered_category_df = filtered_df[filtered_df['CATEGORIES'] == category]
        # Grab count to show in tracing
        count = len(filtered_category_df)
        # Naming the tracing attributes by categories and by the count of those categories
        name = f"{category}: {count}"
        # List comprehension to iterate through all rows of df to pull date and device info
        hover_text = [f"CRASH_DATE: {row['CRASH_DATE']}<br>TRAFFIC_CONTROL_DEVICE: {row['TRAFFIC_CONTROL_DEVICE']}" for _, row in filtered_category_df.iterrows()]
        #Creating the scatter mapbox
        fig.add_scattermapbox(
            lat=filtered_category_df['LATITUDE'],
            lon=filtered_category_df['LONGITUDE'],
            mode='markers',
            name=name,
            marker=dict(color=color, size=10),
            text=hover_text,
            hoverinfo='text'
        )

    # Defining type of map and margins    
    fig.update_layout(mapbox_style="carto-positron")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    return fig

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)


# In[ ]:





# In[ ]:





# In[ ]:




