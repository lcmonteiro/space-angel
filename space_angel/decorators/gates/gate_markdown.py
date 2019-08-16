# -----------------------------------------------------------------------------
# imports
# -----------------------------------------------------------------------------
from ...resources import Markdown

# -----------------------------------------------------------------------------
# decorator
# -----------------------------------------------------------------------------
def gate_markdown(func):
    # wrap function
    def wrap(self, log, backlog):
        # set gate attribute
        setattr(self, "markdown", Markdown(self.gate.output))
        # call function
        func(self, log, backlog)
        # remove gate attribute
        delattr(self, "markdown")
    # return terminal wrap
    return wrap
# -----------------------------------------------------------------------------
# end
# -----------------------------------------------------------------------------