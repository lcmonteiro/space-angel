# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
from yaml         import safe_load as config_load 
from kernel.timer import Timer
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
        self.__gates = {}
        print(self.__config)
    
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
                data = {}
                for name, function in self.__gates.items():
                    function(data)
            timer.sleep()
# -----------------------------------------------------------------------------
# end
# -----------------------------------------------------------------------------