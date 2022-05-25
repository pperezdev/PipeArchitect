from app.backend.Model.pipe_services.myApiServices import MyApiService
from app.backend.Model.pipe_services.copyData import CopyData


class PipeService:
    def __init__(self, service_name, name, description, retry, properties, input, output,depend_on, next):
        self.service_name = service_name
        self.name = name
        self.description = description
        self.retry = retry
        self.depend_on = depend_on
        self.next = next
        self.service = self.create_service(properties)
        self.size = len(self.depend_on)

    def create_service(self, properties):
        class_ = eval(self.service_name)
        return class_(**properties)

    def execute(self):
        self.service.execute()

    def execute_next(self):
        ...
