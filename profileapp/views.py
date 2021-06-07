from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.dacorators import profile_has_ownship
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile

Profile_decortors =[login_required,profile_has_ownship]

class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accountapp:detail',kwargs={'pk':self.object.user.pk})

@method_decorator(Profile_decortors,'get')
@method_decorator(Profile_decortors,'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail',kwargs={'pk':self.object.user.pk})

