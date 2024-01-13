import pandas as pd

def load_data(file_name):
    df = pd.read_csv(file_name)

    # Replace spaces with underscores in column names
    df.columns = df.columns.str.replace(' ', '_')

    return df