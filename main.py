from flask import Flask
import json
import random
from flask_cors import CORS


app=Flask(__name__)
CORS(app)

@app.route("/data", methods=['GET'])

def getdata():
    listFruit=['apple','banana','orange']
    randomfruit=listFruit[random.randint(0,2)]
    return json.dumps({"fruit": randomfruit, "api":apikey})

getdata()

app.run(debug=True)
  
