"""
Testing the decorators utility package.
"""

import unittest
import time
from awesomedecorators import memoized, timeit, timeout, Timer, TimeoutError


class DecoratorsTests(unittest.TestCase):
    """
    Basic decorators utility tests.
    """

    def test_memoized(self):
        """
        Test the memoized property
        """

        class Thing(object):

            @memoized
            def attr(self):
                return 42

        thing = Thing()
        self.assertFalse(hasattr(thing, '_attr'))
        self.assertEqual(thing.attr, 42)
        self.assertTrue(hasattr(thing, '_attr'))

    def test_timeit(self):
        """
        Test the timeit decorator
        """

        @timeit
        def myfunc():
            return 42

        output = myfunc()
        self.assertEqual(len(output), 2)
        result, timer = output
        self.assertEqual(result, 42)
        self.assertTrue(isinstance(timer, Timer))

    def test_timeout(self):
        """
        Test the timeout decorator
        """

        @timeout(1)
        def myfunc():
            # Some function that should take more than 1 second
            time.sleep(2)

        with self.assertRaises(TimeoutError) as context:
            myfunc()
        self.assertTrue('Operation did not finish within'
                        in str(context.exception))

    def test_timeout_elapsed(self):
        """
        Test the timeout decorator: elapsed value
        """

        @timeout(2)
        def myfunc():
            # Some function that should take more than 1 second
            time.sleep(1)

        with Timer() as timer:
            myfunc()
        self.assertGreater(timer.elapsed, 1.0)
        print(timer)
