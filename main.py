from src.etl.extract import csv_reader 
from src.analysis import data_profiler
PATH_CSV="data/raw/data_finance.csv"
df=csv_reader.csv_to_dataframe(PATH_CSV)
#print(df.head())
profile = data_profiler.analyze_dataframe(df)
print(profile)