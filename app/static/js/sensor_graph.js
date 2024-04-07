fetch('/sensor-data')
    .then(response => response.json())
    .then(data => {
        const { temperatures, humidities, wind_speeds, pressures } = data;
        const ctx = document.getElementById('sensorChart').getContext('2d');
        const sensorChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: Array.from({ length: temperatures.length }, (_, i) => i + 1),
                datasets: [
                    {
                        label: 'Temperature',
                        data: temperatures,
                        borderColor: 'rgb(255, 99, 132)',
                        backgroundColor: 'rgba(255, 99, 132, 0.5)',
                    },
                    {
                        label: 'Humidity',
                        data: humidities,
                        borderColor: 'rgb(54, 162, 235)',
                        backgroundColor: 'rgba(54, 162, 235, 0.5)',
                    },
                    {
                        label: 'Wind Speed',
                        data: wind_speeds,
                        borderColor: 'rgb(255, 206, 86)',
                        backgroundColor: 'rgba(255, 206, 86, 0.5)',
                    },
                    {
                        label: 'Pressure',
                        data: pressures,
                        borderColor: 'rgb(75, 192, 192)',
                        backgroundColor: 'rgba(75, 192, 192, 0.5)',
                    }
                ]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    })
    .catch(error => console.error('Error fetching sensor data:', error));
