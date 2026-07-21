import pandas as pd
def csv_to_dataframe(path_file_csv):
    df = pd.read_csv(path_file_csv)
    return df 


