from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^reservation/$',views.Room_Reservation, name = 'Room_Reservation'),
    url(r'^reservation/(?P<pk_2>\d+)/$', views.reservation_detail, name='reservation_detail'),
    url(r'^reservation/new/$', views.reservation_new, name = 'reservation_new'),
]
