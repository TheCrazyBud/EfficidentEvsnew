import React from 'react';
import StripeCheckout from 'react-stripe-checkout';
import axios from 'axios';

function Payment({ amount }) {
  const handleToken = (token) => {
    axios.post('http://localhost:5000/charge', { token, amount })
      .then(response => {
        alert('Payment successful');
      }).catch(error => {
        alert('Payment failed');
      });
  };

  return (
    <StripeCheckout
      stripeKey="YOUR_STRIPE_PUBLISHABLE_KEY"
      token={handleToken}
      amount={amount * 100}
      name="EV Charging Payment"
      currency="USD"
    />
  );
}

export default Payment;
