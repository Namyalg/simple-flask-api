from flask import Flask, jsonify
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
app = Flask(__name__)

cred = credentials.Certificate("./skey.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://chatbot-6f0a0-default-rtdb.firebaseio.com/'})

@app.route('/<int:num>', methods=['GET'])
def hello_world(num):




    ref = db.reference('numbers')
    print(ref.get())
    ref = ref.get()
    vals = ref.values()
    #results = ref.child("test").get()
    if num in vals:
        return jsonify({"Present" : "Yes"})
    return jsonify({"Present" : "No"})

if __name__ == "__main__":
    app.run(debug=True)
