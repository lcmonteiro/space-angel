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
    def __init__(self, header):
        super().__init__(header)
        # attributes
        self._actions = {}
    
    # -----------------------------------------------------
    # get item - retrun the item by name
    # -----------------------------------------------------
    def __getitem__(self, name):
        if name not in self._actions:
            self._actions[name] = Logger(name)
        return self._actions[name]

    # -----------------------------------------------------
    # set item 
    # -----------------------------------------------------
    def __setitem__(self, name, action):
        self._actions[name] = action 

    # -----------------------------------------------------
    # call - log register
    # -----------------------------------------------------
    def __call__(self, path=None, action=None, base_result=0):
        # execute
        if action is None:
            # update result recursive 
            action = self.__update()
        else:
            # insert action in path
            action = self.__insert(path.split('.'), action())
        # validation
        if action.result() < base_result:
            raise Exception("{actual} < {expect}".format(
                actual = action.result(),
                expect = base_result))
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

    # -----------------------------------------------------
    # update results 
    # -----------------------------------------------------
    def __update(self):
        result = 1
        # compute result
        for name, action in self._actions.items():
            if isinstance(action, Logger):
                action()
            result *= action.result() 
        # update result
        return super().__call__(result)

    # -----------------------------------------------------
    # insert action 
    # -----------------------------------------------------
    def __insert(self, path, action):
        # save action on location
        reduce(lambda a, i: a[i], path[:-1], self)[
            path[-1]
        ] = action
        return action
# -----------------------------------------------------------------------------
# end
# -----------------------------------------------------------------------------