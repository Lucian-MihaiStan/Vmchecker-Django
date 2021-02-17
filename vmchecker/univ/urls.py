from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('universities', views.UniversitiesListView.as_view(), name='universities'),
    path('univ-list', views.univ_list, name='univ-list'),
    path('univ/<int:pk>', views.UniversityDetailView.as_view(), name='university-detail'),
    path('subject/<int:pk>', views.SubjectDetailView.as_view(), name='subject-detail'),
]
