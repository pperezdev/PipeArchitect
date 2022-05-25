from app.backend.Controller import builder

class MyApiService:
    def __init__(self, connector_name, properties_name):
        self.connector_name = connector_name
        self.properties_name = properties_name

    def execute(self):
        builder_obj = builder.Builder()
        builder_obj.builder_connectors()
        builder_obj.execute_connector(self.connector_name, self.properties_name)
