import firebase from "firebase/app";
import "firebase/messaging";

// Firebase config
firebase.initializeApp({
  apiKey: "YOUR_API_KEY",
  projectId: "YOUR_PROJECT_ID",
  messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
  appId: "YOUR_APP_ID"
});

const messaging = firebase.messaging();

export const requestPermission = () => {
  messaging.requestPermission().then(() => {
    return messaging.getToken();
  }).then(token => {
    console.log('FCM Token:', token);
  }).catch(err => {
    console.error('Error getting permission for notifications:', err);
  });
};
