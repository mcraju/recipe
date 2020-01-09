from django.shortcuts import render,HttpResponseRedirect
from .models import Foody
from django.urls import reverse


def menu(request):
    foody_menu = Foody.objects.all()
    return render(request, 'foody/menu.html', {'foody_menu': foody_menu})


def make_over(request):
    return render(request, 'foody/make.html')


def save(request):
    Foody.objects.create(name = request.POST['name'],
                         ingredients= request.POST['ingredients'],
                         process = request.POST['process'],
                          )
    return HttpResponseRedirect(reverse('foody:menu'))

def display(request, f_id):
    foody = Foody.objects.get(pk=f_id)
    return render(request, 'foody/details.html', {'foody': foody})



