import React from 'react'
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import { Bar } from 'react-chartjs-2';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

export default function ProjectChart(props) {

    const labels = ['0','1','2','3','4','5','6','7','8','9'];

    const options = {
        responsive: true,
        plugins: {
          legend: {
            position: 'top',
          },
          title: {
            display: true,
            text: 'Digit Recognition Prediction',
          },
        },
      };

    const data = {
        labels,
        datasets: [
          {
            label: 'Prediction',
            data: props.data,
            backgroundColor: 'rgba(255, 99, 132, 0.5)',
          }
        ],
      };

  return <div style={{margin: '1.2rem auto'}}>
    <Bar options={options} data={data} />
    </div>;
}
