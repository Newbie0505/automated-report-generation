import pandas as pd
import os

def load_data(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f'File not found: {filepath}')
    df = pd.read_csv(filepath)
    df.dropna(how='all', inplace=True)
    numeric_cols = ['Units_Sold', 'Revenue', 'Expenses', 'Profit']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    print(f'Loaded {len(df)} rows')
    return df