from src.web_data_extractor.web_extractor import WebExtractor

if __name__ == '__main__':
    rules = {
        'url' : 'https://recetasdecocina.elmundo.es/tabla-calorias',
        'rules' : [
            {
                'name' : 'alimento',
                'tags' : ['tr', 'td'],
                'attrs' : {},
                'type': 0
            }
        ]
    }
    WebExtractor.extract_from_dict(rules)