# -----------------------------------------------------------------------------
# imports
# -----------------------------------------------------------------------------
from resources import Terminal
# -----------------------------------------------------------------------------
# helpers
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# decorator
# -----------------------------------------------------------------------------
def terminal_gate(func):
    # wrap function
    def wrap(self, data):
        # set gate attribute
        setattr(self, "terminal", Terminal(self._context.gate.commands))
        # call function
        func(self, data)
        # remove gate attribute
        delattr(self, "terminal")
    # return terminal wrap
    return wrap
# -----------------------------------------------------------------------------
# end
# -----------------------------------------------------------------------------