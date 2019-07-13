# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
from re         import match
from time       import sleep
from time       import time
from datetime   import datetime
from contextlib import suppress
# -----------------------------------------------------------------------------
# Angel - Implementation
# -----------------------------------------------------------------------------
class Timer:
    __TIME_PATTERN = "%Y/%m/%d (%w) %H:%M:%S"
    # -----------------------------------------------------
    # initialization
    # -----------------------------------------------------
    def __init__(self, pattern):
        # event pattern
        self.__pattern = pattern 
        # init counter
        self.__counter = float(int(time()))

    # -----------------------------------------------------
    # event
    # -----------------------------------------------------
    def event(self):
        # get counter time
        time = datetime.fromtimestamp(self.__counter)
        # format time string
        time = time.strftime(Timer.__TIME_PATTERN)
        # check timer
        return match(self.__pattern, time)
        
    # -----------------------------------------------------
    # sleep
    # -----------------------------------------------------
    def sleep(self):
        # increment counter
        self.__counter += 1
        # sleep
        with suppress(IOError):
            sleep(self.__counter - time())

# -----------------------------------------------------------------------------
# end
# -----------------------------------------------------------------------------
