const express = require('express');
const Booking = require('./bookingModel');
const auth = require('./authMiddleware'); // JWT middleware

const router = express.Router();

// Create a new booking
router.post('/book', auth, async (req, res) => {
  const { station_name, booking_time, duration } = req.body;
  
  const booking = new Booking({
    user_id: req.user.userId,
    station_name,
    booking_time,
    duration
  });
  
  try {
    await booking.save();
    res.status(201).send('Booking confirmed');
  } catch (error) {
    res.status(400).send('Booking failed');
  }
});

// Get user bookings
router.get('/my-bookings', auth, async (req, res) => {
  const bookings = await Booking.find({ user_id: req.user.userId });
  res.json(bookings);
});

module.exports = router;
