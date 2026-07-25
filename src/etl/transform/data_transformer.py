import pandas as pd 
from src.contracts import data_contract

def to_Int(series):
    return pd.to_numeric(series,errors="coerce").astype("Int64")

def to_float(series):
    return pd.to_numeric(series,errors="coerce").astype("float64")

def to_datetime(series):
    return pd.to_datetime(series,errors="coerce")

def to_string(series):
    return series.astype("string")

TYPE_CONVERTERS = {
    "Int64": to_Int,
    "float64":to_float,
    "datetime":to_datetime,
    "string":to_string,
}

def convert_data_types(df,expected_types):
    for column, expected_type in expected_types.items():
        if column in df.columns:
            current_type=df[column].dtype

            if str(current_type) != expected_type:
                converter = TYPE_CONVERTERS.get(expected_type)

                if converter is not None:
                    df[column] = converter(df[column])

    return  df  

def normalize_text(df):
    for column in df.columns:
        if df[column].dtype == "string":
            df[column] = (df[column] 
            .str.strip()
            .str.replace(r"\s+"," ", regex=True) #Elimina dos espacios consecutivos
            .str.title()
            )
    return df

def remove_empty_rows(df):
    df=df.dropna(how="all")
    return df

def remove_null_ids(df):
    df=df.dropna(subset=['id'])
    return df

def remove_duplicate_ids(df):
    df=df.drop_duplicates(subset=['id'], keep='first')
    return df

def tansform(df): #basic transform
    df_transform = df.copy()

    df_transform = convert_data_types(df_transform,data_contract.EXPECTED_TYPES)
    df_transform = normalize_text(df_transform)
    df_transform = remove_empty_rows(df_transform)
    df_transform = remove_null_ids(df_transform)
    df_transform = remove_duplicate_ids(df_transform)


    return df_transform