from flask_socketio import SocketIO
from threading import Lock
from mxlogging_m3lvx.web.app import app
from mxlogging_m3lvx.log_record.LogRecordManager import LogRecordManager

# SocketIO
async_mode = None
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

def background_thread():
    q = LogRecordManager().logrecords_queue
    while True:
        socketio.sleep(1)
        item = q.get()
        socketio.emit('new_log_record', item)

@socketio.event
def client_connected():
    print("Websocket client is connected")

@socketio.event
def connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)