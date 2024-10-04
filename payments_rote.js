const express = require('express');
const stripe = require('stripe')('YOUR_STRIPE_SECRET_KEY');
const router = express.Router();

router.post('/charge', async (req, res) => {
  const { amount, token } = req.body;
  
  try {
    const charge = await stripe.charges.create({
      amount: amount * 100, // amount in cents
      currency: 'usd',
      description: 'Charging station payment',
      source: token
    });
    res.status(200).send('Payment successful');
  } catch (error) {
    res.status(400).send('Payment failed');
  }
});

module.exports = router;
