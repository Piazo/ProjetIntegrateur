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

    df.info()

    print(df.head())
    

  



regression()