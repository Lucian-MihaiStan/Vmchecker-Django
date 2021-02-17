from django.shortcuts import render
from .models import Univ, UnivInstance, Homework, Subject, Year
from django.views import generic


# Create your views here.


def index(request):
    num_books = Univ.objects.all().count()
    num_instance = UnivInstance.objects.all().count()

    context = {
        'num_books': num_books,
        'num_instance': num_instance
    }

    return render(request, 'index.html', context=context)


def univ_list(request):
    univ_list = Univ.objects.all()
    context = {
        'univ_list': univ_list
    }
    return render(request, 'univ/univ_list.html', context=context)


class UniversitiesListView(generic.ListView):
    model = Univ
    paginate_by = 10
