import requests
import pandas as pd
from flatten_json import flatten

class APIParser:
    def __init__(self, url, json_format):
        self.url = url
        self.json_format = json_format

    def parse(self):
        """Parse the file at given url and returns the generated csv file path
        Returns:
            a list of strings. Each string is the output of CSV file content
        """

        r = requests.get(self.url)
        data = r.json()

        if self.json_format == 'flat':
            data = flatten(data)

        df = pd.json_normalize(data)

        return df.to_csv()