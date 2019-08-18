# -----------------------------------------------------------------------------
# imports
# -----------------------------------------------------------------------------
from ...resources import JUnit

# -----------------------------------------------------------------------------
# decorator
# -----------------------------------------------------------------------------
def gate_parser(name):
    Parser = {'junit': JUnit}[name]
    def wrap(func):
        # wrap function
        def wrap(self, log, backlog):
            # set gate attribute
            setattr(self, "parser", Parser(self.gate.output))
            # call function
            func(self, log, backlog)
            # remove gate attribute
            delattr(self, "parser")
    # return terminal wrap
    return wrap
# -----------------------------------------------------------------------------
# end
# -----------------------------------------------------------------------------