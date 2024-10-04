import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [evData, setEvData] = useState(null);
  const [review, setReview] = useState("");
  const [stationName, setStationName] = useState("");
  const [reviews, setReviews] = useState([]);
  
  useEffect(() => {
    // Fetch EV data from backend
    axios.get('http://localhost:5000/ev-status').then((response) => {
      setEvData(response.data);
    });
  }, []);

  const submitReview = () => {
    axios.post('http://localhost:5000/reviews', {
      station_name: stationName,
      review: review
    }).then(() => {
      alert('Review submitted');
      setReviews([...reviews, { station_name: stationName, review }]);
    });
  };

  return (
    <div className="App">
      <h1>Electric Vehicle Dashboard</h1>
      {evData ? (
        <div>
          <p>Battery Level: {evData.battery_level}%</p>
          <p>Motor Efficiency: {evData.motor_efficiency}%</p>
          <p>Current Mode: {evData.driving_mode}</p>
          <p>Next Maintenance Check: {evData.predictive_maintenance}</p>
          <p>Nearest Charging Station: {evData.nearest_charging_station.station_name}</p>
        </div>
      ) : (
        <p>Loading EV data...</p>
      )}
      
      <h2>Leave a Review</h2>
      <input type="text" placeholder="Station Name" value={stationName} onChange={e => setStationName(e.target.value)} />
      <textarea placeholder="Write a review" value={review} onChange={e => setReview(e.target.value)} />
      <button onClick={submitReview}>Submit Review</button>
      
      <h2>Reviews</h2>
      {reviews.map((r, index) => (
        <div key={index}>
          <h4>{r.station_name}</h4>
          <p>{r.review}</p>
        </div>
      ))}
    </div>
  );
}

export default App;
