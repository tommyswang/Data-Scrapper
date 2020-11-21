import requests
import pandas as pd
from flatten_json import flatten


class APIParser:
    """Takes in url and json_format (flat, structured)"""

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
            if isinstance(data, list):
                for i, d in enumerate(data):
                    data[i] = flatten(d)
            else:
                data = flatten(data)

        df = pd.json_normalize(data)

        ret = []
        ret.append(df.to_csv())

        return ret
