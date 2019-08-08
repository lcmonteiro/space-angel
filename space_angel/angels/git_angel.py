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
            # checkout
            angel = monitor.branch + "-angel"
            try:
                repo.checkout(angel)
            except:
                repo.checkout(
                    angel, 
                    repo.ancestor(monitor.branch, monitor.origin))
            # find common ancestor [ branch and angel ]
            print(repo.log(repo.ancestor(monitor.branch, angel)))
            
            print(repo.ancestor(monitor.branch, angel))
            # merge previous ancestor [branch to angel]

        print("decorate::process")
        process_orig(self)


    cls._process = process
    return cls