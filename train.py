import settings
import numpy as np
import pandas as pd
from sklearn import GaussianProcessClassifier


# Load Training Labels
labels_train = pd.read_csv(f'{TRAIN_DATA_PATH}/train_labels.csv')
print(labels_train)
# Load Training FNC features

# Load training SBM features



# Combine and Normalize Data