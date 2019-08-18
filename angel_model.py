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
from space_angel    import angel_git
from space_angel    import gate_terminal
from space_angel    import gate_parser
from space_angel    import gate_markdown
# -----------------------------------------------------------------------------
# process
# -----------------------------------------------------------------------------
@angel_git
class MyAngel(Angel):
    def _pipeline(self):
        # ---------------------------------------------------------
        # build
        # ---------------------------------------------------------
        @self.gate('build')
        @gate_terminal
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
        @gate_parser('junit')
        def test(self, log, backlog):
            log('result', self.parser.load)

        # ---------------------------------------------------------
        # report
        # ---------------------------------------------------------
        @self.gate_force('report')
        @gate_markdown
        def report(self, log, backlog):
            log('save', self.markdown.save, backlog)

        
# -----------------------------------------------------------------------------
# main
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    start(MyAngel)