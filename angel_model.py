#!/usr/bin/env python3
# -----------------------------------------------------------------------------
# imports
# -----------------------------------------------------------------------------
from sys      import argv
from kernel   import Angel
# ---------------------------------------------------------
# decorators
# ---------------------------------------------------------
from angels   import git_angel
from gates    import terminal_gate
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
        def build(self, data):
            print(self._context.base.monitor)
            print(self._context.gate.commands)
            return data
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