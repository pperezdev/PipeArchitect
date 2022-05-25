import os
import config 
import json
from app.backend.Controller import scheduler, builder

def modify_trigger(trigger):
    folder_path = os.path.abspath(os.path.join('.data', "triggers"))
    entries = os.listdir(folder_path)
    name = f'{trigger["name"]}.json'

    if name in entries:
        trigger_path = os.path.abspath(os.path.join(folder_path, name))
        with open(trigger_path, 'w') as outfile:
            json.dump(trigger, outfile,indent=4)
        build()


def run_connector(data):
    connector_name = data["connector_name"]
    return config.builder.run_connector(connector_name)

def get_schema(data):
    connector_name = data["connector_name"]
    return config.builder.get_schema(connector_name, data)

def execute_pipeline(data):
    pipeline_name = data["pipeline_name"]
    return config.builder.execute_pipeline(pipeline_name)

def build():
    config.builder = builder.Builder()
    config.builder.builder()

def run():
    config.trigger_schedule = scheduler.run_schedule()

def reboot_trigger():
    config.trigger_schedule.set()
