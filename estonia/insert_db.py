import zipfile as zf
from django.conf import settings
from .models import *
# from sqlalchemy import create_engine
from django.db import connection

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger("Time calculate")

def insert(filename):
    output_folder = settings.MEDIA_ROOT
    zipInput = zf.ZipFile(output_folder + "/" + filename, "r")

    DELIMITER = ','
    AGENCY = "agency.txt"
    FEED_INFO = "feed_info.txt"
    FARE_ATT = "fare_attributes.txt"
    FARE_RULE = "fare_rules.txt"
    ROUTE = "routes.txt"
    TRIP = "trips.txt"
    CALENDAR = "calendar.txt"
    CALENDAR_DATE = "calendar_dates.txt"
    SHAPE = "shapes.txt"
    STOP_TIME = "stop_times.txt"
    STOP = "stops.txt"

    copy_command = "COPY {table_name}({header}) FROM STDIN WITH CSV HEADER DELIMITER AS '" + DELIMITER + "'"

    with connection.cursor() as cursor:
        cursor_insert(cursor, copy_command, Agency, zipInput.open(AGENCY))
        cursor_insert(cursor, copy_command, FeedInfo, zipInput.open(FEED_INFO))
        cursor_insert(cursor, copy_command, FareAttributes, zipInput.open(FARE_ATT))
        cursor_insert(cursor, copy_command, FareRules, zipInput.open(FARE_RULE))
        cursor_insert(cursor, copy_command, Routes, zipInput.open(ROUTE))
        cursor_insert(cursor, copy_command, Trips, zipInput.open(TRIP))
        cursor_insert(cursor, copy_command, Calendar, zipInput.open(CALENDAR))
        cursor_insert(cursor, copy_command, CalendarDates, zipInput.open(CALENDAR_DATE))
        cursor_insert(cursor, copy_command, Shapes, zipInput.open(SHAPE))
        cursor_insert(cursor, copy_command, StopTimes, zipInput.open(STOP_TIME))
        cursor_insert(cursor, copy_command, Stops, zipInput.open(STOP))
        return


def cursor_insert(cursor, copy_command, Model, fileInput):
    cursor.copy_expert(
        copy_command.format(table_name=Model._meta.db_table, header=fileInput.readline().decode("utf-8")), fileInput)
    return
