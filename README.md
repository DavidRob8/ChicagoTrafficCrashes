## Project 3: City of Chicago Car Crashes
### UC Berkeley Data Analytics and Visualization Bootcamp 2023-24
Group 4: Julio Dela Cruz, Everardo Garcia, Amanpreet Kaur, David Robles, Dylan Sui

Project Website URL: https://davidrob8.github.io/ChicagoTrafficCrashes/


## Description

The purpose of this project is to analyze the data regarding car crashes in the City of Chicago and to create visualizations that will help us answer the following questions:

1. How does lighting affect the amount of car crashes? (Julio)
2. What are the areas in Chicago with the most accidents and what are the primary reasons? (Everardo)
3. How does the presence of traffic control devices affect car crash rates and the incidence of severe injuries or fatalities? (David)
4. Which accident type on average has the highest injury count and what is the average cost of associated damages? (Dylan)
5. Are crash crashes more prevalent during certain days of week or months of year? (Aman)


## Data Cleaning

The initial dataset that we obtained from the source was massive. It contained data of car crashes in the city of Chicago stemming from back in 2015. There were over 800,000 rows in the csv file that we read into our Jupyter Notebook file. Due to the size, we narrowed down the data to only include car crashes from 2022 and 2023. This left our dataset with 219,125 rows. We dropped 27 columns that we deemed irrelevent to the questions we were asking of the dataset. We then converted the "CRASH_DATE" column to datetime to be able to filter dates properly. This was the initial dataset that we started with to create our visualizations for all but one. The map shown under the Map Data tab in the webpage uses live data from https://dev.socrata.com/foundry/data.cityofchicago.org/85ca-t3if.


## Instructions

Click on this link to go to our website. The home page has a summary of our project. There are five tabs that will take you to the different visualizations: Lighting and Weather, Map Data, Traffic Control Devices Map, Average Costs, and Monthly Data. The five questions listed above were answered with visualizations created with different programming languages, Python and JavaScript, as well as several different libraries. Below are instructions on how to use and interact with each visualization used to answer each corresponding question.

#### 1. Lighting & Weather: How does lighting affect the amount of car crashes? (Julio)
The purpose of these barplot visualizations is to examine the number of crashes depending on lighting and weather conditions in Chicago. It can give the viewer insight as to what certain type of conditions lead to the most amount of crashes. The barplots themselves have various options to further examine the data. Using the drop down menu and the legend on the right hand side, they can filter out data based on what they want to see. Hovering the cursor over the bar plots will also allow the user to see the amount of crashes that a specific condition has. 

#### 2. Map Data: What are the areas in Chicago with the most accidents and what are the primary reasons? (Everardo)

The purpose of this map visualization is to show the areas of Chicago with the most car accidents, while also finding the most common causes. This map uses live data from https://dev.socrata.com/foundry/data.cityofchicago.org/85ca-t3if.

- At the top right of the screen we have two ways to view our map (Street Map and Satellite). The user can select one at a time.
- In the same white box but a little lower, we have three other ways to display our data, you can choose one, two or three at a time. It's up to you. Each mark on the map is a car accident that occurred in the previous 4 or 5 days. If you click on one of those marks, you will be able to see information about this accident (location, date of accident, date of accident, cause of accident, lighting conditions, and weather conditions).
- In the lower right part we can see all the Accidents Cause arranged in descending order (from most common to least common).
- In the lower left part we can see the data we are seeing from what day until what day is this data.


#### 3. Traffic Control Devices Map: How does the presence of traffic control devices affect car crash rates and the incidence of severe injuries or fatalities? (David)

Using Plotly Express and Dash in a Jupyter Notebook file, I created a scatter mapbox to show and compare serious car accidents (only car accidents that resulted in fatal or incapacitating injury) with or without a traffic control device (i.e. traffic signal, yield sign, school zone, etc.). The idea of the scatter mapbox is to see whether or not traffic control devices have had an effect on serious car accidents. The data set used is for car crashes in the city of Chicago for the years 2022 and 2023. Since I used Python, I used PythonAnywhere to deploy the app to a webpage.

The map will display the city of Chicago, with markers representing car crashes. As shown in the legend, red markers represent accidents that were fatal with a device present, blue markers represent accidents that were fatal without a device present, yellow markers represent accidents that caused incapacitating injury with a device present, and green markers represent accidents that caused incapacitating injury without a device present. The legend also shows the count for each type of crash for the selected timeframe. There are two dropdown menus: "Select Year" and "Select Month". To view accidents for all of 2022 or all of 2023, select "All of 2022" or "All of 2023", respectively, in the "Select Year" dropdown menu. To view accidents by month, select "2022" or "2023" in the "Select Year" dropdown menu, and choose a month to view in the "Select Month" dropdown menu. You can also hover over the markers to see the crash date and the traffic control device present, if any. 


