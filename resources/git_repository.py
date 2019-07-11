# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
from git import Repo
# -----------------------------------------------------------------------------
# GitRepository - adpter
# -----------------------------------------------------------------------------
class GitRepository:
    # -----------------------------------------------------
    # initialization
    # -----------------------------------------------------
    def __init__(self):
        self.__repo = Repo()

    # -----------------------------------------------------
    # checkout
    # -----------------------------------------------------
    def checkout(self, name):
        self.__repo.git.checkout(name)
