from . import views
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'agency', views.AgencyViewSet, base_name='agency')

urlpatterns = [
    url(r'^', include(router.urls)),
]