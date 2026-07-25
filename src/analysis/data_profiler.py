from src.contracts import data_contract
import pandas as pd
def get_invalid_values(df, valid_values): #Los invalidos están definidos en el contrato
        invalid_values={}

        for column, allowed_values in valid_values.items():
            unique_values = df[column].unique()

            for value in unique_values:
                if pd.notna(value): 
                    if value not in allowed_values: #Value no está en los permitidos 
                        occurrences = int((df[column] == value).sum()) #Comparo value con los valores de la columna y asi contar cuantas veces aparece "True"

                        if column not in invalid_values:
                            invalid_values[column] = {}
                        invalid_values[column][value]=occurrences

        return invalid_values

def analyze_dataframe(df):
    profile = {
        "rows":len(df),
        "columns":len(df.columns),
        "data_types":df.dtypes.to_dict(),
        "null_values":df.isnull().sum().to_dict(),
        "duplicates": {
                        "count":int(df['id'].duplicated().sum()),
                        "duplicates_ids":df["id"][df["id"].duplicated()].unique().tolist()
        },
        "invalid_values": get_invalid_values(df,data_contract.VALID_VALUES) #Son invalidos definidos en el contraro
        
    }

    
    
    return profile


