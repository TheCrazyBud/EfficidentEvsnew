const express = require('express');
const cors = require('cors');
const mongoose = require('mongoose');

const app = express();
app.use(cors());
app.use(express.json());

// MongoDB connection
mongoose.connect('mongodb://localhost:27017/evdb', { useNewUrlParser: true, useUnifiedTopology: true });

// MongoDB Schema for reviews
const reviewSchema = new mongoose.Schema({
  station_name: String,
  review: String
});
const Review = mongoose.model('Review', reviewSchema);

// Endpoint to get EV status
app.get('/ev-status', (req, res) => {
  const evStatus = {
    battery_level: 85,
    motor_efficiency: 95,
    driving_mode: "Eco",
    predictive_maintenance: "No maintenance required",
    nearest_charging_station: { station_name: "ChargePoint", location: [40.7128, -74.0060] },
  };
  res.json(evStatus);
});

// Endpoint to submit a review
app.post('/reviews', (req, res) => {
  const newReview = new Review(req.body);
  newReview.save().then(() => {
    res.status(200).send('Review submitted');
  });
});

// Start the server
app.listen(5000, () => {
  console.log('Server running on http://localhost:5000');
});
