import pandas as pd

class DataCleaning:

    def __init__(self):
        pass

    @staticmethod
    def cleaning(df: pd.DataFrame):

        for column  in df.columns:
            # if its number fill with avg of column
            if df [column].dtypes in ['int64', 'float64']:
                df[column].fillna(df[column].mean(),inplace= True)
            # else fill with mode string in the column
            else:
                df[column].fillna(df[column].mode()[0],inplace=True)

        return df







