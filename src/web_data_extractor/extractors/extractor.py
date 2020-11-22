import logging


def check_rules_schema(parse_func):
    def check_schema(*args, **kwargs):
        result = parse_func(*args, **kwargs)
        if 'url' in result and 'rules' in result:
            rules = result['rules']
            if isinstance(rules, list):
                areValidRules = True
                for rule in rules:
                    if 'name' not in rule \
                            or 'tags' not in rule \
                            or 'attrs' not in rule\
                            or 'type' not in rule:
                        areValidRules = False
                if areValidRules:
                    return result
                else:
                    logging.error("error schema")
                    raise Exception("Bad Schema")
            else:
                logging.error("error schema")
                raise Exception("Bad Schema")
        else:
            logging.error("error schema")
            raise Exception("Bad Schema")
    return check_schema


class Extractor:

    def parse_rules(self, input_rules):
        pass

    def extract_data(self, rules):
        pass
