import json
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from random import shuffle
import pickle

model_filename = 'svm_model_file.sav'

def train_model():
    json_data = json.load(open("output_file.json", "r+"))

    number_of_features = 12
    total_training_examples = 0
    for x in json_data:
        total_training_examples = total_training_examples + len(json_data[x])

    X_train = np.zeros(shape=(total_training_examples, number_of_features+1))
    Y_train = np.zeros(shape=(total_training_examples))

    y_count = 0

    for i in range(0, len(json_data["none"])):
        x_count = 0
        for x in range(1, 5):
            X_train[y_count][0+x_count] = float(json_data["none"][str(i)][str(x)]["MPA"])
            X_train[y_count][1+x_count] = float(json_data["none"][str(i)][str(x)]["PIA"])
            X_train[y_count][2+x_count] = float(json_data["none"][str(i)][str(x)]["IPA"])
            x_count = x_count + 3
        X_train[y_count][x_count] = 0
        y_count = y_count + 1

    for i in range(0, len(json_data["1"])):
        x_count = 0
        for x in range(1, 5):
            X_train[y_count][0+x_count] = float(json_data["1"][str(i)][str(x)]["MPA"])
            X_train[y_count][1+x_count] = float(json_data["1"][str(i)][str(x)]["PIA"])
            X_train[y_count][2+x_count] = float(json_data["1"][str(i)][str(x)]["IPA"])
            x_count = x_count + 3
        X_train[y_count][x_count] = 1
        y_count = y_count + 1

    '''
    for i in range(0, len(json_data["two"])):
        x_count = 0
        for x in range(0, len(json_data["two"][str(i)])):
            X_train[y_count][0+x_count] = float(json_data["two"][str(i)][str(x)]["MPA"])
            X_train[y_count][1+x_count] = float(json_data["two"][str(i)][str(x)]["PIA"])
            X_train[y_count][2+x_count] = float(json_data["two"][str(i)][str(x)]["IPA"])
            x_count = x_count + 3
        X_train[y_count][x_count] = 2
        y_count = y_count + 1

    '''

    np.random.shuffle(X_train)
    Y_train = X_train[:,-1]
    X_train = X_train[:,:-1,]

    X_test = X_train[-2:]
    Y_test = Y_train[-2:]

    Y_train = Y_train[:-2]
    X_train = X_train[:-2]

    print(X_train.shape[0])
    print(Y_train.shape[0])
    print(X_test.shape[0])
    print(Y_test.shape[0])

    """
    clf = RandomForestClassifier(n_jobs=2, random_state=0)
    clf.fit(X_train, Y_train)
    """

    svm_model = svm.SVC(probability=True)
    svm_model.fit(X_train, Y_train)

    print("Training SVM on " + str(X_train.shape[0]) + " samples")
    print("Accuracy on training data: " + str(svm_model.score(X_train, Y_train)))
    #print("Support vectors: " + str(len(svm_model.support_vectors_)))

    pickle.dump(svm_model, open(model_filename, 'wb'))

def test_model():

    # Load the neural network model from a pickle file
    svm_model = pickle.load(open(model_filename, 'rb'))

    json_data = json.load(open("output_file_test.json", "r+"))

    number_of_features = 12
    total_training_examples = 0
    for x in json_data:
        total_training_examples = total_training_examples + len(json_data[x])

    X_test = np.zeros(shape=(total_training_examples, number_of_features+1))
    Y_test = np.zeros(shape=(total_training_examples))

    y_count = 0

    for jdata in json_data:
        for i in range(0, len(json_data[jdata])):
            x_count = 0
            for x in range(1, 5):
                X_test[y_count][0+x_count] = float(json_data[jdata][str(i)][str(x)]["MPA"])
                X_test[y_count][1+x_count] = float(json_data[jdata][str(i)][str(x)]["PIA"])
                X_test[y_count][2+x_count] = float(json_data[jdata][str(i)][str(x)]["IPA"])
                x_count = x_count + 3
            if jdata == "none":
                X_test[y_count][x_count] = 0
            elif jdata == "1":
                X_test[y_count][x_count] = 1
            elif jdata == "2":
                X_test[y_count][x_count] = 2
            y_count = y_count + 1

    Y_test = X_test[:,-1]
    X_test = X_test[:,:-1,]

    print("Testing SVM on " + str(X_test.shape[0]) + " samples")
    print("Accuracy on testing data: " + str(svm_model.score(X_test, Y_test)))
    print("Predicted outcomes: " + str(svm_model.predict(X_test)))
    print("Actual outcomes: " + str(Y_test))

if __name__ == "__main__":
    train_model()
    test_model()
