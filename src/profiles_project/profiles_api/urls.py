from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

import profiles_api.views

app_name = 'profiles_api'

router = DefaultRouter()
router.register('viewset', profiles_api.views.HelloViewSet, base_name='viewset')

urlpatterns = [
    url(r'^hello', profiles_api.views.HelloApiView.as_view(), name='hello'),
    url(r'', include(router.urls), name='viewset'),
]
