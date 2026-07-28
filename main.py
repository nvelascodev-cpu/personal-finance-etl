from src.analysis import data_profiler
from src.analysis import profile_report
from src.contracts import database_contract
from src.etl.extract import csv_reader
from src.etl.load import sqlite_loader
from src.etl.transform import data_transformer

def main():
    PATH_CSV = "data/raw/data_finance.csv"


    # =========================
    # EXTRACT
    # =========================

    df_raw = csv_reader.csv_to_dataframe(PATH_CSV)


    # =========================
    # ANALYZE (Antes)
    # =========================

    profile_before = data_profiler.analyze_dataframe(df_raw)


    # =========================
    # TRANSFORM
    # =========================

    df_transform = data_transformer.tansform(df_raw)


    # =========================
    # ANALYZE (Después)
    # =========================

    profile_after = data_profiler.analyze_dataframe(df_transform)


    # =========================
    # LOAD
    # =========================

    connection = sqlite_loader.connect_database(
        database_contract.DATABASE_PAHT
    )

    sqlite_loader.create_table(connection)
    sqlite_loader.clear_table(connection)
    sqlite_loader.insert_dataframe(connection, df_transform)


    # =========================
    # VALIDACIÓN
    # =========================

    df_sqlite = sqlite_loader.read_database(connection)

    sqlite_loader.close_database(connection)


    # =========================
    # RESULTADOS
    # =========================

    print(df_sqlite)

    # profile_report.print_profile(profile_before)
    # profile_report.print_profile(profile_after)

if __name__ == "__main__":
    main()