from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.get("/")
def about():
  return {'slackusername': "Musawakiliml",
            'backend': True,
            'age': 26,
            'bio': "Hey, there i am an aspiring Machine Learning Engineer. A Python Developer with a zeal to become a grey haired programmer."}



if __name__ == "__main__":
    app.run(debug=True)