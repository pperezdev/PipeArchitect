from app.backend.Controller import scheduler

class Weekly:
    def __init__(self, type, day):
        self.day = day

    def set(self, define_interval, pipeline):
        schedule_fct = getattr(scheduler, f'set_schedule_{self.day}')
        schedule_fct(define_interval, pipeline)
