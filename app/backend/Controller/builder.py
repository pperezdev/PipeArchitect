import config
from app.backend.Model.pipeline import Pipeline
from app.backend.Model.trigger import Trigger
from app.backend.Model.connector import Connector
from app.backend.Controller import executor
import asyncio
import json
import os

class Builder:
    def __init__(self):
        self.connectors = []
        self.pipelines = []
        self.triggers = []

    def open_files(self, path, fct):
        objects = []

        folder_path = os.path.abspath(os.path.join('data', path))
        entries = os.listdir(folder_path)
        for entry in entries:
            file_path = os.path.join(folder_path, entry)
            file = open(file_path, encoding='utf-8')
            data = json.load(file)
            objects.append(fct(data))

        return objects

    def build_variables(self):
        ...

    def build_connectors(self):
        return self.open_files("connectors", self.create_connector)

    def build_pipeline(self):
        return self.open_files("pipelines", self.create_pipeline)

    def build_trigger(self):
        return self.open_files("triggers", self.create_trigger)

    def create_connector(self, data):
        m_connector = Connector(**data)
        return m_connector

    def create_trigger(self, data):
        m_trigger = Trigger(**data)
        m_trigger.set(self.pipelines)
        return m_trigger

    def create_pipeline(self, data):
        m_pipeline = Pipeline(**data)
        return m_pipeline

    def builder(self):
        self.connectors = self.build_connectors()
        self.pipelines = self.build_pipeline()
        self.triggers = self.build_trigger()

    def builder_connectors(self):
        self.connectors = self.build_connectors()

    def find_and_execute(self, execution_name, execution_list, execution_item_name, fct_name, *args,**kwargs):
        pointed_execution = [execution for execution in execution_list if execution.name == execution_item_name]
        if len(pointed_execution) == 0:
            return f"ERROR, YOUR {execution_name} '{execution_item_name}' DOESNT EXIST"
        fct = getattr(pointed_execution[0], fct_name)
        return fct(*args, **kwargs)
    
    def find_and_execute_pipeline_async(self, pipeline_name, pipeline_list, pipeline_item_name, *args,**kwargs):
        pointed_pipeline = [pipeline for pipeline in pipeline_list if pipeline.name == pipeline_item_name]
        if len(pointed_pipeline) == 0:
            return f"ERROR, YOUR {pipeline_name} '{pipeline_item_name}' DOESNT EXIST"
        executor.execute_pipeline(pointed_pipeline[0], args, kwargs)
        return "EXECUTE PIPELINE"

    def run_connector(self, connector_name):
        return self.find_and_execute("CONNECTOR", self.connectors, connector_name, "connection_test")

    def execute_connector(self, connector_name, data):
        return self.find_and_execute("CONNECTOR", self.connectors, connector_name, "execute", data)

    def execute_copy_data_connector(self, connector_name, data):
        return self.find_and_execute("CONNECTOR", self.connectors, connector_name, "execute_copy_data_connector", data)

    def get_schema(self, connector_name, data):
        return self.find_and_execute("CONNECTOR", self.connectors, connector_name, "get_schema", data)

    def execute_pipeline(self, pipeline_name):
        return self.find_and_execute_pipeline_async("PIPELINE", self.pipelines, pipeline_name)