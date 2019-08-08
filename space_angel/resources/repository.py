# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
from git import Repo
# -----------------------------------------------------------------------------
# GitRepository - adpter
# -----------------------------------------------------------------------------
class Repository:
    # -----------------------------------------------------
    # initialization
    # -----------------------------------------------------
    def __init__(self):
        self.__repo = Repo()

    # -----------------------------------------------------
    # checkout
    # -----------------------------------------------------
    def checkout(self, name, point = None):
        if point:
            self.__repo.git.checkout(point, b=name) 
        else:
            self.__repo.git.checkout(name)
    
    # -----------------------------------------------------
    # ancestor
    # -----------------------------------------------------
    def ancestor(self, point1, point2):
        return self.__repo.git.merge_base(point1, point2)

    # -----------------------------------------------------
    # log 
    # -----------------------------------------------------
    def log(self, end, method=None):
        for each in self.__repo.iter_commits('head'):
            if each.hexsha == end:
                break
            print(each.hexsha)
            
    def __log_all(self, end, method=None):
        for each in self.__repo.iter_commits('head'):
            if each.hexsha == end:
                break
            print(each.hexsha)

# -----------------------------------------------------------------------------
# end
# -----------------------------------------------------------------------------