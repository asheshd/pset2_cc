from sklearn.neural_network import MLPClassifier
import os
import numpy as np
import pickle


# Read in data
X_train = np.genfromtxt("data/processed/train_features.csv")
y_train = np.genfromtxt("data/processed/train_labels.csv")

# Fit a model

model = MLPClassifier(random_state=0, max_iter=10)

model.fit(X_train, y_train)

# Save model

filename = "pset2_model.sav"
pickle.dump(model, open(os.path.join("models", filename), 'wb'))

print("Model saved successfully")