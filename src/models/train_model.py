from sklearn.neural_network import MLPClassifier
import os
import numpy as np
import pickle

from modelstore import ModelStore
import json

# Read in data
X_train = np.genfromtxt("data/processed/train_features.csv")
y_train = np.genfromtxt("data/processed/train_labels.csv")

# Fit a model

model = MLPClassifier(random_state=0, max_iter=1)

model.fit(X_train, y_train)

# Save model Locally for further evaluation

filename = "pset2_model.sav"
pickle.dump(model, open(os.path.join("models", filename), 'wb'))

model_store = ModelStore.from_aws_s3("iiscdvc")

# Save model in AWS S3 bucket

domain = "pset2-prod-mlcp-model"
meta_data = model_store.upload(domain, model=model)

print(json.dumps(meta_data, indent=4))

print ("Model saved successfully in S3.")
