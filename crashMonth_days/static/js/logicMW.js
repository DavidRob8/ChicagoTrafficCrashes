// Get the url endpoint for 2022 and 2023
const url_2022 = "2022.json";
const url_2023 = "2023.json";

function mainCrashesByMonth(url, year) {
    // Fetch the JSON data and console log it
    return d3.json(url).then(function(data) {
        // Initialize each monthly total 
        let january = 0, february = 0, march = 0, april = 0, may = 0, june = 0, july = 0, august = 0, september = 0, october = 0, november = 0, december = 0;

        // For loop to go through all crash_month property
        for (let i = 0; i < data.length; i++) {
            // Get the month from the data
            let month = data[i].CRASH_MONTH;

            // Conditional statements to get count of each month and append it
            if (month === "1") {january += 1;
            } else if (month === "2") {february += 1;
            } else if (month === "3") {march += 1;
            } else if (month === "4") {april += 1;
            } else if (month === "5") {may += 1;
            } else if (month === "6") {june += 1;
            } else if (month === "7") {july += 1;
            } else if (month === "8") {august += 1;
            } else if (month === "9") {september += 1;
            } else if (month === "10") {october += 1;
            } else if (month === "11") {november += 1;
            } else if (month === "12") {december += 1;}
        }

        // Print totals for each month by year
        console.log(year + " Total Crashes by Month:");
        console.log("January to December", january, february, march, april, may, june, july, august, september, october, november, december); 
        console.log("--------------")

        // Create trace for scatter plot using Plotly
        const trace = {
            x: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
            y: [january, february, march, april, may, june, july, august, september, october, november, december],
            mode: 'lines+markers',
            name: year
        };

        // Return the trace
        return trace;
    });
}

function mainCrashesByWeekday(url, year) {
    // Fetch the JSON data and console log it
    return d3.json(url).then(function(data){
        //Initialize total of each weekday
        let sunday = 0, monday = 0, tuesday = 0, wednesday = 0, thursday = 0, friday = 0, saturday = 0 ; 

        // For loop to go through all days
        for (let i = 0; i < data.length; i++)  {
            // Get the weekday from the data
            let day = data[i].Weekday; 

            // Conditional statements to get count of each weekday and append it
            if (day === 'Sunday'){sunday +=1; 
            } else if (day === 'Monday'){monday +=1;
            } else if (day === 'Tuesday'){tuesday +=1;
            } else if (day === 'Wednesday'){wednesday +=1;
            } else if (day === 'Thursday'){thursday +=1;
            } else if (day === 'Friday'){friday +=1;
            } else if (day === 'Saturday'){saturday +=1;}
        }

        // Print totals for each weekday by year
        console.log(year + " Total Crashes by Weekday:");
        console.log("Sunday to Saturday", sunday,monday,tuesday,wednesday,thursday,friday,saturday);
        console.log("--------------")

        // Assign color by year for plotting inside main function    
        let color;
        if (year === '2022') {
            color = 'rgba(0, 140, 255, 0.6)'; // muted blue color 2022
        } else if (year === '2023') {
            color = 'rgba(31, 119, 180), 0.6)'; // safety orange color 2023
        }

        // Create bar chart for weekdays
        var trace = {
            y: ["Saturday","Friday","Thursday","Wednesday","Tuesday","Monday","Sunday"],
            x: [saturday,friday,thursday,wednesday,tuesday,monday,sunday], 
            type: 'bar',
            orientation: 'h',
            name: year,
            marker: {
                color: color
            }
        };

        // Return the trace
        return trace;
    });
}

// Fetch data for both years by month and weekday
Promise.all([
    mainCrashesByMonth(url_2022, '2022'),
    mainCrashesByMonth(url_2023, '2023'),
    mainCrashesByWeekday(url_2022, '2022'),
    mainCrashesByWeekday(url_2023, '2023')
]).then(traces => {
    
    // Layout for the scatter plot
    const layoutCrashesByMonth = {
        title: 'Crashes by Month 2022-2023',
        margin: { t: 50, l: 150, r: 300, b: 100 },
        xaxis: {
            title: 'Month' 
        },
        yaxis: {
            title: {
                text: 'Number of Car Crashes',
                standoff:20}
        }
    };

    // Layout for the bar plot
    const layoutCrashesByWeekday = {
        title: 'Crashes by Weekday 2022-2023',
        margin: { t: 50, l: 150, r: 300, b: 100 },            
        xaxis: {
            title: 'Number of Car Crashes',
            range: [8000, Math.max(...traces.flatMap(trace => trace.x))] 
        },
        yaxis: {
            title: {
                text: 'Weekday',
                standoff:20
            },
            tickangle: -35,
            ticklen: 8
        }
    };

    // Plot the scatter plot for crashes by month
    Plotly.newPlot('plot1', [traces[0], traces[1]], layoutCrashesByMonth);

    // Plot the bar plot for crashes by weekday
    Plotly.newPlot('plot2', [traces[2], traces[3]], layoutCrashesByWeekday);
}); 