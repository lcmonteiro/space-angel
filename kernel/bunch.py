# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Bunch : convert {"a": {"b":1 }} to a.b  
# -----------------------------------------------------------------------------
class Bunch(object):
    # -----------------------------------------------------
    # initialization
    # -----------------------------------------------------
    def __init__(self, d):
        for k, o in d.items():
            if isinstance(o, (list, tuple)):
                setattr(self, k, [self.__get_obj(x) for x in o])
            else:
                setattr(self, k, self.__get_obj(o))
    
    # -----------------------------------------------------
    # items - return all attributes
    # -----------------------------------------------------
    def items(self):
        return self.__dict__.items()

    # -----------------------------------------------------
    # helpers
    # -----------------------------------------------------
    def __get_obj(self, o):
        return Bunch(o) if isinstance(o, dict) else o

# -----------------------------------------------------------------------------
# end
# -----------------------------------------------------------------------------