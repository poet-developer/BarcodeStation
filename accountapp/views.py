from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):

    if request.method == 'POST':
        temp = request.POST.get('input_text')
        return render(request,'accountapp/home.html',context={'text':temp})
    else:
        return render(request, 'accountapp/home.html', context={'text':'.'})