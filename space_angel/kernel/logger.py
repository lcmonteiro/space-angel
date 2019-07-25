# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
from functools import reduce
from .action   import Action
# -----------------------------------------------------------------------------
# Logger : 
# -----------------------------------------------------------------------------
class Logger(Action):
    # -----------------------------------------------------
    # initialization
    # -----------------------------------------------------
    def __init__(self):
        super().__init__()
        # attributes
        self._actions = {}
    
    # -----------------------------------------------------
    # get item - retrun the item by name
    # -----------------------------------------------------
    def __getitem__(self, name):
        if name not in self._actions:
            self._actions[name] = Logger()
        return self._actions[name]

    # -----------------------------------------------------
    # set item 
    # -----------------------------------------------------
    def __setitem__(self, name, action):
        self._actions[name] = action 

    # -----------------------------------------------------
    # call - log register
    # -----------------------------------------------------
    def __call__(self, path, action):
        try:
            # execute action
            a = action()
            # save action
            p = path.split('.')
            # action location
            l = reduce(lambda a, i: a[i], p[:-1], self)
            # 
            l[p[-1]] = a
        except:
            raise self
        return self
    
    # -----------------------------------------------------
    # representation 
    # -----------------------------------------------------
    def __repr__(self):
        return repr({
            'header' : self._header,
            'result' : self._result,
            'output' : self._output,
            'errors' : self._errors,
            'actions': self._actions})

# -----------------------------------------------------------------------------
# end
# -----------------------------------------------------------------------------