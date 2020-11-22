import requests
from bs4 import BeautifulSoup

from src.web_data_extractor.extractors.dict_web_extractor import DictWebExtractor
from src.web_data_extractor.extractors.json_web_extractor import JsonWebExtractor
from src.web_data_extractor.pipeline.pipeline import Pipeline


class WebExtractor:

    @staticmethod
    def create_pipeline(reader, writer):
        return Pipeline(reader, writer)

    @staticmethod
    def extract_from_json(rules_json):
        extractor = JsonWebExtractor()
        return extractor.extract_data(rules_json)

    @staticmethod
    def extract_from_dict(rules_dict):
        extractor = DictWebExtractor()
        return extractor.extract_data(rules_dict)

    def write_to_mongo(self, db, collection, host, data):
        pass
