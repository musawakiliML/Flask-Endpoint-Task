from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_restful import Resource, Api
import settings
import os
import openai
from enum import Enum

app = Flask(__name__)
api = Api(app)
CORS(app)

# Load your API key from an environment variable or secret management service
openai.api_key = settings.openai_key
#openai.api_key = os.getenv("OPENAI_API_KEY")

class operation_type(Enum):
    addition = "+"
    subtraction = "-"
    multiplication = "*"

#data = list(operation_type)

#print(data)

class HNGTask1(Resource):
    def get(self):
        return jsonify({'slackUsername': "Musawakiliml", 'backend': True,
                    'age': 26,
                    'bio': "Hey, there i am an aspiring Machine Learning Engineer. A Python Developer with a zeal to become a grey haired programmer."})

class HNGTask2(Resource):
    def get(self):
        return jsonify({"Data": "Hello, World!"})  
    
    def post(self):
        data = request.get_json()
        
        result = None
        operation_type = None
        
        data_operation_type = data['operation_type'].lower()
        
        if 
        
        response = openai.Completion.create(model="text-davinci-002", prompt="Say this is a test", temperature=0, max_tokens=100)
        
        return jsonify(data)

api.add_resource(HNGTask1, '/api/v1/about')
api.add_resource(HNGTask2, '/api/v1/')

#print(openai.api_key)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=os.getenv("PORT", default=5000))

#@app.get("/api/v1/about")
#def about():
 #   return jsonify({'slackUsername': "Musawakiliml", 'backend': True,
 #                   'age': 26,
  #                  'bio': "Hey, there i am an aspiring Machine Learning Engineer. A Python Developer with a zeal to become a grey haired programmer."})
    
#data = {"operation_type": list(operation_type) , "x":int, "y": int }
#@app.post("/")
#def operation():
#    return jsonify(data)
