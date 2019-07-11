# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
from yaml         import safe_load   as config_load 
from kernel.timer import Timer
from collections  import OrderedDict as Pipeline
# -----------------------------------------------------------------------------
# Bunch : convert {"a": {"b":1 }} to a.b  
# -----------------------------------------------------------------------------
class Bunch(object):
    def __init__(self, d):
        for k, o in d.items():
            if isinstance(o, (list, tuple)):
                setattr(self, k, [self.__get_obj(x) for x in o])
            else:
                setattr(self, k, self.__get_obj(o))

    def __get_obj(self, o):
        return Bunch(o) if isinstance(o, dict) else o
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