from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accountapp.models import TextDB


def home(request):

    if request.method == 'POST':
        temp = request.POST.get('input_text')
        initial_DB = TextDB()
        initial_DB.text = temp
        initial_DB.save()

        return HttpResponseRedirect('.')
    else:
        text = TextDB.objects.all()

        return render(request, 'accountapp/home.html', context={'text':text})

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:home')
    template_name = 'accountapp/create.html'