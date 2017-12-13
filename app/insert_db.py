import pandas as pd
import zipfile as zf
from django.conf import settings
from django.db import transaction
from elron.models import *
from sqlalchemy import create_engine


@transaction.atomic
def insert(filename):
    # Input file here
    output_folder = settings.MEDIA_ROOT
    zipInput = zf.ZipFile(output_folder + "/" + filename, "r")

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

    shape = pd.read_csv(zipInput.open(SHAPE))
    for item in shape.fillna('').to_dict('records'):
        sp = Shapes(**item)
        sp.save()
        sid = transaction.savepoint()
    transaction.savepoint_commit(sid)

    user = settings.DATABASES['default']['USER']
    password = settings.DATABASES['default']['PASSWORD']
    database_name = settings.DATABASES['default']['NAME']
    database_host = settings.DATABASES['default']['HOST']
    database_port = settings.DATABASES['default']['PORT']

    database_url = 'postgresql://{user}:{password}@{database_host}:{database_port}/{database_name}'.format(
        user=user,
        password=password,
        database_name=database_name,
        database_host=database_host,
        database_port=database_port
    )

    engine = create_engine(database_url, echo=False)
    # pd.read_csv(zipInput.open(AGENCY)).fillna('').to_sql(Agency._meta.db_table, con=engine, if_exists='replace',
    #                                                      index=False, chunksize=50)
    # pd.read_csv(zipInput.open(FEED_INFO)).fillna('').to_sql(FeedInfo._meta.db_table, con=engine, if_exists='replace',
    #                                                         index=False, chunksize=50)
    # pd.read_csv(zipInput.open(FARE_ATT)).fillna('').to_sql(FareRules._meta.db_table, con=engine, if_exists='replace',
    #                                                        index=False, chunksize=50)
    # pd.read_csv(zipInput.open(FARE_RULE)).fillna('').to_sql(FareRules._meta.db_table, con=engine, if_exists='replace',
    #                                                         index=False, chunksize=50)
    # pd.read_csv(zipInput.open(ROUTE)).fillna('').to_sql(Routes._meta.db_table, con=engine, if_exists='replace',
    #                                                     index=False, chunksize=50)
    # pd.read_csv(zipInput.open(TRIP)).fillna('').to_sql(Trips._meta.db_table, con=engine, if_exists='replace',
    #                                                    index=False, chunksize=50)
    # pd.read_csv(zipInput.open(CALENDAR)).fillna('').to_sql(Calendar._meta.db_table, con=engine, if_exists='replace',
    #                                                        index=False, chunksize=50)
    # pd.read_csv(zipInput.open(CALENDAR_DATE)).fillna('').to_sql(CalendarDates._meta.db_table, con=engine,
    #                                                             if_exists='replace', index=False, chunksize=50)
    # pd.read_csv(zipInput.open(SHAPE)).fillna('').to_sql(Shapes._meta.db_table, con=engine, if_exists='replace',
    #                                                     index=False, chunksize=5)
    # pd.read_csv(zipInput.open(STOP_TIME)).fillna('').to_sql(StopTimes._meta.db_table, con=engine, if_exists='replace',
    #                                                         index=False, chunksize=50)
    # pd.read_csv(zipInput.open(STOP)).fillna('').to_sql(Stops._meta.db_table, con=engine, if_exists='replace',
    #                                                    index=False, chunksize=5)

    return
