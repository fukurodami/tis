from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View
from .models import Service
from .forms import OrderForm


class CatalogView(View):

    def get(self, request):
        serveses = Service.objects.all()
        if request.user.is_authenticated:
            return render(request, "catalog/catalog.html", {"serveses": serveses})
        else:
            return render(request, "registration/login.html")

class UsView(View):
    """О нас страница"""

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, "catalog/us.html")
        else:
            return render(request, "registration/login.html")



class PostView(View):
    """Главная страница"""

    def get(self, request, pk):
        serveses = Service.objects.get(id=pk)
        if request.user.is_authenticated:
            if request.method == 'POST':
                form = OrderForm(request.POST)
                print(form.title)
                if form.is_valid:

                    form.save()
                    return HttpResponseRedirect('/')
            else:
                form = OrderForm()
                return render(request, "catalog/order.html", {'serveses': serveses, 'form': form})
        else:
            return render(request, "registration/login.html")

    def post(self, request, pk):
        serveses = Service.objects.get(id=pk)
        if request.user.is_authenticated:
            if request.method == 'POST':
                form = OrderForm(request.POST)
                if form.is_valid:
                    forma = form.save(commit=False)
                    forma.title = serveses
                    forma.save()
                    return HttpResponseRedirect('/')
            else:
                form = OrderForm()
                return render(request, "catalog/order.html", {'serveses': serveses, 'form': form})
        else:
            return render(request, "registration/login.html")
