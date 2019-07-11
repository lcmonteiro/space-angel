# -----------------------------------------------------------------------------
# imports
# -----------------------------------------------------------------------------
from resources import GitRepository
# -----------------------------------------------------------------------------
# helpers
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# decorator
# -----------------------------------------------------------------------------
def git_process(cls):
    # create a git repository instance
    repo = GitRepository()
    # save original process
    process_orig = cls._process
    def process(self):
        # process for each monitor
        for monitor in self._context.monitor:
            # checkout
            repo.checkout(monitor.branch)

        print("decorate::process")
        process_orig(self)


    cls._process = process
    return cls