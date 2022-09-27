import numpy as np
import pandas as pd

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import models, layers
from sklearn.model_selection import GridSearchCV

# exercice a data
def test_set_a(num_data_points=10000):
    result = []
    np.random.seed(100)
    for i in range(0, num_data_points):
        base = np.random.uniform(101, 2000)
        a = base + np.random.uniform(-100, 100)
        b = base + np.random.uniform(-100, 100)
        target_class = 0 if a/b < 1 else 1
        result.append([a, b, target_class])
    return np.array(result)

# exercice b data
def test_set_b(num_data_points=10000):
    result = []
    np.random.seed(100)
    for i in range(0, num_data_points):
        base = np.random.uniform(-1000, 1000)
        a = base + np.random.uniform(-100, 100)
        b = base + np.random.uniform(-100, 100)
        target_class = 0 if abs(a - b) < 50 else 1
        result.append([a, b, target_class])
    return np.array(result)

# data preparation
def test_set_preparation(exercice, test_set):
    df = pd.DataFrame(test_set, columns=["A","B","Target"])
    
    if exercice == "exercice_a":
        df = df[df["B"]!=0]
    
    X = df[["A","B"]]
    y = df["Target"]
    return X,y

# model creation
def create_model(input_dim, units, learning_rate, decay, activation):
    model = models.Sequential()
    model.add(layers.Dense(units=units, activation=activation, kernel_initializer="random_uniform", input_dim=input_dim))
    model.add(layers.Dense(units=1, activation="sigmoid"))
    optimizer = keras.optimizers.Adam(learning_rate=learning_rate, decay=decay, clipvalue=0.5)
    model.compile(optimizer = 'Adam', loss="binary_crossentropy", metrics=["binary_accuracy"])
    return model

# model pipline and finetunning
def model_pipeline(model,X,y):
    
    # starting parameters for the model
    param_grid = {"learning_rate":[0.001],
              "decay":[0.0001],
              "activation":["relu"],
              "units":[16],
              "epochs":[5],
              "batch_size":[1]}
    
    # starting results for the model
    accuracy = 0
    standard_deviation = 0
    parameters = {}
    
    # find the best parameters until the accuray < 0.90
    while accuracy < 0.90:
        # add new parameters to the grid search
        param_grid["learning_rate"].append(np.random.uniform(0.001,0.009))
        
        # run the new model
        grid = GridSearchCV(estimator=model, param_grid=param_grid, cv=2, scoring='accuracy')
        grid_result = grid.fit(X, y)

        # update the results
        acc = grid_result.best_score_
        accuracy = acc
    
        std = grid_result.cv_results_['std_test_score'][grid_result.best_index_]
        standard_deviation = std
    
        param = grid_result.best_params_
        parameters = param
        
    return accuracy, standard_deviation, parameters
    
