from pathlib import Path
import pandas as pd


class Olist:
    """
    The Olist class provides methods to interact with Olist's e-commerce data.

    Methods:
        get_data():
            Loads and returns a dictionary where keys are dataset names (e.g., 'sellers', 'orders')
            and values are pandas DataFrames loaded from corresponding CSV files.

        ping():
            Prints "pong" to confirm the method is callable.
    """
    def get_data(self):
        """
        This function returns a Python dict.
        Its keys should be 'sellers', 'orders', 'order_items' etc...
        Its values should be pandas.DataFrames loaded from csv files
        """
        csv_path = Path("~/.workintech/olist/data/csv").expanduser()
        data = {}

        for path in csv_path.iterdir():
            if path.suffix == ".csv":
                key = path.stem.removeprefix("olist_").removesuffix("_dataset")
                data[key] = pd.read_csv(path)

        return data


    def ping(self):
        """
        You call ping I print pong.
        """
        print("pong")
