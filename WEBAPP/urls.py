from django.urls import path
from . views import hi, hello, how, are
from . import views


urlpatterns = [
    path('', views.hi, name='MATRIX'),
    path('', views.hello, name='HOME'),
    path('', views.hello, name='FORMULAS'),
    path('', views.are, name='CALENDAR'),

]