#### 4. Average Incident Information: Which accident type on average has the highest injury count and what is the average cost of associated damages? (Dylan)

Using Pandas and Plotly express in a Jupyter Notebook / VS Code file, I created two bar charts. One bar chart highlighted the Crash Type, which is the type of incident that occured. For example, if it was a rear end collusion, side swipe, or parked car. Within this chart I took the average number of injured individuals per accident and organized the chart by the highest to lowest numbered of injured inidividuals. From this chart we could determine which accidents are the most harmful. By hovering your mouse over each line of the chart you are also able to see additional information regarding each data point. 

The second chart was a basic count of the damage cost per accident. The three cost groups were "$500 or less", "$501 - $1500", and "Over $1,500". Since the raw data didn't specify exactly how much property damage or collision damage occured, the Chicago Police Department most likely estimated the amounts per incident. With over 150K accidents costing "Over $1,500" we can safely assume that if you were to be in an accident the damages an individual would have to pay for would be greater than $1,500. The file was created with Plotly Express and allows the user to gather more information from each bar chart by hovering their mouse over the respective chart. 

   
#### 5. Monthly Data: Are crash crashes more prevalent during certain days of week or months of year? (Aman)
   
The working dataset was obtained from data_cleaning.ipynb as csv file and converted into .json format using csvtojson.py file, separated by each year. Within VS Code, I utilized D3.js library in JavaScript and Plotly.js in order to extract the car crash data by each month and each weekday over 2022 and 2023; and created two data visualizations in web browsers that can be launched from the HTML file. Users can access the console window by right-clicking inside the generated web browser page and selecting ‘Inspect’ to bring up the console log. This will help verify the .js code is running without any issue, and should auto-populate with 2022-2023 Total Crashes by Month and 2022-2023 Total Crashes by Weekday data. Concurrently, webpage should display one scatter plot and one bar chart visualizing this accrued data, respectively. Both visuals show the number of car crashes that occurred in Chicago between 2022 and 2023. Users can select/deselect the years individually from the legend accompanying each graph to look at the car crash data over one year alone. By hovering over each timepoint, users may also view the total number of car crashes displayed in pop-ups. These visuals help assess during which particular weekday(s) or month(s) did more car crashes occur over this two-year period. 


## Ethical Considerations

The data that we used for this project is crash data within the City of Chicago limits and under the jurisdiction of the Chicago Police Department (CPD). The actual data shown is extracted from the electronic reporting system (E-Crash) that is used at the CPD, but it excludes any personally identifiable information. Given that this is a public dataset API, we were made more comfortable using it for our project knowing that personal information about sensitive occurences such as car accidents were excluded. Another ethical consideration we looked at was that Socrata, the creator of this Chicago API, was acquired by Tyler Technologies in 2018 and is now the Data and Insights division of Tyler. The platform is still powered by the same software formerly known as Socrata, but there are references to Data & Insights. As we discussed in class, when companies get sold or merged, the ownership and the transferring of data creates risk that can be tricky to navigate. However, as mentioned previously, we were comfortable using this data set as the primary purpose of the data source is for users to explore the data.


## Data Limitations

- Data from E-Crash are available for some police districts in 2015, but citywide data are not available until September 2017.
- About half of all crash reports, mostly minor crashes, are self-reported at the police district by the driver(s) involved and the other half are recorded at the scene by the police officer responding to the crash.
- Many of the crash parameters, including street condition data, weather condition, and posted speed limits, are recorded by the reporting officer based on best available information at the time, but many of these may disagree with posted information or other assessments on road conditions.
- If any new or updated information on a crash is received, the reporting officer may amend the crash report at a later time.
- A traffic crash within the city limits for which CPD is not the responding police agency, typically crashes on interstate highways, freeway ramps, and on local roads along the City boundary, are excluded from this dataset.

## Sources

https://dev.socrata.com/foundry/data.cityofchicago.org/85ca-t3if

https://data.cityofchicago.org/resource/85ca-t3if.json


## Built With:

Mapping:  

https://leafletjs.com/

https://plotly.com/python/scattermapbox/

https://dash.plotly.com/




