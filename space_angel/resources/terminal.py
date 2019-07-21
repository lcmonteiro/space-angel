# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------------------------
# Imports
# -------------------------------------------------------------------------------------------------
# external
# ---------------------------------------------------------
from subprocess import Popen
from subprocess import PIPE
from platform   import system
from parse      import parse
from os         import linesep
from ast        import literal_eval
# ---------------------------------------------------------
# internal
# ---------------------------------------------------------
from ..kernel   import Reader
# -------------------------------------------------------------------------------------------------
# Terminal - context
# -------------------------------------------------------------------------------------------------
class Terminal:
    # -------------------------------------------------------------------------
    # Command object
    # -------------------------------------------------------------------------
    class Command(object):
        # -------------------------------------------------
        # initialization
        # -------------------------------------------------
        def __init__(self, shell, cmd):
            self.__shell = shell
            self.__cmd   = cmd

        # -------------------------------------------------
        # execute
        # -------------------------------------------------
        def __call__(self):
            return self.__shell(self.__cmd)

    # -------------------------------------------------------------------------
    # Shell object
    # -------------------------------------------------------------------------
    class Shell(object):
        __PATTERN = ""
        # -------------------------------------------------
        # initialization
        # -------------------------------------------------
        def __init__(self):
            # select a context
            context = 'cmd' if system() == 'Windows' else 'sh' 
            # open a context
            self.__proc = Popen(
                context, stdin=PIPE, stdout=PIPE, stderr=PIPE, bufsize=0)
            #
            self.__stdout = Reader(self.__proc.stdout) 
            self.__stderr = Reader(self.__proc.stderr) 
        
        # -------------------------------------------------
        # call
        # -------------------------------------------------
        def __call__(self, cmd):
            # ---------------------------------------------
            # process
            # ---------------------------------------------
            class Process:
                # command template ------------------------
                __CMD = '{c} && echo "{t}" || echo "{f}" {n}'

                # result  template ------------------------
                __RES = '--!!({c})==>>({r})??--'

                # initialization --------------------------
                def __init__(self, cmd):
                    self.__res  = False
                    self.__cmd  = cmd
                    self.__line = Process.__CMD.format(
                        c = cmd,
                        t = Process.__RES.format(c=cmd, r=True ),
                        f = Process.__RES.format(c=cmd, r=False),
                        n = linesep 
                    )

                # command line ----------------------------
                def __bytes__(self):
                    return self.__line.encode()

                # process result --------------------------
                def __bool__(self):
                    return self.__res

                # match result ----------------------------
                def __eq__(self, line):
                    try:
                        self.__res = literal_eval(parse(
                            Process.__RES.format(
                                c = self.__cmd, r = '{r}'
                            ), line)['r']
                        )
                    except:
                        return False
                    return True
            # ---------------------------------------------
            # execute
            # ---------------------------------------------
            proc, out, err = Process(cmd), [], [] 
            # send
            self.__proc.stdin.write(bytes(proc))
            # wait result
            for line in iter(self.__stdout.readline, proc):
                out += line.splitlines()
            # wait result
            for line in self.__stderr.readlines():
                err += line.splitlines()
            # return data
            return (bool(proc), {'out': out, 'err': err})

        # -------------------------------------------------
        # delete
        # -------------------------------------------------
        def __del__(self):
            self.__proc.kill()

    # -------------------------------------------------------------------------
    # initialization
    # -------------------------------------------------------------------------
    def __init__(self, commands):
        # create shell
        self.__shell = Terminal.Shell()
        # create commands
        for k, c in commands.items():
            setattr(self, k, Terminal.Command(self.__shell, c))

# -------------------------------------------------------------------------------------------------
# end
# -------------------------------------------------------------------------------------------------