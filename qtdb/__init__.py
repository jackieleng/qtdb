#! /usr/bin/env python
"""
pdb for pyqt4

Most of this is from: http://stackoverflow.com/questions/1736015/debugging-a-pyqt4-app
"""


def set_trace():
    '''Set a tracepoint in the Python debugger that works with Qt'''
    from PyQt4.QtCore import pyqtRemoveInputHook
    import pdb
    import sys
    pyqtRemoveInputHook()
    # set up the debugger
    debugger = pdb.Pdb()
    debugger.reset()
    # custom next to get outside of function scope
    debugger.do_next(None)  # run the next command
    users_frame = sys._getframe().f_back  # frame where the user invoked `pyqt_set_trace()`

    # debugger.interaction(users_frame, None)
    debugger.set_trace(users_frame)  # Using this, it is possible to step through using 'next':
