# -----------------------------------------------------------------------------
# imports
# -----------------------------------------------------------------------------
from resources import Repository
# -----------------------------------------------------------------------------
# helpers
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# decorator
# -----------------------------------------------------------------------------
def git_angel(cls):
    # create a git repository instance
    repo = Repository()
    # save original process
    process_orig = cls._process
    def process(self):
        # process for each monitor
        for monitor in self._context.monitor:
            # checkout
            try:
                repo.checkout(
                    monitor.branch + "-angel")
            except:
                repo.checkout(
                    monitor.branch + "-angel", 
                    repo.ancestor(monitor.branch, monitor.origin))

        print("decorate::process")
        process_orig(self)


    cls._process = process
    return cls