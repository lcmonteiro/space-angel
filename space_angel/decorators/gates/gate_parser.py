# -----------------------------------------------------------------------------
# imports
# -----------------------------------------------------------------------------
from ...resources import JUnit

# -----------------------------------------------------------------------------
# decorator
# -----------------------------------------------------------------------------
def gate_parser(func, name):
    PARSER = {'junit': JUnit}
    # wrap function
    def wrap(self, log, backlog):
        # set gate attribute
        setattr(self, "parser", PARSER[name](self.gate.output))
        # call function
        func(self, log, backlog)
        # remove gate attribute
        delattr(self, "parser")
    # return terminal wrap
    return wrap
# -----------------------------------------------------------------------------
# end
# -----------------------------------------------------------------------------