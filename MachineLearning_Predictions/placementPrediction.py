import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def placement(v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12):
    df = pd.read_csv('ML_Datasets/Placement_Data_Full_Class.csv')

    from sklearn.preprocessing import LabelEncoder
    encoder = LabelEncoder()
    df['gender'] = encoder.fit_transform(df['gender'])
    df['ssc_b'] = encoder.fit_transform(df['ssc_b'])
    df['hsc_b'] = encoder.fit_transform(df['hsc_b'])
    df['hsc_s'] = encoder.fit_transform(df['hsc_s'])
    df['degree_t'] = encoder.fit_transform(df['degree_t'])
    df['workex'] = encoder.fit_transform(df['workex'])
    df['specialisation'] = encoder.fit_transform(df['specialisation'])
    df['status'] = encoder.fit_transform(df['status'])

    columns_to_drop = ['status', 'sl_no', 'salary']
    X = df.drop(columns_to_drop, axis=1)
    y = df['status']

    X = df.drop(columns_to_drop, axis=1)
    y = df['status']

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

    from sklearn.neighbors import KNeighborsClassifier
    knn = KNeighborsClassifier(n_neighbors=14)
    knn.fit(X_train, y_train)


    y_pred = knn.predict(X_test)

    columns = X_train.columns
    data = []
    ##
    if v1 == "M":
        v1 = 1
    else:
        v1 = 0

    if v3 == "Central":
        v3 = 0
    else:
        v3 = 1

    if v5 == "Central":
        v5 = 0
    else:
        v5 = 1

    if v6 == "Science":
        v6 = 2
    elif v6 == "Commerce":
        v6 = 1
    else:
        v6 = 0

    if v8 == "Sci&Tech":
        v8 = 2
    else:
        v8 = 0

    if v9 == "Yes":
        v9 = 1
    else:
        v9 = 0

    if v11 == "Mkt&Fin":
        v11 = 0
    else:
        v11 = 1
    ##
    data.append([v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12])
    X_manual = pd.DataFrame(data, columns=columns)
    ans_pred = knn.predict(X_manual)

    return ans_pred