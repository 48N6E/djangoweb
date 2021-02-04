from django.conf.urls import url
from .views import reg,show

urlpatterns = [
    url(r'^reg$',reg),
    url(r'^show$',show)
]
