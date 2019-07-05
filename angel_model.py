#!/usr/bin/env python3
# -----------------------------------------------------------------------------
# imports
# -----------------------------------------------------------------------------
from kernel.angel import Angel
# -----------------------------------------------------------------------------
# process
# -----------------------------------------------------------------------------
process = Angel()
# -----------------------------------------------------------------------------
# gates
# -----------------------------------------------------------------------------
# build
# ---------------------------------------------------------
@process.gate('build')
#@gate.cmake
def build(data):
    print("build")
    return data
# ---------------------------------------------------------
# test
# ---------------------------------------------------------
@process.gate('test')
#@gate.ctest
def test(data):
    print("test")
    return data
# ---------------------------------------------------------
# report
# ---------------------------------------------------------
@process.gate('report')
#@gate.markdown
def report(data):
    return data
# -----------------------------------------------------------------------------
# main
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    process.run()