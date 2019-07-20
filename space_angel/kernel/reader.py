# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Imports  
# -----------------------------------------------------------------------------
from threading import Thread
from queue     import Queue, Empty
# -----------------------------------------------------------------------------
# Reader: 
# -----------------------------------------------------------------------------
class Reader:
    # -----------------------------------------------------
    # initialization
    # -----------------------------------------------------
    def __init__(self, stream, timeout = 36000):
        self.__timeout = timeout
        self.__queue   = Queue()
        # create async task to read the stream
        self.__task = Thread(
            target = Reader.__populate, 
            args   = (self.__queue, stream),
            daemon = True)
        # start task
        self.__task.start()
    # -----------------------------------------------------
    # readline
    # -----------------------------------------------------
    def readline(self):
        try:
            return self.__queue.get(timeout = self.__timeout)
        except Empty:
            return None

    # -----------------------------------------------------
    # readlines
    # -----------------------------------------------------
    def readlines(self):
        try:
            while True:
                yield self.__queue.get(block=False)
        except Empty:
            pass

    # -----------------------------------------------------
    # populate
    # -----------------------------------------------------
    @staticmethod
    def __populate(queue, stream):
        for line in iter(stream.readline, b''):
            queue.put(line.decode())

# -----------------------------------------------------------------------------
# end
# -----------------------------------------------------------------------------