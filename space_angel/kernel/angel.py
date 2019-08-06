# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
# external
# ---------------------------------------------------------
from os           import getcwd, chdir, mkdir
from os.path      import exists
from sys          import argv
from yaml         import safe_load   as loader 
from collections  import OrderedDict as Pipeline
# ---------------------------------------------------------
# internal
# ---------------------------------------------------------
from .timer       import Timer
from .bunch       import Bunch
from .logger      import Logger
# -----------------------------------------------------------------------------
# Angel - Implementation
# -----------------------------------------------------------------------------
class Angel:
    # -----------------------------------------------------
    # initialization
    # -----------------------------------------------------
    def __init__(self, config):
        # load configuration
        with open(config, 'r') as stream:
            self.__config = Bunch(loader(stream))
        # change workdirectory
        self.__set_workspace(self.__config.settings.workspace)
        # gate container
        self.__gates = Pipeline()
        # load pipeline
        self._pipeline()
        
    # -----------------------------------------------------
    # gate decorator 
    # -----------------------------------------------------
    def gate(self, name):
        def decorator(func):
            self.__gates[name] = Bunch({
                'call'  : func, 
                'force' : False
            }) 
            return func
        return decorator

    # -----------------------------------------------------
    # gate force decorator 
    # -----------------------------------------------------
    def gate_force(self, name):
        def decorator(func):
            self.__gates[name] = Bunch({
                'call'  : func, 
                'force' : True
            }) 
            return func
        return decorator
    
    # -----------------------------------------------------
    # run 
    # -----------------------------------------------------
    def run(self):
        timer = Timer(self.__config.settings.trigger)
        while(True):
            if timer.event():
                # enable angel attribute
                setattr(self, "angel", self.__config.settings)
                # process gates
                self._process()
                # disable angel attribute
                delattr(self, "angel")
            timer.sleep()
            
    # -----------------------------------------------------
    # process gates 
    # -----------------------------------------------------
    def _process(self):
        backlog = Logger('gates')
        # process each gate
        pipeline = True
        for name, gate in self.__gates.items():
            if pipeline or gate.force:
                log = Logger(name)
                # enable gate attribute
                setattr(self, "gate", self.__config.gates[name])
                # process gate
                try:
                    gate.call(self, log, backlog)
                    pipeline = True
                except:
                    pipeline = False
                # disable gate attribute
                delattr(self, "gate")
                # save log in backlog
                backlog(name, log)
        return backlog()

    # -----------------------------------------------------
    # helpers
    # -----------------------------------------------------
    def __set_workspace(self, path):
        if not exists(path):
            mkdir(path)
        chdir(path)

# -----------------------------------------------------------------------------
# Angel - Start
# -----------------------------------------------------------------------------
def start(angel):
    try:
        angel(argv[1]).run()
    except IndexError:
        print("Usage: angel.py [CONFIG_FILE].yaml")
    except KeyboardInterrupt:
        pass
# -----------------------------------------------------------------------------
# end
# -----------------------------------------------------------------------------