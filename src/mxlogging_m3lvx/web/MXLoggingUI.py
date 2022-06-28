from mxlogging_m3lvx.web.app import app
from mxlogging_m3lvx.web.websocketserver import socketio
from contextlib import contextmanager

import logging
import sys, os
import threading

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout

def runFlaskApp():
        print("MXLogging UI running at http://127.0.0.1:5343")
        # Disable flask logging
        log = logging.getLogger('werkzeug')
        log.setLevel(logging.ERROR)

        with suppress_stdout():
            socketio.run(app, host = '0.0.0.0', port = 5343, debug = False, use_reloader=False) # TODO: handle busy port

class MXLoggingUI:

    def __init__(self):
        pass


    @staticmethod
    def launch():
        threading.Thread(target=runFlaskApp, daemon=True).start()