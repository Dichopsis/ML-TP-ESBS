from typing import Union
from sklearn.metrics import f1_score
from fastapi import FastAPI
from typing import List
import pickle
import urllib.request
from deta import Deta
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

# initialize with a project key
deta = Deta(os.getenv("DETAKEY"))

# create and use DBs
leaderboard_db = deta.Base("leaderboard")
if len(leaderboard_db.fetch({"name": "TD2"}).items) == 0:
    leaderboard_db.insert({"name": "TD2", "leaderboard": {}})


def load_ground_truth():
    data = pickle.load(
        urllib.request.urlopen("https://lbgi.fr/~meyer/TD_ML2/ground_truth.pickle")
    )
    return data


# FastAPI post route called "score" that take a list of prediction as entry and compare them to ground truth and calculate F1 score
# We then add the score to the leaderboard
@app.post("/score")
def score(prediction: List[int], student_name: str):
    # Fetch the leaderboard DB entry with its key, name and dict.
    leaderboard = leaderboard_db.fetch({"name": "TD2"})
    leaderboard_key = leaderboard.items[0]["key"]
    leaderboard_name = leaderboard.items[0]["name"]
    leaderboard_dict = leaderboard.items[0]["leaderboard"]
    # Load the real predictions
    ground_truth = load_ground_truth()
    prediction = [int(x) for x in prediction]
    # Calculate the student prediction score
    f1 = f1_score(prediction, ground_truth)
    # Default message
    message = "Sadly you did not improved your previous score !"
    # If the score is better than current best score, update the leaderboard
    if f1 > leaderboard_dict.get(student_name, 0):
        leaderboard_dict[student_name] = f1
        message = "Congrats ! You have a new personnal best score !"
    # Sort the leaderboard by F1 value
    leaderboard_dict = {
        k: v
        for k, v in sorted(
            leaderboard_dict.items(), key=lambda item: item[1], reverse=True
        )
    }
    # Get the Student rank in the leaderboard
    rank = list(leaderboard_dict.keys()).index(student_name) + 1
    rank_string = "You are currently ranked " + str(rank) + " in the leaderboard !"
    # Update the leaderboard DB entry
    leaderboard_db.put(
        {"name": leaderboard_name, "leaderboard": leaderboard_dict}, leaderboard_key
    )
    return {
        "msg": message,
        "F1": f1,
        "rank_msg": rank_string,
        "leaderboard": leaderboard_dict,
    }


@app.get("/")
def get_leaderboard():
    leaderboard = leaderboard_db.fetch({"name": "TD2"})
    leaderboard_dict = leaderboard.items[0]["leaderboard"]
    return {"leaderboard": leaderboard_dict}
