from django.conf.urls import url
from api.views import candidate_list

from api.views import candidate_detail

urlpatterns = [

    url(r'^candidate/$', candidate_list, name='candidate_list'),
    url(r'^candidate/(?P<pk>[0-9]+)$', candidate_detail, name='candidate_detail'),
]