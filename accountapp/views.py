from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
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