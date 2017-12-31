# -*- coding: utf8 -*-
"""
Timeit and timeout are about tracking and controlling performance issues.
Credits: Benjamin Bengfort <benjamin@bengfort.com>
"""
from functools import wraps
import signal
from .timer import Timer


class TimeoutError(Exception):
    """
    An operation timed out
    """
    pass


def timeit(func):
    """
    Returns the number of seconds that a function took along with the result
    """

    @wraps(func)
    def timer_wrapper(*args, **kwargs):
        """
        Inner function that uses the Timer context object
        """
        with Timer() as timer:
            result = func(*args, **kwargs)

        return result, timer

    return timer_wrapper


def timeout(seconds):
    """
    Raises a TimeoutError if a function does not terminate within
    specified seconds.
    """
    def _timeout_error(signal, frame):
        raise TimeoutError("Operation did not finish within \
        {} seconds".format(seconds))

    def timeout_decorator(func):

        @wraps(func)
        def timeout_wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _timeout_error)
            signal.alarm(seconds)
            try:
                return func(*args, **kwargs)
            finally:
                signal.alarm(0)

        return timeout_wrapper

    return timeout_decorator
