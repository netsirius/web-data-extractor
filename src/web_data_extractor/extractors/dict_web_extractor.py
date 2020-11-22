import requests
from bs4 import BeautifulSoup

from src.web_data_extractor.extractors.extractor import Extractor, check_rules_schema


class DictWebExtractor(Extractor):

    @check_rules_schema
    def parse_rules(self, input_rules):
        return input_rules

    def extract_data(self, rules):
        rules_dict = self.parse_rules(input_rules=rules)
        page_request = requests.get(rules_dict['url'])

        soup = BeautifulSoup(page_request.content, 'html5lib')

        result = {}

        for rule in rules_dict['rules']:
            elementName = rule['name']
            elementType = rule['type']
            elementTags = rule['tags']
            elementAttrs = rule['attrs']

            if elementType == 0:
                result[elementName] = soup.find(elementTags, attrs=elementAttrs)