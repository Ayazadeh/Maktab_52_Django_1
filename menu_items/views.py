from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView
from .models import *


class Menu(ListView):
    template_name = 'basepage.html'


# def create_menu_item(request):
#     from .forms import CreateMenuItem
#     if request.method == 'POST':
#         form = CreateMenuItem(request.POST, request.FILES)
#         if form.is_valid():
#             print(form.cleaned_data)
#             MenuItems.objects.create(name=form.cleaned_data['name'],
#                                      price=form.cleaned_data['price'],
#                                      discount=form.cleaned_data['discount'],
#                                      image=form.cleaned_data['image'],
#                                      category=form.cleaned_data['category'],
#                                      starting_cooking_time=timezone.now())
#             return HttpResponse('ok :)')
#
#     else:
#         form = CreateMenuItem()
#     return render(request, 'create_menu_item.html', {'form': form})

def create_menu_item(request):
    from .forms import CreateMenuItem
    if request.method == 'POST':
        form = CreateMenuItem(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponse('ok :)')
    else:
        form = CreateMenuItem()
    return render(request, 'create_menu_item.html', {'form': form})