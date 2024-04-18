const addSensorCharts = async (location) => {
    try {
        const response = await fetch(`/locations/${location}`);

        if (!response.ok) {
            const errorMsg = (await response.json()).error;
            throw new Error(errorMsg);
        }

        const data = await response.json();

        const chartsData = [
            ["Air Temperature", data.air_temperatures, data.timestamps, 'Temperature °C', 'rgba(255, 99, 132, 0.2)', 'rgba(255, 99, 132, 1)'],
            ["Humidity", data.humidities, data.timestamps, 'Humidity (%)', 'rgba(255, 206, 86, 0.2)', 'rgba(255, 206, 86, 1)'],
            ["Wind Speed", data.wind_speeds, data.timestamps, 'Wind Speed (m/s)', 'rgba(75, 192, 192, 0.2)', 'rgba(75, 192, 192, 1)'],
            ["Clearness", data.clearness, data.timestamps, 'Clearness (%)', 'rgba(120, 120, 120, 0.2)', 'rgba(120, 120, 120, 1)'],
            ["Water Temperature", data.water_temperatures, data.timestamps, 'Temperature °C', 'rgba(0, 255, 255, 0.2)', 'rgba(0, 255, 255, 1)'],
            ["Depth", data.depths, data.timestamps, 'Depth (m)', 'rgba(0, 0, 255, 0.2)', 'rgba(0, 0, 255, 1)'],
            ["Pressure", data.pressures, data.timestamps, 'Pressure (mb)', 'rgba(54, 162, 235, 0.2)', 'rgba(54, 162, 235, 1)']
        ];

        for (const [title, data, timestamps, yLabel, backgroundColor, borderColor] of chartsData) {
            createDataChart(title, data, timestamps, yLabel, backgroundColor, borderColor);
        }
    } catch (error) {
        const errorMessageElement = document.createElement('h3');
        errorMessageElement.textContent = error.message;

        const graphDivElement = document.getElementById('graph-div');
        graphDivElement.appendChild(errorMessageElement);
    }
}

const createDataChart = (title, data, timestamps, yLabel, backgroundColor, borderColor) => {
    const sensorChartElement = document.createElement('canvas');
    sensorChartElement.width = 100;
    sensorChartElement.height = 50;

    const ctx = sensorChartElement.getContext('2d');
    
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: timestamps,
            datasets: [{
                data: data,
                backgroundColor: backgroundColor,
                borderColor: borderColor,
                borderWidth: 1
            }]
        },
        options: {
            plugins: {
                title: { display: true, text: title,
                         align: 'center', font: { size: 20 } },
                legend: { display: false }
            },
            scales: {
                y: {
                    title: { display: true, text: yLabel,
                             align: 'center', font: { size: 18 } }
                },
                x: {
                    title: { display: true, text: 'Timestamp',
                             align: 'center', font: { size: 18 } },
                    ticks: { autoSkip: true, maxTicksLimit: 20, }
                }
            }
        }
    });

    const graphDivElement = document.getElementById('graph-div');
    graphDivElement.appendChild(sensorChartElement);
}