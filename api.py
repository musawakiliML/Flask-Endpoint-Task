from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Resource, Api
import os
from enum import Enum

app = Flask(__name__)
api = Api(app)
CORS(app)


class HNGTask(Resource):
    def get(self):
        return jsonify({'slackUsername': "Musawakiliml", 'backend': True,
                    'age': 26,
                    'bio': "Hey, there i am an aspiring Machine Learning Engineer. A Python Developer with a zeal to become a grey haired programmer."})

api.add_resource(HNGTask, '/api/v1/about')

#@app.get("/api/v1/about")
#def about():
 #   return jsonify({'slackUsername': "Musawakiliml", 'backend': True,
 #                   'age': 26,
  #                  'bio': "Hey, there i am an aspiring Machine Learning Engineer. A Python Developer with a zeal to become a grey haired programmer."})

class operation_type(Enum):
    addition = "addition"
    subtraction = "subtraction"
    multiplication = "multiplication"
    
#data = {"operation_type": list(operation_type) , "x":int, "y": int }
#@app.post("/")
#def operation():
#    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=os.getenv("PORT", default=5000))
