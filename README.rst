This stuff is mostly copied from answers from this SO question:
http://stackoverflow.com/questions/1736015/debugging-a-pyqt4-app, but bundled
in a Python package for convenience, and includes *one* minor change (calling
``set_trace()`` instead of ``interaction()``) that makes it work better (e.g.
``next`` would not work properly otherwise).

Install::

    $ sudo pip install git+https://github.com/jackieleng/qtdb.git

Set a breakpoint::

    import qtdb; qtdb.set_trace()
