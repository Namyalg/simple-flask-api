from firebase import Firebase

config = {
  "apiKey": "AIzaSyCMenIj4Q-IDm0NPMnQ4Mf3L7nWIQW_epw",
  "authDomain": "chatbot-6f0a0.firebaseapp.com",
  "databaseURL": "https://chatbot-6f0a0-default-rtdb.firebaseio.com",
  "storageBucket": "chatbot-6f0a0.appspot.com",
  "serviceAccount" : "./skey.json"
}

firebase = Firebase(config)
