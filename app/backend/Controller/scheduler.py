import threading
import time
import schedule
from app.backend.Controller import executor

def set_schedule_day(schedule_time, pipeline):
    schedule.every().day.at(schedule_time).do(executor.execute_pipeline, pipeline)

def set_schedule_monday(schedule_time, pipeline):
    schedule.every().monday.at(schedule_time).do(executor.execute_pipeline, pipeline)

def set_schedule_tuesday(schedule_time, pipeline):
    schedule.every().tuesday.at(schedule_time).do(executor.execute_pipeline, pipeline)

def set_schedule_wednesday(schedule_time, pipeline):
    schedule.every().wednesday.at(schedule_time).do(executor.execute_pipeline, pipeline)

def set_schedule_thursday(schedule_time, pipeline):
    schedule.every().thursday.at(schedule_time).do(executor.execute_pipeline, pipeline)

def set_schedule_friday(schedule_time, pipeline):
    schedule.every().friday.at(schedule_time).do(executor.execute_pipeline, pipeline)

def set_schedule_saturday(schedule_time, pipeline):
    schedule.every().saturday.at(schedule_time).do(executor.execute_pipeline, pipeline)

def set_schedule_sunday(schedule_time, pipeline):
    schedule.every().sunday.at(schedule_time).do(executor.execute_pipeline, pipeline)

def run_schedule():
    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):
        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                schedule.run_pending()
                time.sleep(1)

    continuous_thread = ScheduleThread()
    continuous_thread.start()
    return cease_continuous_run