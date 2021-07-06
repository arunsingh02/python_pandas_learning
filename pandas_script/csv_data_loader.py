
# Author: Arun Singh
# mailID: arunsingh.wave2@gmail.com

import pandas as pd
import matplotlib.pyplot as plt


class CSVReader:
    """
    Loading CSV file with `read_csv` and printing with Data Frames
    """
    def __init__(self):
        self.csv_file = "../pandas_data/reddit_vm.csv"

    @staticmethod
    def load_csv_data(csv_file: str = ""):
        """
        Loading CSV file
        iloc[0:10] - 0 to 9 (same as python)
        loc[0:10] - 0 to 10
        Returns: CSV data dict

        """
        csv_data = pd.read_csv(csv_file)
        pd.set_option("display.max_rows", 15)
        print("\n--- Filter testing ---\n")
        print(csv_data.loc[3])
        print(csv_data.iloc[1:13:2, 3])
        print(csv_data.iloc[1:13:2])
        print(csv_data.loc[(csv_data.score == 6) | (csv_data.comms_num > 0)])
        print(csv_data.comms_num.describe())
        print(csv_data.url.describe())
        print(csv_data.url.value_counts())
        print(csv_data.comms_num.unique())
        return csv_data

    def load_csv_data_into_table(self):
        """
        Not compulsory to load csv data into DataFrame
        Loading csv data into tabular format with the help of DataFrame
        Returns: None

        """
        csv_data = self.load_csv_data(self.csv_file)
        df = pd.DataFrame(csv_data)
        df.plot.scatter(y="score", x="comms_num")
        plt.tight_layout()
        plt.savefig('foo.pdf')
        plt.show()
        plt.close()
        print(f"\n --- Printing first 5 CSV data frame urls value ---\n\n{df['url'].head(5)}")
        print(f"\n --- Printing last 5 CSV data frame urls value ---\n\n{df['url'].tail(5)}")


if __name__ == '__main__':
    csv_obj = CSVReader()
    csv_obj.load_csv_data_into_table()
