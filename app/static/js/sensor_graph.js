const location = 'kiten-atliman'; // Заместете 'someLocation' с началната локация или използвайте метода за извличане от URL

const addSensorCharts = async (location) => {
    try {
        const response = await fetch(`/locations/${location}`);
        if (!response.ok) {
            const errorMsg = await response.json();
            throw new Error(errorMsg.error);
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

        // Очистване на старите графики преди да добавите нови
        const graphDivElement = document.getElementById('graph-div');
        graphDivElement.innerHTML = ''; // Премахвате старите canvas елементи

        for (const [title, data, timestamps, yLabel, backgroundColor, borderColor] of chartsData) {
            createDataChart(title, data, timestamps, yLabel, backgroundColor, borderColor);
        }
    } catch (error) {
        console.error('Error loading sensor data:', error);
        const errorMessageElement = document.createElement('h3');
        errorMessageElement.textContent = error.message;
        document.getElementById('graph-div').appendChild(errorMessageElement);
    }
};

// Създаване на графиката
const createDataChart = (title, data, timestamps, yLabel, backgroundColor, borderColor) => {
    const sensorChartElement = document.createElement('canvas');
    sensorChartElement.width = 400;
    sensorChartElement.height = 200;
    const ctx = sensorChartElement.getContext('2d');

    new Chart(ctx, {
        type: 'line',
        data: {
            labels: timestamps,
            datasets: [{
                label: title,
                data: data,
                backgroundColor: backgroundColor,
                borderColor: borderColor,
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: yLabel
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: 'Timestamp'
                    },
                    ticks: {
                        callback: function(value, index, values) {
                            // Показва етикет само на всеки трети запис
                            return index % 4 === 0 ? value : '';
                        },
                        maxRotation: 0, // Предотвратява въртенето на етикетите, ако са дълги
                        autoSkip: false // Изключва автоматичното пропускане на етикети от Chart.js
                    }
                }
            }
        }
    });

    document.getElementById('graph-div').appendChild(sensorChartElement);
};

// Инициализация на графиките при зареждане на страницата
addSensorCharts(location);

// Настройка за автоматично обновление на графиките на всеки 60 секунди
setInterval(() => {
    addSensorCharts(location);
}, 10000); // Обновяване на всеки 60 секунди
