# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
from yaml         import safe_load   as config_load 
from collections  import OrderedDict as Pipeline
from kernel.timer import Timer
from kernel.bunch import Bunch

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
        # set base context
        self._context = Bunch(self.__config["settings"])
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
                # reset context
                self._context = Bunch(self.__config["settings"])
                # process 
                self._process()
            timer.sleep()
            
    # -----------------------------------------------------
    # process gates 
    # -----------------------------------------------------
    def _process(self):
        data = {}
        for name, gate in self.__gates.items():
            # set context
            self._context = Bunch({
                "base" : self.__config["settings"],
                "gate" : self.__config["gates"][name]})
            # process gate
            gate(self, data)
    # -----------------------------------------------------
    # process gates 
    # -----------------------------------------------------
    def __(self, tag):
        return self.__config["settings"][tag]
# -----------------------------------------------------------------------------
# end
# -----------------------------------------------------------------------------