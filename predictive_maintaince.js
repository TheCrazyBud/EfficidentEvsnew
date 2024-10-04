const tf = require('@tensorflow/tfjs-node');

// Example model training
async function trainModel(maintenanceData) {
  const xs = tf.tensor2d(maintenanceData.map(d => [d.mileage, d.batteryHealth]));
  const ys = tf.tensor2d(maintenanceData.map(d => [d.maintenanceRequired]));
  
  const model = tf.sequential();
  model.add(tf.layers.dense({ inputShape: [2], units: 1, activation: 'sigmoid' }));
  model.compile({ optimizer: 'adam', loss: 'meanSquaredError' });
  
  await model.fit(xs, ys, { epochs: 100 });
  return model;
}

module.exports = { trainModel };
