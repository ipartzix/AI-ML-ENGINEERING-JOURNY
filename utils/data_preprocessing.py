import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder


def load_csv(path):
    """Load CSV file into a DataFrame."""
    return pd.read_csv(path)


def encode_labels(df, column):
    """Encode categorical labels as integers."""
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    return df, le


def scale_features(X, method='standard'):
    """Scale features using StandardScaler or MinMaxScaler."""
    if method == 'standard':
        scaler = StandardScaler()
    elif method == 'minmax':
        scaler = MinMaxScaler()
    else:
        raise ValueError("method must be 'standard' or 'minmax'")
    X_scaled = scaler.fit_transform(X)
    return X_scaled, scaler


def split_data(X, y, test_size=0.2, random_state=42):
    """Split features and labels into training and test sets."""
    return train_test_split(X, y, test_size=test_size, random_state=random_state)
