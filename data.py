import requests as rq

parameters = {"amount": 10,
              "type": "boolean",
              "category": 18
              }
data = rq.get(url="https://opentdb.com/api.php",params= parameters)
data.raise_for_status()
q_data = data.json()
question_data = q_data["results"]

