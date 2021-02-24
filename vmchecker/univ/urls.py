from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('universities', views.UniversitiesListView.as_view(), name='universities'),
    path('homeworks', views.HomeworkListView.as_view(), name='homeworks'),
    path('subjects', views.SubjectsListView.as_view(), name='subjects'),
    path('univ-list', views.univ_list, name='univ-list'),
    path('univ/<int:pk>', views.UniversityDetailView.as_view(), name='university-detail'),
    path('subject/<int:pk>', views.SubjectDetailView.as_view(), name='subject-detail'),
    path('homework/<int:pk>', views.HomeworkDetailView.as_view(), name='homework-detail'),
    path('year/<int:pk>', views.YearDetailView.as_view(), name='year-detail')
]
