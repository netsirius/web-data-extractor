import requests
from bs4 import BeautifulSoup

from src.web_data_extractor.extractors.dict_web_extractor import DictWebExtractor
from src.web_data_extractor.extractors.extractor import Extractor
from src.web_data_extractor.extractors.json_web_extractor import JsonWebExtractor
from src.web_data_extractor.pipeline.pipeline import Pipeline
from src.web_data_extractor.transformations.transformation import Transformation
from src.web_data_extractor.writers.CsvWriter import CsvWriter
from src.web_data_extractor.writers.MongoWriter import MongoWriter
from src.web_data_extractor.writers.writer import Writer


class WebExtractor:

    @staticmethod
    def create_pipeline(extractor: Extractor, transformation: Transformation, writer: Writer):
        """
        Define a extraction pipeline
        :param extractor: Instance of web Extractor as a source (JsonExtractor, DictExtractor...)
        :param transformation: Instance of Transformation with defined transform method
        :param writer: Instance of a Writer as a data destination (MongoWriter, CsvWriter...)
        :return: Instance of a Pipeline
        """
        return Pipeline(extractor=extractor, transformation=transformation, writer=writer)

    @staticmethod
    def extract_from_json(rules_json):
        """
        Extract web data from a given json of rules
        :param rules_json: rules in json format
        :return:
        """
        extractor = JsonWebExtractor()
        return extractor.extract_data(rules_json)

    @staticmethod
    def extract_from_dict(rules_dict):
        """
        Extract web data from a given dict of rules
        :param rules_dict: rules in dict format
        :return:
        """
        extractor = DictWebExtractor()
        return extractor.extract_data(rules_dict)

    @staticmethod
    def write_to_mongo(host, port, db, collection, data):
        """
        Write extracted data documents to mongo collection
        :param host: mongodb hostname
        :param port: mongodb port number
        :param db: mongodb database name
        :param collection: mongo db collection name
        :param data: documents to write
        :return:
        """
        mongo_writer = MongoWriter(host=host, port=port, db_name=db, collection_name=collection)
        mongo_writer.write(data)

    @staticmethod
    def write_to_csv(file_path, data):
        """
        Write extracted data documents to CSV file
        :param file_path: path to csv file
        :param data: data to write
        :return:
        """
        csv_writer = CsvWriter(path=file_path)
        csv_writer.write(data)
