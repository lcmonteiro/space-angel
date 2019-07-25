# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Action : 
# -----------------------------------------------------------------------------
class Action(object):
    # -----------------------------------------------------
    # initialization
    # -----------------------------------------------------
    def __init__(self):
        # attributes
        self._header = None
        self._result = None
        self._output = None
        self._errors = None

    # -----------------------------------------------------
    # call - log register
    # -----------------------------------------------------
    def __call__(self, 
        header= None, result=None, output=None, errors=None):
        self._header = header
        self._result = result
        self._output = output
        self._errors = errors
        return self
    
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