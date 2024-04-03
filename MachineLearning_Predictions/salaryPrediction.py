import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from xgboost import XGBRegressor

def predictSalary(v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22):
    df = pd.read_csv('ML_Datasets/Engineering_graduate_salary.csv')

    df.drop(['ID', 'DOB', 'CollegeID', '12graduation', '10board', '12board', 'CollegeState'
                , 'CollegeCityID', 'CollegeCityTier'
                , 'GraduationYear'], axis=1, inplace=True)

    df.drop_duplicates()

    specialization = df.Specialization.value_counts(ascending=False)

    specializationlessthan10 = specialization[specialization <= 10]

    def removespeciallessthan10(value):
        if value in specializationlessthan10:
            return 'other'
        else:
            return value

    df.Specialization = df.Specialization.apply(removespeciallessthan10)
    df = df.replace(-1, np.nan)

    cols_with_nan = [column for column in df.columns if df.isna().sum()[column] > 0]
    for column in cols_with_nan:
        df[column] = df[column].fillna(df[column].mean())

    df.drop(['10percentage'], axis=1, inplace=True)

    le = LabelEncoder()

    df.Gender = le.fit_transform(df.Gender)
    df.Degree = le.fit_transform(df.Degree)
    df.Specialization = le.fit_transform(df.Specialization)

    x = df.drop('Salary', axis=1)
    y = df['Salary']

    sc = StandardScaler()
    x = sc.fit_transform(x)

    xgb = XGBRegressor()
    xgb.fit(x, y)
    data = []
    data.append([0.0, 75.0, 2.0, 0.0, 0.0, 64.3, 575.0, 495.0, 365.0, 0.278457409311292, 315.0, 335.9479166666667,
                 406.72063037249285, 401.1748633879781, 423.3360655737705, 349.8795620437956, 341.96, -1.4992, -0.7473,
                 -1.0697, 0.0622299999999999, 0.1864])
    X_manual = pd.DataFrame(data)
    predictions = xgb.predict(X_manual)
    float(predictions[0])

    return (float(predictions[0]))

