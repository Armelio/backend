from flask import Flask
import json
import random
from flask_cors import CORS
from dotenv import load_dotenv
import os

app=Flask(__name__)
CORS(app)
envload=load_dotenv()
apikey=os.getenv("APIKEY")

@app.route("/data", methods=['GET'])

def getdata():
    listFruit=['apple','banana','orange']
    randomfruit=listFruit[random.randint(0,2)]
    return json.dumps({"fruit": randomfruit, "api":apikey})

getdata()

app.run(debug=True)
  
