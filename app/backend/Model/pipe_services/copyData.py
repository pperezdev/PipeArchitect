from app.backend.Controller import builder

class CopyData:
    def __init__(self, source, destination, mappage):
        self.source = source
        self.destination = destination
        self.mappage = mappage

    def execute(self):
        builder_obj = builder.Builder()
        builder_obj.builder_connectors()
        builder_obj.execute_copy_data_connector(self.destination, "")