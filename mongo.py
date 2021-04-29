
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/<int:num>', methods=["GET"])
def find_number(num):

    client = MongoClient("mongodb+srv://test:test@cluster0.ltlnj.mongodb.net/student_db?retryWrites=true&w=majority")
    db = client.get_database('student_db')
    records = db.student_records
    phone_nums = []
    for i in records.find({"_id": ObjectId("608a7697a9365fc9a694f7cc")}):
        print(i["Phone"])
        phone_nums = i["Phone"]
    if num in phone_nums:
        #return "YES"
        return jsonify({"Present" : "Yes"})
    #return "NO"
    return jsonify({"Present" : "No"})

if __name__ == "__main__":
    app.run(debug=True)
