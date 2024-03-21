## Project 3: City of Chicago Car Crashes
### UC Berkeley Data Analytics and Visualization Bootcamp 

The purpose of this project is to analyze the data regarding car crashes in the City of Chicago and to create visualizations that will help us answer the following questions:

1. What are the areas in Chicago with the most accidents and what are the primary reasons? (Everardo)
2. How does lighting affect the amount of car crashes? (Julio)
3. How does the presence of traffic control devices affect car crash rates and the incidence of severe injuries or fatalities? (David)
4. Are crash crashes more prevalent during certain days of week or months of year? (Aman)
5. What is the most common type of accident, and what is the average cost of associated damages? (Dylan)

## Data Cleaning
The initial dataset that we obtained from the source was massive. It contained data of car crashes in the city of Chicago stemming from back in 2015. There were over 800,000 rows in the csv file that we read into our Jupyter Notebook file. Due to the size, we narrowed down the data to only include car crashes from 2022 and 2023. This left our dataset with 219,125 rows. We dropped 27 columns that we deemed irrelevent to the questions we were asking of the dataset. We then converted the "CRASH_DATE" column to datetime to be able to filter dates properly. This was the initial dataset that we started with to create our visuals.

## Instructions
The five questions listed above were answered with visualizations created with different programming languages, Python and JavaScript, as well as several different libraries. Below are instructions on how to use and interact with each visualization used to answer each corresponding question.

1. What are the areas in Chicago with the most accidents and what are the primary reasons? (Everardo)
2. How does lighting affect the amount of car crashes? (Julio)
3. How does the presence of traffic control devices affect car crash rates and the incidence of severe injuries or fatalities? (David)

Using Plotly Express and Dash in a Jupyter Notebook file, I created a scatter mapbox to show and compare serious car accidents (only car accidents that resulted in fatal or incapacitating injury) with or without a traffic control device (i.e. traffic signal, yield sign, school zone, etc.). The idea of the scatter mapbox is to see whether or not traffic control devices have had an effect on serious car accidents. The data set used is for car crashes in the city of Chicago for the years 2022 and 2023. The map will display the city of Chicago, with markers representing car crashes. As shown in the legend, red markers represent accidents that were fatal with a device present, blue markers represent accidents that were fatal without a device present, yellow markers represent accidents that caused incapacitating injury with a device present, and green markers represent accidents that caused incapacitating injury without a device present. The legend also shows the count for each type of crash for the selected timeframe. There are two dropdown menus: "Select Year" and "Select Month". To view accidents for all of 2022 or all of 2023, select "All of 2022" or "All of 2023", respectively, in the "Select Year" dropdown menu. To view accidents by month, select "2022" or "2023" in the "Select Year" dropdown menu, and choose a month to view in the "Select Month" dropdown menu. You can also hover over the the markers to see the crash date and the traffic control device present, if any. 
   
5. Are crash crashes more prevalent during certain days of week or months of year? (Aman)
6. What is the most common type of accident, and what is the average cost of associated damages? (Dylan)


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

## Built With:

Mapping:  https://plotly.com/python/scattermapbox/, https://dash.plotly.com/


Screenshots of relevant, "inspiring" visualizations that show your creative ideas:
![image](https://github.com/DavidRob8/ChicagoTrafficCrashes/assets/150605617/18dec27b-5701-4904-b21e-b9fda25a4170)
![image](https://github.com/DavidRob8/ChicagoTrafficCrashes/assets/150605617/b07de6c0-fa15-408b-a128-fe9eb8bc899d)
![image](https://github.com/DavidRob8/ChicagoTrafficCrashes/assets/150605617/83c24aaa-a50b-476c-94a4-01fc2fc6dcc6)
![image](https://github.com/DavidRob8/ChicagoTrafficCrashes/assets/150605617/c6a8fd41-dff2-4c9e-b16d-873a3c21f67a)




