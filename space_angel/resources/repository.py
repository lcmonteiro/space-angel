# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
from git import Repo
# -----------------------------------------------------------------------------
# GitRepository - adpter
# -----------------------------------------------------------------------------
class Repository:
    # ---------------------------------------------------------------
    # initialization
    # ---------------------------------------------------------------
    def __init__(self):
        self.__repo = Repo()

    # ---------------------------------------------------------------
    # checkout
    # ---------------------------------------------------------------
    def checkout(self, name, point = None):
        if point:
            self.__repo.git.checkout(point, b=name) 
        else:
            self.__repo.git.checkout(name)

    # ---------------------------------------------------------------
    # merge
    # ---------------------------------------------------------------
    def merge(self, point = None):
        self.__repo.git.merge(point)
        
    # ---------------------------------------------------------------
    # commint
    # ---------------------------------------------------------------
    def commit(self, msg):
        print('commit=', msg)
    
    # ---------------------------------------------------------------
    # ancestor
    # ---------------------------------------------------------------
    def ancestor(self, point1, point2):
        return self.__repo.git.merge_base(point1, point2)

    # ---------------------------------------------------------------
    # log 
    # ---------------------------------------------------------------
    def log(self, branch, end, method=None):
        # -------------------------------------------------
        #  log all       
        # -------------------------------------------------
        def log_all(end):
            for each in self.__repo.iter_commits(branch):
                if each.hexsha == end:
                    break
                yield each.hexsha
        # -------------------------------------------------
        # log with fibonacci steps
        # -------------------------------------------------
        def log_fib(end):
            def gen_fib():
                a,b = 1,1
                yield a
                yield b
                while True:
                    a, b = b, a + b
                    yield b
            g = gen_fib()
            c = next(g)
            for each in self.__repo.iter_commits(branch):
                if each.hexsha == end:
                    break
                if c > 1:
                    c -= 1
                    continue
                c = next(g)
                yield each.hexsha
        # -------------------------------------------------
        # select method
        # -------------------------------------------------
        return {
            None : log_all,
            'fib': log_fib
        }[method](end)

# -----------------------------------------------------------------------------
# end
# -----------------------------------------------------------------------------