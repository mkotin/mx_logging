from logging import StreamHandler

from mxlogging_m3lvx.log_record.LogRecordManager import LogRecordManager

""" This class catch stream logging and push them to the logs list """
class MXLoggingHandler(StreamHandler):

    def __init__(self):
        StreamHandler.__init__(self)
        self.logmanager = LogRecordManager()

    def emit(self, record):
        self.logmanager.add_log(record)