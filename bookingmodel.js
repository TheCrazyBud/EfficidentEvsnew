const mongoose = require('mongoose');

const bookingSchema = new mongoose.Schema({
  user_id: { type: mongoose.Schema.Types.ObjectId, ref: 'User' },
  station_name: { type: String, required: true },
  booking_time: { type: Date, required: true },
  duration: { type: Number, required: true } // Duration in hours
});

const Booking = mongoose.model('Booking', bookingSchema);
module.exports = Booking;
