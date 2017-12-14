from django.db import models


class Agency(models.Model):
    agency_id = models.CharField(primary_key=True, editable=True, max_length=255)
    agency_name = models.CharField(max_length=255)
    agency_url = models.CharField(max_length=512)
    agency_timezone = models.CharField(max_length=255)
    agency_phone = models.CharField(max_length=255)
    agency_lang = models.CharField(max_length=255)

    def __str__(self):
        return self.agency_name


class Calendar(models.Model):
    service_id = models.CharField(primary_key=True, editable=True, max_length=255)
    monday = models.BooleanField()
    tuesday = models.BooleanField()
    wednesday = models.BooleanField()
    thursday = models.BooleanField()
    friday = models.BooleanField()
    saturday = models.BooleanField()
    sunday = models.BooleanField()
    start_date = models.CharField(max_length=255)
    end_date = models.CharField(max_length=255)


class CalendarDates(models.Model):
    service_id = models.CharField(primary_key=True, editable=True, max_length=255)
    date = models.CharField(max_length=255)
    exception_type = models.CharField(max_length=255)


class FareAttributes(models.Model):
    fare_id = models.CharField(primary_key=True, editable=True, max_length=255)
    price = models.CharField(max_length=255)
    currency_type = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=255)
    transfers = models.CharField(max_length=255)
    agency_id = models.CharField(max_length=255)


class FareRules(models.Model):
    fare_id = models.CharField(primary_key=True, editable=True, max_length=255)
    route_id = models.CharField(max_length=255)
    origin_id = models.CharField(max_length=255)
    destination_id = models.CharField(max_length=255)


class FeedInfo(models.Model):
    feed_publisher_name = models.CharField(max_length=255)
    feed_publisher_url = models.CharField(max_length=255)
    feed_lang = models.CharField(max_length=255)


class Routes(models.Model):
    route_id = models.CharField(primary_key=True, editable=True, max_length=255)
    agency_id = models.CharField(max_length=255)
    route_short_name = models.CharField(max_length=255)
    route_long_name = models.CharField(max_length=255)
    route_type = models.CharField(max_length=255)
    route_color = models.CharField(max_length=255)
    competent_authority = models.CharField(max_length=255)


class Shapes(models.Model):
    shape_id = models.CharField(primary_key=True, editable=True, max_length=255)
    shape_pt_lat = models.FloatField()
    shape_pt_lon = models.FloatField()
    shape_pt_sequence = models.CharField(max_length=255)


class StopTimes(models.Model):
    trip_id = models.CharField(max_length=255)
    arrival_time = models.CharField(max_length=255)
    departure_time = models.CharField(max_length=255)
    stop_id = models.CharField(max_length=255)
    stop_sequence = models.CharField(max_length=255)
    pickup_type = models.CharField(max_length=255)
    drop_off_type = models.CharField(max_length=255)


class Stops(models.Model):
    stop_id = models.CharField(primary_key=True, editable=True, max_length=255)
    stop_code = models.CharField(max_length=255)
    stop_name = models.CharField(max_length=255)
    stop_lat = models.FloatField()
    stop_lon = models.FloatField()
    zone_id = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    stop_area = models.CharField(max_length=255)
    stop_desc = models.CharField(max_length=255)
    zone_name = models.CharField(max_length=255)
    location_type = models.CharField(max_length=255)
    parent_station = models.CharField(max_length=255)


class Trips(models.Model):
    route_id = models.CharField(primary_key=True, editable=True, max_length=255)
    service_id = models.CharField(max_length=255)
    trip_id = models.CharField(max_length=255)
    trip_headsign = models.CharField(max_length=255)
    trip_long_name = models.CharField(max_length=255)
    direction_code = models.CharField(max_length=255)
    shape_id = models.CharField(max_length=255)
    wheelchair_accessible = models.CharField(max_length=255)
