# -----------------------------------------------------------------------------
# imports
# -----------------------------------------------------------------------------
from ..resources import Repository
# -----------------------------------------------------------------------------
# decorator
# -----------------------------------------------------------------------------
def git_angel(cls):
    # ---------------------------------------------------------------
    # helpers
    # ---------------------------------------------------------------
    # log message
    # ---------------------------------------------------------------
    def summary(rep):
        msg = ''
        for gate, log in rep:
            if len(log) > 0:
                msg += ' #{g}={r}'.format(g=gate, r=log.result())
        return msg
    # ---------------------------------------------------------------
    # process
    # ---------------------------------------------------------------
    # create a git repository instance
    repo = Repository()
    # save original process
    process_orig = cls._process
    def process(self):
        # process for each monitor
        for monitor in self.angel.monitor:
            angel  = monitor.branch + "-angel"
            branch = monitor.branch
            origin = monitor.origin
            # checkout angel
            try:
                repo.checkout(angel)
            except:
                repo.checkout(
                    angel, 
                    repo.ancestor(branch, origin))
            # find test points
            for point in reversed(
                list(repo.log(branch, repo.ancestor(branch, angel), 'fib'))):
                # merge test point
                repo.merge(point)
                # process
                rep = process_orig(self)
                # commint test result
                repo.commit("Checkpoint commit:{s}".format(s=summary(rep())))

    cls._process = process
    return cls

# -----------------------------------------------------------------------------
# end
# -----------------------------------------------------------------------------