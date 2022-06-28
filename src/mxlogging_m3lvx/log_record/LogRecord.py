from logging import LogRecord

class LogRecord:

    def __init__(self, originalLogRecord: LogRecord):
        self.originalLogRecord = originalLogRecord.__dict__
        self.args = originalLogRecord.args
        self.asctime = originalLogRecord.asctime
        self.levelname = originalLogRecord.levelname
        self.levelno = originalLogRecord.levelno
        self.exc_info = originalLogRecord.exc_info
        self.lineno = originalLogRecord.lineno
        self.message = originalLogRecord.message
        self.module = originalLogRecord.module
        self.msecs = originalLogRecord.msecs
        self.msg = originalLogRecord.msg
        self.name = originalLogRecord.name
        self.filename = originalLogRecord.filename
        self.funcName = originalLogRecord.funcName
        self.pathname = originalLogRecord.pathname
        self.thread = originalLogRecord.thread
        self.threadName = originalLogRecord.threadName
        self.process = originalLogRecord.process
        self.processName = originalLogRecord.processName
        self.relativeCreated = originalLogRecord.relativeCreated
        self.stack_info = originalLogRecord.stack_info
