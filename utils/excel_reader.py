import pandas as pd


def get_test_data(file_path, sheet_name):

    data = pd.read_excel(
        file_path,
        sheet_name=sheet_name
    )

    # Remove completely empty columns

    data = data.dropna(
        axis=1,
        how="all"
    )

    # Remove completely empty rows

    data = data.dropna(
        axis=0,
        how="all"
    )

    return data.values.tolist()