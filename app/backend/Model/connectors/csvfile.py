import os
import csv
import json

class CsvConnector:
    def __init__(self, connector_name, properties):
        self.connector_name = connector_name

        self.path = properties["path"]
        self.example_file = f"{properties['example_file']}.csv"
        self.file = properties["file"]
        self.delimiter = properties["delimiter"]

    def open_csv(self, path):
        print(path)
        with open(path, "r", encoding="utf-8", newline='') as csvfile:
            cr = csv.reader(csvfile, delimiter=self.delimiter)
            content = list(cr)
        return content

    def connection_test(self):  
        path = os.path.join(self.path, self.example_file) 
        result = os.path.exists(path)
        return str(result)

    def get_schema(self, data):
        path = os.path.join(self.path, self.example_file)
        content = self.open_csv(path)
        return json.dumps(content[0])

    def execute(self, request, *args):
        file = self.file
        if file == "{output}":
            file = args.file
        print(file)
        output = os.path.join(self.path, file)
        return ""