from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)


@app.get("/api/v1/about")
def about():
    return jsonify({'slackUsername': "Musawakiliml", 'backend': True,
                    'age': 26,
                    'bio': "Hey, there i am an aspiring Machine Learning Engineer. A Python Developer with a zeal to become a grey haired programmer."})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=os.getenv("PORT", default=5000))
