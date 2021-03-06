# -*- coding: utf8 -*-
"""
Timer
Credit: Benjamin Bengfort <benjamin@bengfort.com>
"""
import time


class Timer(object):
    """
    A context object timer. Usage:
        >>> with Timer() as timer:
        ...     do_something()
        >>> print timer.elapsed
    """

    def __init__(self, wall_clock=True):
        """
        If wall_clock is True then use time.time() to get the number of
        actually elapsed seconds. If wall_clock is False, use time.clock to
        get the process time instead.
        """
        self.wall_clock = wall_clock
        self.time = time.time if wall_clock else time.clock

        # Stubs for serializing an empty timer.
        self.started = None
        self.finished = None
        self.elapsed = 0.0

    def __enter__(self):
        self.started = self.time()
        return self

    def __exit__(self, typ, value, tb):
        self.finished = self.time()
        self.elapsed = self.finished - self.started

    def __str__(self):
        return '{} second(s)'.format(self.elapsed)
