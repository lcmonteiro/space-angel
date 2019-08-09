# -----------------------------------------------------------------------------
# imports
# -----------------------------------------------------------------------------
from ..resources import Repository
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
                print('point=', point)
                # merge test point
                repo.merge(point)
                # process
                print('git::process', process_orig(self))
                # commint test result
                repo.commit("Checkpoint commit:")

    cls._process = process
    return cls

# -----------------------------------------------------------------------------
# end
# -----------------------------------------------------------------------------