import pymongo

from src.web_data_extractor.writers.writer import Writer


class MongoWriter(Writer):

    def __init__(self, host, port, db_name, collection_name):
        self.host = host
        self.port = port
        self.db_name = db_name
        self.collection_name = collection_name

    def write(self, data):
        """
        Writes the final data into a mongo collection
        :param data:
        :return:
        """
        client = pymongo.MongoClient(host=self.host, port=self.port)
        db = client[self.db_name]
        collection = db[self.collection_name]

        collection.insert_many(data, ordered=False)
        client.close()
