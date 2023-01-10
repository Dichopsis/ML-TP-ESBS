from typing import Union
from sklearn.metrics import f1_score
from fastapi import FastAPI
from typing import List
import pickle
import json
import urllib.request

app = FastAPI()


def load_ground_truth():
    data = pickle.load(
        urllib.request.urlopen("https://lbgi.fr/~meyer/TD_ML2/ground_truth.pickle")
    )
    return data


def load_leaderboard():
    try:
        with open("/tmp/leaderboard.json", "r") as f:
            leaderboard = json.load(f)
        return leaderboard
    except FileNotFoundError:
        return {}


def save_leaderboard(leaderboard: dict):
    with open("/tmp/leaderboard.json", "w") as f:
        json.dump(leaderboard, f)


# FastAPI post route called "score" that take a list of prediction as entry and compare them to ground truth and calculate F1 score
# We then add the score to the leaderboard
@app.post("/score")
def score(prediction: List[int], student_name: str):
    leaderboard = load_leaderboard()
    ground_truth = load_ground_truth()
    prediction = [int(x) for x in prediction]
    f1 = f1_score(prediction, ground_truth)
    message = "Sadly you did not improved your previous score !"
    if f1 > leaderboard.get(student_name, 0):
        leaderboard[student_name] = f1
        message = "Congrats ! You have a new personnal best score !"
    # Sort the leaderboard by F1 value
    leaderboard = {
        k: v
        for k, v in sorted(leaderboard.items(), key=lambda item: item[1], reverse=True)
    }
    # get the student rank in the leaderboard
    rank = list(leaderboard.keys()).index(student_name) + 1
    rank_string = "You are currently ranked " + str(rank) + " in the leaderboard !"
    save_leaderboard(leaderboard)
    return {
        "msg": message,
        "F1": f1,
        "rank_msg": rank_string,
        "leaderboard": leaderboard,
    }


@app.get("/")
def get_leaderboard():
    leaderboard = load_leaderboard()
    return {"leaderboard": leaderboard}
