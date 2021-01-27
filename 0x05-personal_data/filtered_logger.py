#!/usr/bin/env python3
"""
regex-ing
"""

from typing import List
import logging
import os
import re
import mysql.connector

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'ip')


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """return the log message"""
    temp = message
    for field in fields:
        temp = re.sub(field + "=.*?" + separator,
                      field + "=" + redaction + separator, temp)
    return temp

def get_logger() -> logging.Logger:
    """returns logger obj"""
    return logging.getLogger('user_data')


def get_db() -> mysql.connector.connection.MySQLConnection:
    """connect to mysql db"""
    user = os.environ.get('PERSONAL_DATA_DB_PASSWORD', None)
    password = os.environ.get('PERSONAL_DATA_DB_PASSWORD', None)
    db_host = os.environ.get('PERSONAL_DATA_DB_HOST', None)
    db_name = os.environ.get('PERSONAL_DATA_DB_NAME', None)

    return mysql.connector.connect(user=user,
                                   password=password,
                                   host=db_host,
                                   database=db_name)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """init class"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """filters values in incoming log records"""
        return filter_datum(
            self.fields, self.REDACTION, super(
                RedactingFormatter, self).format(record),
            self.SEPARATOR)
