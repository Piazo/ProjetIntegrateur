from matplotlib import test
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor


def regression(pred = False):

    # On récupère le dataFrame
    df = pd.read_csv("./data/value.csv", sep=';')
    
    # On enlève les 2 dernières colonnes: les coordonnées 
    df = df.drop(columns=["Coord1", "Coord2"], axis=1)


    X1 = df[["CPU1", "RAM1"]]
    Y1 = df["Latence1"]

    # On crée le jeu de tests et d'entraînement
    X_train, X_test, y_train, y_test = train_test_split(X1, Y1, test_size=0.2, random_state=42)


    # On normalise les données
    scaler = StandardScaler().fit(X_train)
    X_train_transformed = scaler.transform(X_train)
    X_test_transformed = scaler.transform(X_test)
    
    minScore = 4000 
    max_depth = 0
    bestModel = RandomForestRegressor()

    for i in [1, 2, 3, 4]:
        for j in [1, 2, 3]:
            clf = RandomForestRegressor(max_depth=i, min_samples_leaf=j, random_state=0).fit(X_train_transformed, y_train)
            currentScore = mean_squared_error(y_test, clf.predict(X_test_transformed), squared=False)
            print(i, j, currentScore)
            if currentScore < minScore:
                minScore = currentScore
                max_depth = i          
                bestModel = clf 

    print("\nRésultat trouvé : max depth = ", bestModel.max_depth)
    print("\nRésultat trouvé : min samples leaf = ", bestModel.min_samples_leaf)
    print("\nScore = ", minScore)

    print("------predictions-------")
    pred = bestModel.predict(X_test_transformed)

    for i in range(len(pred)):
        print("pred : ", pred[i], "  true value : ", y_test.to_numpy()[i])
   

regression()