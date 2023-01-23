import tensorflow as tf
import pandas as pd

# Load all the models 

# Node 1
model1 = tf.keras.models.load_model('ModelSaved/Node1')

# Node 1
model2 = tf.keras.models.load_model('ModelSaved/Node2')

# Node 1
model3 = tf.keras.models.load_model('ModelSaved/Node3')



# architecture du modèle 1
model1.summary()


# Faire des prédictions 
# On a besoin des 6 dernières latences, et on calcule les medianes des 3 dernières latences et les moyennes des 4 dernières
# Donc pour commencer, on doit avoir les 9 dernières latences.

# Imaginons qu'on ait pour le node 1:

latences = [0.3, 0.4, 0.4, 0.23, 0.66, 0.6, 0.4, 0.3, 0.22]

df = pd.DataFrame()

print("AVANT CALCUL")

df['val'] = latences
print(df)

print("APRES CALCUL")

df['median'] = df['val'].rolling(3).median()
df['mean'] = df['val'].rolling(4).mean()

# On enlève la latence
df = df.drop(columns=['val'])


# Les 3 premières valeurs sont NaN, c'est normal
print(df)


print("On enlève les colonnes NaN ")
df.dropna(inplace=True)
print(df)


# df comporte maintenant 6 valeurs, on peut faire des predictions dessus : 
print("\nPredictions\n")

# On le met en format list

val = df.values.tolist()

print(model1.predict([val]))