# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Angel - Implementation
# -----------------------------------------------------------------------------
class Angel:
    # -----------------------------------------------------
    # initialization
    # -----------------------------------------------------
    def __init__(self):
        # gate container
        self.__gates = {}
    
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
        data = {}
        for name, function in self.__gates.items():
            function(data)
# -----------------------------------------------------------------------------
# end
# -----------------------------------------------------------------------------