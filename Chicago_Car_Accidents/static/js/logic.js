// Function to create map
function createMap(crashLayer, heatLayer, markerCluster, legends) {
  // Create the tile layer that will be the background of our map.
  let streetmap = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  });

  let satellite = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
    attribution: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community'
  });

  let darkMode = L.tileLayer('https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png', {
    attribution: '&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>, &copy; <a href="https://openmaptiles.org/">OpenMapTiles</a> &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors'
  });

  // Create a baseMaps object to hold the streetmap layer and the others.
  let baseMaps = {
    "Street Map": streetmap,
    "Satellite": satellite
    //"Dark Mode": darkMode
  };

  // Create an overlayMaps object to hold the crashLayer, heatLayer, and markerCluster.
  let overlayMaps = {
    "Car Accidents in Chicago": crashLayer,
    "Heatmap": heatLayer,
    "Marker Cluster": markerCluster
  };

  // Create the map object with options.
  map = L.map("map-id", {
    center: [41.8781, -87.6298], // Chicago's coordinates
    zoom: 12,
    layers: [streetmap, crashLayer, heatLayer, markerCluster]
  });

  // Add layer control to the map.
  L.control.layers(baseMaps, overlayMaps, {
    collapsed: false      //we can put false as well if we want
  }).addTo(map);

  // Create a legend control
  let legend = createLegendControl(legends);
  legend.addTo(map);
}

// Function to create a legend control
function createLegendControl(legends) {
  let legend = L.control({
    position: 'bottomright'
  });

  legend.onAdd = function(map) {
    let div = L.DomUtil.create('div', 'info legend');
    
    // Define the box properties
    div.style.backgroundColor = 'rgba(255, 255, 255, .7)';
    div.style.padding = '10px';
    div.style.borderRadius = '5px';
    div.style.maxHeight = '200px'; // we can adjust this 
    div.style.overflowY = 'auto'; // Enable vertical scrolling if content exceeds the height
    
    // Using template literals to construct the legend content
    div.innerHTML = `
      <div style="font-size: 14px; margin-bottom: 5px;"><strong>Accident Cause</strong></div>
      <div style="font-size: 12px;">`;

    // Sort legends by count
    const sortedLegends = Object.entries(legends).sort((a, b) => b[1].count - a[1].count);
    
    // Append legend items dynamically
    sortedLegends.forEach(([cause, { color, count }]) => {
      div.innerHTML += `<div><span style="color:${color}">&bull;</span> ${cause} (${count})</div>`;
    });

    div.innerHTML += `</div>`; // Close the legend content

    return div;
  };

  return legend;
}

// Function to create markers
function createMarkers(response) {
  // Initialize arrays to hold car markers and coordinates for the heatmap.
  let carMarkers = [];
  let heatArray = [];
  let legends = {};

  // Initialize a MarkerClusterGroup to hold car markers.
  let markerCluster = L.markerClusterGroup();

  // Loop through the response array.
  response.forEach(crash => {
    let latitude = parseFloat(crash.latitude);
    let longitude = parseFloat(crash.longitude);

    // Check if latitude and longitude are valid numbers.
    if (latitude && longitude) {
      // Create a marker for each crash using valid coordinates.
      let carMarker = L.marker([latitude, longitude])
        .bindPopup(`<h3>Location: ${crash.street_no} ${crash.street_direction} ${crash.street_name}</h3><p>Crash Date: ${new Date(crash.crash_date).toDateString()}<p>Crash Hour:${new Date(crash.crash_date).toLocaleTimeString()}<p>Accident Cause: ${crash.prim_contributory_cause}<p>Lighthing Condition: ${crash.lighting_condition}<p>Weather Condition: ${crash.weather_condition}</p>`);
      // Add the marker to the carMarkers array.
      carMarkers.push(carMarker);

      // Add coordinates to heatArray for heatmap.
      heatArray.push([latitude, longitude]);

      // Add the marker to the markerCluster.
      markerCluster.addLayer(carMarker);

      // Update legend data
      if (!legends[crash.prim_contributory_cause]) {
        
        let color = '#000000'; // Black color
        legends[crash.prim_contributory_cause] = {
          color: color,
          count: 1
        };
      } else {
        legends[crash.prim_contributory_cause].count++;
      }
    }
  });

  // Create a layer group from carMarkers array.
  let crashLayer = L.layerGroup(carMarkers);

  // Create a heatmap layer from heatArray.
  let heatLayer = L.heatLayer(heatArray, { radius: 80, blur: 50 });

  // Create a map with crashLayer, heatLayer, and markerCluster.
  createMap(crashLayer, heatLayer, markerCluster, legends);

  // Display first and last crash dates
  displayCrashDates(response);
}

// Function to display first and last crash dates
function displayCrashDates(response) {
  let firstCrashDate = '';
  let lastCrashDate = '';
  
  // Loop through the response array to find first and last crash dates
  response.forEach(crash => {
    if (!firstCrashDate || new Date(crash.crash_date) < new Date(firstCrashDate)) {
      firstCrashDate = crash.crash_date;
    }
    if (!lastCrashDate || new Date(crash.crash_date) > new Date(lastCrashDate)) {
      lastCrashDate = crash.crash_date;
    }
  });
  
  // Construct HTML content for first and last crash dates
  let content = `
    <div style="font-size: 14px; margin-bottom: 5px;"><strong>First and Last Crash Dates in this Map</strong></div>
    <div style="font-size: 12px;">
      <div>First Crash Date: <span>${new Date(firstCrashDate).toDateString()}</span></div>
      <div>Last Crash Date: <span>${new Date(lastCrashDate).toDateString()}</span></div>
    </div>
  `;
  
  // Create a legend control
  let legend = L.control({
    position: 'bottomleft'
  });
  
  legend.onAdd = function(map) {
    let div = L.DomUtil.create('div', 'info legend');
    
    // Define the box properties
    div.style.backgroundColor = 'rgba(255, 255, 255, .7)';
    div.style.padding = '10px';
    div.style.borderRadius = '5px';
    div.style.maxHeight = '200px'; // we can adjust this 
    div.style.overflowY = 'auto'; // Enable vertical scrolling if content exceeds the height
    
    // Set the content
    div.innerHTML = content;

    return div;
  };

  // Add legend to the map
  legend.addTo(map);
}

// Perform an API call to get the crash information. Call createMarkers when it completes.
d3.json("https://data.cityofchicago.org/resource/85ca-t3if.json")
  .then(createMarkers);

