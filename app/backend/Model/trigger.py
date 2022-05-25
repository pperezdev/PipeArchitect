from app.backend.Model.trigger_properties.Daily import Daily
from app.backend.Model.trigger_properties.Weekly import Weekly

class Trigger:
    def __init__(self, type, name, description, schedule_interval, schedule_time,triggered_pipeline):
        self.type = type
        self.name = name
        self.description = description
        self.schedule_time = schedule_time
        self.schedule_interval = self.define_interval(schedule_interval)
        self.triggered_pipeline_name = triggered_pipeline
        self.triggered_pipeline = []

    def define_interval(self, schedule_interval_string):
        schedule_interval_type = schedule_interval_string["type"]
        class_ = eval(schedule_interval_type)
        schedule_interval = class_(**schedule_interval_string)
        return schedule_interval

    def set(self, pipelines):
        self.triggered_pipeline = []
        for pipeline in pipelines:
            for name in self.triggered_pipeline_name:
                if pipeline.name == name:
                    self.triggered_pipeline.append(pipeline)
                    self.schedule_interval.set(self.schedule_time , pipeline)
        