from multiprocessing import Process

def execute_pipeline(pipeline, *args):
    p = Process(target=pipeline.execute)
    p.start()