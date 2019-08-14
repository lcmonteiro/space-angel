#!/usr/bin/env python3
# -----------------------------------------------------------------------------
# imports
# -----------------------------------------------------------------------------
from pprint        import pprint
# ---------------------------------------------------------
# base
# ---------------------------------------------------------
from space_angel   import start
from space_angel   import Angel
# ---------------------------------------------------------
# decorators
# ---------------------------------------------------------
from space_angel    import git_angel
from space_angel    import terminal_gate
from space_angel    import markdown_gate
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
        def build(self, log, backlog):
            # build code
            #log('build.1', self.terminal.build, base_result=0.9)
            log('build.1', self.terminal.build)

            # {
            #     'header': None,
            #     'result': None,
            #     'log' :[

            #     ],
            #     'err':[

            #     ],
            #     'sub':[
            #         {

            #         }
            #     ]
            # }

        # ---------------------------------------------------------
        # test
        # ---------------------------------------------------------
        @self.gate('test')
        def test(self, log, backlog):
            print("test")

        # ---------------------------------------------------------
        # report
        # ---------------------------------------------------------
        @self.gate_force('report')
        @markdown_gate
        def report(self, log, backlog):
            log('save', self.markdown.save(backlog))

        
# -----------------------------------------------------------------------------
# main
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    start(MyAngel)