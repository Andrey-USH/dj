from django.urls import path
from .views import *

urlpatterns = [
    path('', General.as_view(), name='general'),
    path('deparment/<int:department_id>/', GetDep.as_view(), name='department'),
    path('staff/<int:pk>/', Detail.as_view(), name='get_staff'),
    path('/sort/', filter_symbol, name='sort'),
]
