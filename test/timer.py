import time

class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""

class Timer:
    def __init__(self, logger=print):
        self._start_time = None
        self._elapsed_time = None
        self.logger = logger
    
    def start(self):
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")
        
        self._start_time = time.perf_counter()

    def stop(self):
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")
        
        self._elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None

        if self.logger:
            self.logger(f"Elapsed time: {self._elapsed_time:0.4f} seconds")

        return self._elapsed_time
