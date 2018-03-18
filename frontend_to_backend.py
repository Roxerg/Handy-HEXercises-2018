import json
import pickle
import numpy as np
from sklearn import svm


# Rokas imports
#import wsclient #currently not needed#

def receive_request(jsondata):
    # Receive the HTTP request from the webapp

    json_data = json.loads(jsondata)

    EXERCISE_ID = {"6": "half_bend", "5": "emoji", "4": "fingers", "3": "full_bend", "2": "mini_bend", "1": "pitch_exercise"}

    id_of_the_exercise = str(json_data["exerciseid"])
    arm_direction = str(json_data["armdata"]["arm direction"])
    pitch = str(json_data["armdata"]["pitch"])
    roll = str(json_data["armdata"]["roll"])
    yaw = str(json_data["armdata"]["yaw"])

    # Variables
    number_of_features = 12
    X_test = np.zeros(shape=(1, number_of_features))

    # Put the incoming data into X_test array to then feed it into the model
    x_count = 0
    for fingers in json_data:
        if fingers == "exerciseid" or fingers == "armdata":
            continue
        for angle in json_data[fingers]:
            X_test[0][0+x_count] = float(json_data[fingers][angle])
            x_count += 1

    # Test the data on the model according to the exercise id
    if EXERCISE_ID[id_of_the_exercise] == "half_bend":
        result = half_bend(X_test)
    elif EXERCISE_ID[id_of_the_exercise] == "emoji":
        result = emoji(X_test)
    elif EXERCISE_ID[id_of_the_exercise] == "fingers":
        result = fingers(X_test)
    elif EXERCISE_ID[id_of_the_exercise] == "full_bend":
        result = full_bend(X_test)
    elif EXERCISE_ID[id_of_the_exercise] == "mini_bend":
        result = mini_bend(X_test)
    elif EXERCISE_ID[id_of_the_exercise] == "pitch_exercise":
        result = pitch_exercise(pitch, roll, yaw, arm_direction)
    else:
        result = "There is a freaking somewhere error"

    # Send the result to the webapp
    return(str(result[0]))


# Function for testing the half_bend
def half_bend(X_test):
    model_filename = "half_bend_svm.sav"
    svm_model = pickle.load(open(model_filename, 'rb'))
    result = svm_model.predict(X_test)
    return result

# Function for testing the full_bend
def full_bend(X_test):
    model_filename = "full_bend_svm.sav"
    svm_model = pickle.load(open(model_filename, 'rb'))
    result = svm_model.predict(X_test)
    return result

# Function for testing the mini_bend
def mini_bend(X_test):
    model_filename = "mini_hand_bend_svm.sav"
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

def pitch_exercise(pitch, roll, yaw, arm_direction):
    pass

def send_info(result):
    # Send the result to the webapp
    pass


if __name__ == "__main__":
    receive_request()
