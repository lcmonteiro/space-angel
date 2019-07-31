# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Action : 
# -----------------------------------------------------------------------------
class Action(object):
    # -----------------------------------------------------
    # initialization
    # -----------------------------------------------------
    def __init__(self, header=None):
        # attributes
        self._header = header
        self._result = 0
        self._output = []
        self._errors = []

    # -----------------------------------------------------
    # call - log register
    # -----------------------------------------------------
    def __call__(self, result=None, output=None, errors=None):
        if result is not None:
            self._result = result  
        if output is not None:
            self._output = output
        if errors is not None:
            self._errors = errors
        return self
    
    # -----------------------------------------------------
    # get result 
    # -----------------------------------------------------
    def result(self):
        return self._result
    # -----------------------------------------------------
    # representation 
    # -----------------------------------------------------
    def __repr__(self):
        return repr({
            'header': self._header,
            'result': self._result,
            'output': self._output,
            'errors': self._errors})

# -----------------------------------------------------------------------------
# end
# -----------------------------------------------------------------------------