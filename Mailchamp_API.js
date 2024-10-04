const mailchimp = require('@mailchimp/mailchimp_marketing');

mailchimp.setConfig({
  apiKey: 'YOUR_MAILCHIMP_API_KEY',
  server: 'us19' // e.g., us19, check Mailchimp for your server prefix
});

async function sendMarketingEmail() {
  const response = await mailchimp.messages.send({
    message: {
      subject: "EV Service Promotion",
      from_email: "your_email@example.com",
      to: [{ email: "customer_email@example.com" }],
      text: "Check out our new features for your EV!"
    }
  });
  return response;
}

sendMarketingEmail().then(response => {
  console.log('Email sent:', response);
}).catch(err => {
  console.error('Error:', err);
});
