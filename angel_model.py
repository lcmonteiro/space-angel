#!/usr/bin/env python3
# -----------------------------------------------------------------------------
# imports
# -----------------------------------------------------------------------------
from sys           import argv
from pprint        import pprint
# ---------------------------------------------------------
# base
# ---------------------------------------------------------
from space_angel   import Angel
from space_angel   import Logger
# ---------------------------------------------------------
# decorators
# ---------------------------------------------------------
from space_angel    import git_angel
from space_angel    import terminal_gate
# -----------------------------------------------------------------------------
# process
# -----------------------------------------------------------------------------
@git_angel
class MyAngel(Angel):
    def _pipeline(self):
        # ---------------------------------------------------------
        # build
        # ---------------------------------------------------------
        @self.gate('build')
        @terminal_gate
        def build(self, backlog):
            log = Logger()
            # build code
            pprint(log('build.1', self.terminal.build))

            {
                'header': None,
                'result': None,
                'log' :[

                ],
                'err':[

                ],
                'sub':[
                    {

                    }
                ]
            }
            return log
        # ---------------------------------------------------------
        # test
        # ---------------------------------------------------------
        @self.gate('test')
        def test(self, data):
            print("test")
            return data
        # ---------------------------------------------------------
        # report
        # ---------------------------------------------------------
        @self.gate('report')
        #@gate.markdown
        def report(self, data):
            print("report")
            return data
# -----------------------------------------------------------------------------
# main
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    MyAngel(argv[1]).run()