from src.web_data_extractor.writers.writer import Writer


class CsvWriter(Writer):

    def __init__(self, path):
        self.path = path

    def write(self, data):
        """
        Writes the final data into a CSV file
        :param data:
        :return:
        """
        pass
