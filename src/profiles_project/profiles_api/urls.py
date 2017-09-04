from django.conf.urls import url
import profiles_api.views

app_name = 'profiles_api'


urlpatterns = [
    url(r'^hello', profiles_api.views.HelloApiView.as_view(), name='hello'),
]
