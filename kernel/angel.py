# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
from yaml         import safe_load   as config_load 
from kernel.timer import Timer
from collections  import OrderedDict as Pipeline
# -----------------------------------------------------------------------------
# Angel - Implementation
# -----------------------------------------------------------------------------
class Angel:
    # -----------------------------------------------------
    # initialization
    # -----------------------------------------------------
    def __init__(self, config):
        # load configuration
        with open(config, 'r') as stream:
            self.__config = config_load(stream)
        # gate container
        self.__gates = Pipeline()
        # load pipeline
        self._pipeline()
    
    # -----------------------------------------------------
    # gate decorator 
    # -----------------------------------------------------
    def gate(self, name):
        def decorator(func):
            self.__gates[name] = func
            return func
        return decorator
    
    # -----------------------------------------------------
    # run 
    # -----------------------------------------------------
    def run(self):
        timer = Timer(self.__config["settings"]["trigger"])
        while(True):
            if timer.event():
                self._process()
            timer.sleep()
            
    # -----------------------------------------------------
    # process gates 
    # -----------------------------------------------------
    def _process(self):
        data = {}
        for name, gate in self.__gates.items():
            gate(self, data)
    # -----------------------------------------------------
    # process gates 
    # -----------------------------------------------------
    def get(self, tag):
        return self.__config["settings"][tag]
# -----------------------------------------------------------------------------
# end
# -----------------------------------------------------------------------------