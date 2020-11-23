from src.web_data_extractor.extractors.extractor import Extractor
from src.web_data_extractor.transformations.transformation import Transformation
from src.web_data_extractor.writers.writer import Writer


class Pipeline:

    def __init__(self, extractor: Extractor, transformation: Transformation, writer: Writer):
        self.r = extractor
        self.t = transformation
        self.w = writer

    def __init__(self, reader, writer):
        self.r = reader
        self.w = writer

    def run_pipeline(self):
        """
        Executes the entire pipeline, extracting data with the Extractor, transforming the data
        and finally writing the data to destination
        :return:
        """
        pass
