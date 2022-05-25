from app.backend.Controller import scheduler

class Daily:
    def __init__(self, type, days):
        self.days = days

    def set(self, define_interval, pipeline):
        for day in self.days:
            schedule_fct = getattr(scheduler, f'set_schedule_{day}')
            schedule_fct(define_interval, pipeline)
