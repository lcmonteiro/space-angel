# -----------------------------------------------------------------------------
# imports
# -----------------------------------------------------------------------------
from ..resources import Terminal
# -----------------------------------------------------------------------------
# helpers
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# decorator
# -----------------------------------------------------------------------------
def terminal_gate(func):
    # wrap function
    def wrap(self, log, backlog):
        # set gate attribute
        setattr(self, "terminal", Terminal(self.gate.commands))
        # call function
        func(self, log, backlog)
        # remove gate attribute
        delattr(self, "terminal")
    # return terminal wrap
    return wrap
# -----------------------------------------------------------------------------
# end
# -----------------------------------------------------------------------------