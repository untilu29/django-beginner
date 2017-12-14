from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import UploadFileForm
# from django.template import loader
from . import elron_filter
from estonia import insert_db
from django.core import serializers

from .models import Question
from estonia.models import *


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'index.html', context)


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question not exist')

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)


def upload_file(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        elron_filter.elron_filter(filename)
        uploaded_file_url = fs.url(filename)
        return render(request, 'upload.html', {
            'uploaded_file_url': 'media/estonia.zip'
        })
    return render(request, 'upload.html')


def handle_uploaded_file(f):
    with open('name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def insert_to_db(request):
    insert_db.insert('gtfs.zip')
    return HttpResponse("Done!")


def show_json(request):
    data = serializers.serialize("json", Agency.objects.all()[10:100])
    return HttpResponse(data, content_type='application/json')


def filter_by_agency(request, agency_name):
    app_name = 'estonia'

    routes = Routes.objects.raw("SELECT * from {app_name}_routes WHERE agency_id IN "
                                "(SELECT agency_id from {app_name}_agency WHERE agency_name='{agency}')".format(
        app_name=app_name,
        agency=agency_name
    ))

    trips = Trips.objects.raw("SELECT * from {app_name}_trips WHERE route_id IN "
                              "(SELECT route_id from {app_name}_routes WHERE agency_id IN "
                              "(SELECT agency_id from {app_name}_agency WHERE agency_name='{agency}'))".format(
        app_name=app_name,
        agency=agency_name
    ))

    shapes = Shapes.objects.raw("SELECT * from {app_name}_shapes WHERE shape_id IN "
                                "(SELECT shape_id from {app_name}_trips WHERE route_id IN "
                                "(SELECT route_id from {app_name}_routes WHERE agency_id IN "
                                "(SELECT agency_id from {app_name}_agency WHERE agency_name='{agency}')))".format(
        app_name=app_name,
        agency=agency_name
    ))

    calendars = Calendar.objects.raw("SELECT * from {app_name}_calendar WHERE service_id IN "
                                     "(SELECT service_id from {app_name}_trips WHERE route_id IN "
                                     "(SELECT route_id from {app_name}_routes WHERE agency_id IN "
                                     "(SELECT agency_id from {app_name}_agency WHERE agency_name='{agency}')))".format(
        app_name=app_name,
        agency=agency_name
    ))

    stop_times = StopTimes.objects.raw("SELECT 1 as id ,* from {app_name}_stoptimes WHERE trip_id IN "
                                       "(SELECT trip_id from {app_name}_trips WHERE route_id IN "
                                       "(SELECT route_id from {app_name}_routes WHERE agency_id IN "
                                       "(SELECT agency_id from {app_name}_agency WHERE agency_name='{agency}')))".format(
        app_name=app_name,
        agency=agency_name
    ))

    stops = Stops.objects.raw("SELECT * from {app_name}_stops WHERE stop_id IN "
                              "(SELECT stop_id from {app_name}_stoptimes WHERE trip_id IN "
                              "(SELECT trip_id from {app_name}_trips WHERE route_id IN "
                              "(SELECT route_id from {app_name}_routes WHERE agency_id IN "
                              "(SELECT agency_id from {app_name}_agency WHERE agency_name='{agency}'))))".format(
        app_name=app_name,
        agency=agency_name
    ))

    feed_info = FeedInfo.objects.all()

    fare_attr = FareAttributes.objects.raw("SELECT * from {app_name}_fareattributes WHERE agency_id IN "
                                           "(SELECT agency_id from {app_name}_agency WHERE agency_name='{agency}')".format(
        app_name=app_name,
        agency=agency_name
    ))

    fare_rules = FareRules.objects.raw("SELECT * from {app_name}_farerules WHERE route_id IN "
                                       "(SELECT route_id from {app_name}_routes WHERE agency_id IN "
                                       "(SELECT agency_id from {app_name}_agency WHERE agency_name='{agency}'))"
                                       "AND origin_id IN (SELECT zone_id from {app_name}_stops WHERE stop_id IN "
                                       "(SELECT stop_id from {app_name}_stoptimes WHERE trip_id IN "
                                       "(SELECT trip_id from {app_name}_trips WHERE route_id IN "
                                       "(SELECT route_id from {app_name}_routes WHERE agency_id IN "
                                       "(SELECT agency_id from {app_name}_agency WHERE agency_name='{agency}')))))"
                                       "AND destination_id IN (SELECT zone_id from {app_name}_stops WHERE stop_id IN "
                                       "(SELECT stop_id from {app_name}_stoptimes WHERE trip_id IN "
                                       "(SELECT trip_id from {app_name}_trips WHERE route_id IN "
                                       "(SELECT route_id from {app_name}_routes WHERE agency_id IN "
                                       "(SELECT agency_id from {app_name}_agency WHERE agency_name='{agency}')))))".format(
        app_name=app_name,
        agency=agency_name
    ))


    list_fare = list(fare_rules)

    return HttpResponse(serializers.serialize("json", fare_rules), content_type='application/json')
