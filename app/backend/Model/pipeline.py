from app.backend.Model.pipe_services.pipeService import PipeService
import asyncio

class Pipeline:
    def __init__(self, type, name, description, services, **kwargs):
        self.type = type
        self.name = name
        self.description = description

        self.services = self.create_services(services)

    def create_services(self, services):
        list_services = []
        for service in services:
            pipe_service = PipeService(**service)
            list_services.append(pipe_service)
        return list_services

    def execute(self):
        print(f"------ PIPELINE {self.name} ------")
        print("STARTED ...")
        services_no_depends = [service for service in  self.services if service.size == 0]

        for service_no_depends in services_no_depends:
            service_no_depends.execute()
        print("DONE ...")