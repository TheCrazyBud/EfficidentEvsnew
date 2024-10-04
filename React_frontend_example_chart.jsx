import React from 'react';
import { Line } from 'react-chartjs-2';

function Analytics({ energyConsumption }) {
  const data = {
    labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    datasets: [
      {
        label: 'Energy Consumption (kWh)',
        data: energyConsumption,
        borderColor: 'rgba(75,192,192,1)',
        borderWidth: 2,
        fill: false
      }
    ]
  };

  return (
    <div>
      <h2>Energy Consumption Over Time</h2>
      <Line data={data} />
    </div>
  );
}

export default Analytics;


