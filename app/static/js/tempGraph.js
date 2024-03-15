fetch('/temp-data')
    .then(response => response.json())
    .then(temperatures => {
        const ctx = document.getElementById('tempChart').getContext('2d');
        const myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: Array.from({ length: temperatures.length }, (_, i) => i + 1), // Generating sequential labels
                datasets: [{
                    label: 'Temperature',
                    data: temperatures,
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                }
            }
        });
    })
    .catch(error => console.error('Error fetching temperature data:', error));