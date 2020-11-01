import requests
import pandas as pd

class HTMLParser:
    def __init__(self, url):
        self.url = url

    def parse(self):
        """Parse the file at given url and returns the generated csv file path
        Returns:
            a list of strings. Each string is the output of CSV file content
        """
        r = requests.get(self.url)

        dfs = pd.read_html(r.text)

        ret = []
        for df in dfs:
            ret.append(df.to_csv())

        return ret