from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('upload', views.upload_file, name='upload'),
    path('insert', views.insert_to_db, name='insert'),
    path('json', views.show_json, name='json'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('agency/<str:agency_name>/', views.filter_by_agency, name='agency_name'),
]
