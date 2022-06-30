import os
import pickle
import numpy as np
import pandas as pd

from sklearn.metrics import recall_score, precision_score
import json

filename = "pset2_model.sav"
X_test = np.genfromtxt("data/processed/test_features.csv")
y_test = np.genfromtxt("data/processed/test_labels.csv")

model = pickle.load(open(os.path.join("models", filename), 'rb'))

# Get overall accuracy
acc = model.score(X_test, y_test)

# Get precision and recall
y_score = model.predict(X_test)
prec = precision_score(y_test, y_score)
rec = recall_score(y_test, y_score)

# Get the loss
loss = model.loss_curve_
pd.DataFrame(loss, columns=["loss"]).to_csv("reports/loss.csv", index=False)

with open("reports/metrics.json", 'w') as outfile:
    json.dump({"accuracy": acc, "precision": prec, "recall": rec}, outfile)
