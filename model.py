from sklearn.preprocessing import LabelEncoder, StandardScaler
import pandas as pd
import numpy as np

def preprocess(data):
    data= pd.DataFrame.from_dict(data)
    # Detect categorical and numerical columns
    categorical_cols = data.select_dtypes(include='object').columns

    # Label encode categorical columns
    label_encoders = {}
    for col in categorical_cols:
        label_encoder = LabelEncoder()
        data[col] = label_encoder.fit_transform(data[col])
        label_encoders[col] = label_encoder

    data=data.to_dict()

    return data
