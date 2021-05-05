import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("./skey.json")


firebase_admin.initialize_app(cred, {'databaseURL': 'https://chatbot-6f0a0-default-rtdb.firebaseio.com/'})

ref = db.reference('numbers')
print(ref.get())

#results = ref.child("test").get()

#print(results)
