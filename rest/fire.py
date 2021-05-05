import firebase_admin
from firebase_admin import credentials

cred = credentials.Cert('skey.json')
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://chatbot-6f0a0-default-rtdb.firebaseio.com/'
})
