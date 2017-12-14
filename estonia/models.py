from django.db import models


class Agency(models.Model):
    agency_id = models.TextField(primary_key=True, editable=True)
    agency_name = models.TextField(null=True)
    agency_url = models.TextField(null=True)
    agency_timezone = models.TextField(null=True)
    agency_phone = models.TextField(null=True)
    agency_lang = models.TextField(null=True)

    def __str__(self):
        return self.agency_name


class Calendar(models.Model):
    service_id = models.TextField()
    monday = models.CharField(max_length=1)
    tuesday = models.CharField(max_length=1)
    wednesday = models.CharField(max_length=1)
    thursday = models.CharField(max_length=1)
    friday = models.CharField(max_length=1)
    saturday = models.CharField(max_length=1)
    sunday = models.CharField(max_length=1)
    start_date = models.TextField()
    end_date = models.TextField()


class CalendarDates(models.Model):
    service_id = models.TextField()
    date = models.TextField()
    exception_type = models.TextField(null=True)


class FareAttributes(models.Model):
    fare_id = models.TextField()
    price = models.TextField(null=True)
    currency_type = models.TextField(null=True)
    payment_method = models.TextField(null=True)
    transfers = models.TextField(null=True)
    agency_id = models.TextField()


class FareRules(models.Model):
    fare_id = models.TextField()
    route_id = models.TextField()
    origin_id = models.TextField()
    destination_id = models.TextField()


class FeedInfo(models.Model):
    feed_publisher_name = models.TextField()
    feed_publisher_url = models.TextField()
    feed_lang = models.TextField()


class Routes(models.Model):
    route_id = models.TextField(primary_key=True, editable=True)
    agency_id = models.TextField()
    route_short_name = models.TextField(null=True)
    route_long_name = models.TextField(null=True)
    route_type = models.TextField(null=True)
    route_color = models.TextField(null=True)
    competent_authority = models.TextField(null=True)


class Shapes(models.Model):
    shape_id = models.TextField()
    shape_pt_lat = models.FloatField()
    shape_pt_lon = models.FloatField()
    shape_pt_sequence = models.TextField()


class StopTimes(models.Model):
    trip_id = models.TextField()
    arrival_time = models.TextField(null=True)
    departure_time = models.TextField(null=True)
    stop_id = models.TextField()
    stop_sequence = models.TextField()
    pickup_type = models.TextField(null=True)
    drop_off_type = models.TextField(null=True)


class Stops(models.Model):
    stop_id = models.TextField(primary_key=True, editable=True)
    stop_code = models.TextField(null=True)
    stop_name = models.TextField(null=True)
    stop_lat = models.FloatField()
    stop_lon = models.FloatField()
    zone_id = models.TextField()
    alias = models.TextField(null=True)
    stop_area = models.TextField(null=True)
    stop_desc = models.TextField(null=True)
    lest_x = models.FloatField()
    lest_y = models.FloatField()
    zone_name = models.TextField(null=True)
    location_type = models.TextField(null=True)
    parent_station = models.TextField(null=True)


class Trips(models.Model):
    route_id = models.TextField()
    service_id = models.TextField()
    trip_id = models.TextField()
    trip_headsign = models.TextField(null=True)
    trip_long_name = models.TextField(null=True)
    direction_code = models.TextField(null=True)
    shape_id = models.TextField(null=True)
    wheelchair_accessible = models.TextField(null=True)
