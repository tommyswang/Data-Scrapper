import tabula
import tempfile


class PdfParser:
    def __init__(self, path):
        self.path = path

    def parse(self):
        """Parse the file at given path and returns the generated csv file path

        Returns:
            a list of strings. Each string is the output of CSV file content
        """
        dfs = tabula.read_pdf(self.path, pages='all')

        ret = []
        for df in dfs:
            ret.append(df.to_csv())

        return ret
