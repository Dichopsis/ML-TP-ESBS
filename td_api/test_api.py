# Make a post request to the score route with the following data:
# {
#     "prediction": [1, 0, 1, 1, 0, 1, 0, 1, 1, 0],
#     "student_name": "John"
# }
#
#
# # Path: api_test.py
import requests
import json
import pickle
import urllib.request

# Send a post request to the score route
def test_score_route():
    url = "http://127.0.0.1:8000/score"
    data = pickle.load(
        urllib.request.urlopen("https://lbgi.fr/~meyer/TD_ML2/ground_truth.pickle")
    )
    headers = {"accept": "application/json", "Content-Type": "application/json"}

    querystring = {"student_name": "test_user"}

    response = requests.request(
        "POST", url, params=querystring, json=data, headers=headers
    )
    print(response.json()["msg"])
    print(response.json()["rank_msg"])
    print("Your score is: ", response.json()["F1"])
    print("=== LEADERBOARD ===")
    counter = 1
    for key, value in response.json()["leaderboard"].items():
        print("Rank ", counter, " - ", key, " - F1: ", value)
        counter += 1


def show_leaderboard():
    url = "http://127.0.0.1:8000/"
    headers = {"accept": "application/json", "Content-Type": "application/json"}
    response = requests.request("GET", url, headers=headers)
    print("=== LEADERBOARD ===")
    counter = 1
    for key, value in response.json()["leaderboard"].items():
        print("Rank ", counter, " - ", key, " - F1: ", value)
        counter += 1


print("######## TEST 1: Submit Score ########")
test_score_route()
print("######## TEST 2: Show Leaderboard ########")
show_leaderboard()
