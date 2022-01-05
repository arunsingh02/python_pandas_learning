
# Author: Arun Singh
# mailID: arunsingh.wave2@gmail.com

import pandas as pd
import json
import logging

LOGGER_NAME = "pandas.log"
_LOG = logging.getLogger()


class GenerateDataFrames:
    """
    Writing first pandas script
    """
    def __init__(self):
        self.file_path = "../pandas_data/data_frames.json"

    @staticmethod
    def data_frames_data_getter(file_path: str = ""):
        """
        Collect data frames details from given specified file path
        Args:
            file_path: string

        Returns: dict

        """
        if not file_path:
            _LOG.debug("Please provide the correct file path to generate data frames.")
            return {}
        with open(file_path) as file_reader:
            data_frames = json.load(file_reader)
        return data_frames

    def generate_data_frames(self):
        """
        Using pandas DataFrame function to generate tabular data
        Returns: None

        """
        data_frames = self.data_frames_data_getter(file_path=self.file_path)
        df = pd.DataFrame(data_frames, index=['2010', '2011', '2012'])
        print(f"----- Printing Data Frame -----\n{df}")
        print(f"\n----- Printing indexed value -----\n{df['Name'][1]}")

    @staticmethod
    def add_series():
        """
        Using Series (List data) with pandas
        """
        s1 = pd.Series([10, 20, 30], index=['2010', '2011', '2012'], name="Product A")
        print(f"\n\n----- Printing Series -----\n{s1}")


if __name__ == '__main__':
    df_obj = GenerateDataFrames()
    df_obj.generate_data_frames()
    df_obj.add_series()
