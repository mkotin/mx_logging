from logging import LogRecord
from mxlogging_m3lvx.log_record.LogRecordManagerMeta import LogRecordManagerMeta
from mxlogging_m3lvx.log_record.LogRecord import LogRecord as MXLogRecord
import json, queue


class LogRecordManager(metaclass=LogRecordManagerMeta):

    def __init__(self):
        self.logrecords_queue = queue.Queue()

    #
    #
    def add_log(self, record: LogRecord):
        record = MXLogRecord(record)
        record = json.dumps(record.__dict__)
        self.logrecords_queue.put(record)
        
    

    # #
    # #
    # def get_log(self, start, count):
    #     return self.logrecords[0]


    # #
    # #
    # def get_logs(self):
    #     return self.logrecords


    # #
    # #
    # def tail(self, number):
    #     pass
    

    # #
    # #
    # def clear(self):
    #     pass


    # #
    # #
    # def get_logs_str(self):
    #     pass

