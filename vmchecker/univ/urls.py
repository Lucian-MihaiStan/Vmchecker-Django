from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('universities', views.UniversitiesListView.as_view(), name='universities'),
    path('univ-list', views.univ_list, name='univ-list'),
]
