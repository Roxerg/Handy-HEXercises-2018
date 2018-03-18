import json
import pickle
import numpy as np
from sklearn import svm


# Rokas imports
import wsclient

def receive_request(jsondata):
    # Receive the HTTP request from the webapp

    jsondata = json.loads(jsondata)

    EXERCISE_ID = {"6": half_bend, "5": emoji, "4": fingers}

    id_of_the_exercise = jsondata[0]

    # Variables
    number_of_features = 12
    X_test = np.zeros(shape=(1, number_of_features))

    # Put the incoming data into X_test array to then feed it into the model
    x_count = 0
    for fingers in json_data:
        if fingers == id_of_the_exercise:
            continue
        for angle in fingers:
            X_test[0][0+x_count] = float(fingers[angle])
            x_count += 1

    # Test the data on the model according to the exercise id
    if EXERCISE_ID[id_of_the_exercise] == "6":
        result = half_bend(X_test)
    elif EXERCISE_ID[id_of_the_exercise] == "5":
        result = emoji(X_test)
    elif EXERCISE_ID[id_of_the_exercise] == "4":
        result = fingers(X_test)
    else:
        result = "There is a freaking somewhere error"

    # Send the result to the webapp
    send_info(result)


# Function for testing the half_bend
def half_bend(X_test):
    model_filename = "half_bend_svm.sav"
    svm_model = pickle.load(open(model_filename, 'rb'))
    result = svm_model.predict(X_test)
    return result

# Function for testing the emoji
def emoji(X_test):
    model_filename = "emoji_svm.sav"
    svm_model = pickle.load(open(model_filename, 'rb'))
    result = svm_model.predict(X_test)
    return result

# Function for testing the fingers
def fingers(X_test):
    model_filename = "fingers_svm.sav"
    svm_model = pickle.load(open(model_filename, 'rb'))
    result = svm_model.predict(X_test)
    return result

def send_info(result):
    # Send the result to the webapp
    pass


if __name__ == "__main__":
    receive_request()
