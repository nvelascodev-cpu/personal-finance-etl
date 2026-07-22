import pandas as pd
def csv_to_dataframe(path_file_csv):
    """ Input: path to a CSV file and Return: DataFrame """
    df = pd.read_csv(path_file_csv)
    return df 


