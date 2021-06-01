from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import UserUpdateForm
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

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name =  'accountapp/detail.html'

class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = UserUpdateForm
    success_url = reverse_lazy('accountapp:home')
    template_name = 'accountapp/update.html'

class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:home')
    template_name =  'accountapp/delete.html'