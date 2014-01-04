#!/usr/bin/env python
#coding=utf-8

import logging, os

class Logger:
    def __init__(self, path,
                 cli_level=logging.DEBUG,
                 file_level=logging.DEBUG):
        self.logger = logging.getLogger(path)
        self.logger.setLevel(logging.DEBUG)
        format = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        sh = logging.StreamHandler()
        sh.setFormatter(format)
        sh.setLevel(cli_level)

        fh = logging.FileHandler(path)
        fh.setFormatter(format)
        fh.setLevel(file_level)

        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def debug(self, message=None):
        self.logger.debug(message)

    def info(self, message=None):
        self.logger.info(message)

    def warn(self, message=None):
        self.logger.warn(message)

    def error(self, message=None):
        self.logger.error(message)

    def critical(self, message=None):
        self.logger.critical(message)

def log_test():
    logger1 = Logger('/tmp/pylog.txt',
                     cli_level=logging.ERROR,
                     file_level=logging.DEBUG)
    logger1.debug("a debug msg of test")
    logger1.info("a info msg of test")
    logger1.warn("a warn msg of test")
    logger1.error("a error msg of test")
    logger1.critical(" a cirtical msg of test")

if __name__ == "__main__":
    log_test()
