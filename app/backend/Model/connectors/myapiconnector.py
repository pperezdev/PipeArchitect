import requests

class MyAPIConnector:
    def __init__(self, connector_name, properties):
        self.connector_name = connector_name

        self.URL = properties["url"]

    def connection_test(self):
        full_url = f"{self.URL}/"
        result = requests.get(full_url)
        return result.content

    def get_schema(self, data):
        full_url = f"{self.URL}/get-schema"
        result = requests.get(full_url)
        return result.content

    def execute(self, data):
        full_url = f"{self.URL}/my-request"
        body = {"request_name" : data}
        result = requests.post(full_url, json=body)
        return result.content