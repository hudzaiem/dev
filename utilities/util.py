import pandas as pd
import numpy as np

def preproccess(df):
    df['value'] = df['value'].fillna(0)
    df['date'] = pd.to_datetime(df['date'])
    df['date'] = df['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
    df_dict = df.to_dict('records')
    return df_dict