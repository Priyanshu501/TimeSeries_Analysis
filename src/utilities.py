''' Contains all the necessary functions for Statistical Calculations '''
import pandas as pd

def preprocessing(df):
    ''' Data Preprocessing '''
    # Converting Date Colume to Date Time Format
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

    # Setting Date columne as Index
    df = df.set_index('Date').rename_axis(None)
    return df
