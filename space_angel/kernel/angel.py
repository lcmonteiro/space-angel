# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
from yaml         import safe_load   as config_load 
from collections  import OrderedDict as Pipeline
# ---------------------------------------------------------
# local
# ---------------------------------------------------------
from .timer       import Timer
from .bunch       import Bunch
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
            self.__config = Bunch(config_load(stream))
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
        timer = Timer(self.__config.settings.trigger)
        while(True):
            if timer.event():
                # enable angel attribute
                setattr(self, "angel", self.__config.settings)
                # process gates
                self._process()
                # disable angel attribute
                delattr(self, "angel")
            timer.sleep()
            
    # -----------------------------------------------------
    # process gates 
    # -----------------------------------------------------
    def _process(self):
        data = {}
        for name, gate in self.__gates.items():
            # enable gate attribute
            setattr(self, "gate", self.__config.gates[name])
            # process gate
            gate(self, data)
            # disable gate attribute
            delattr(self, "gate")
        return data

    # -----------------------------------------------------
    # process gates 
    # -----------------------------------------------------
    def __(self, tag):
        return self.__config["settings"][tag]
# -----------------------------------------------------------------------------
# end
# -----------------------------------------------------------------------------